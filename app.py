import ast
import streamlit as st
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

ANSWER_STR = """
SELECT * FROM beverages 
CROSS JOIN food_items
"""
#solution_df = duckdb.sql(ANSWER_STR).df()


st.write(
    """
         # SQL SRS 
         SQL Spaced Repetition
         System"""
)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross join", "Group by", "window_functions"),
        index=None,
        placeholder="Select a topic...",
    )

    st.write("You selected:", theme)
    exercise = con.execute(f"SELECT * FROM memory_state where theme = '{theme}' ").df()
    st.write(exercise)

st.header("enter your code")
query = st.text_area(label="write your sql command", key="user input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

    # try:
    #     result = result[solution_df.columns]
    #     st.dataframe(result.compare(solution_df))
    # except KeyError as e:
    #     st.write("There are some missing columns")
    #
    # rows_difference = result.shape[0] - solution_df.shape[0]
    # if rows_difference != 0:
    #     st.write(f"result has {rows_difference} rows different than solution")


tab1, tab2 = st.tabs(["tables", "solution"])

with tab1:
    exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f"table:{table}")
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
    exercise_name = exercise.loc[0, "exercise name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)
