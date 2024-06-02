import logging
import os
import logging
import streamlit as st
import duckdb
from datetime import date, timedelta

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("making data folder")
    os.mkdir("data")

if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)


def check_user_solution(user_query: str) -> None:
    """
    Checks if user solution is correct by:
    1: compare columns
    2: compare number of rows
    :param user_query: string contains the query entered by user
    :return:
    """
    result = con.execute(user_query).df()
    st.dataframe(result)
    try:
        result = result[solution_df.columns]
        comparison = result.compare(solution_df)
        if comparison.empty:
            st.balloons()
            st.write("That's Correct !")
        else:
            st.dataframe(comparison)
            st.write("try again !")

    except KeyError as e:
        st.write("There are some missing columns")
    rows_difference = result.shape[0] - solution_df.shape[0]
    if rows_difference != 0:
        st.write(f"result has {rows_difference} rows different than solution")


st.write(
    """
         # SQL SRS 
         SQL Spaced Repetition
         System"""
)

with st.sidebar:
    available_themes = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What would you like to review?",
        available_themes["theme"].unique(),
        index=None,
        placeholder="Select a topic...",
    )
    if theme:
        st.write("You selected:", theme)
        select_exercise_query = f"SELECT * FROM memory_state where theme = '{theme}' "

    else:
        select_exercise_query = "SELECT * FROM memory_state"

    exercise = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    st.write(exercise)
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("enter your code")
query = st.text_area(label="write your sql command", key="user input")


if query:
    check_user_solution(query)

for n_days in [2, 7, 21]:
    if st.button(f"review in {n_days} days"):
        next_review = date.today() + timedelta(days=n_days)
        con.execute(
            f"UPDATE memory_state SET last_reviewed = '{next_review}' where exercise_name = '{exercise_name}'"
        )
        st.rerun()


if st.button("Reset"):
    con.execute("UPDATE memory_state set last_reviewed = '1970-01-01'")
    st.rerun()

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        table_df = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(table_df)
#     st.write("beverages")
#     st.dataframe(beverages)
#     st.write("foods")
#     st.dataframe(food_items)
#     st.write("expected")
#     st.dataframe(solution_df)
#
with tab2:
    st.write(answer)
