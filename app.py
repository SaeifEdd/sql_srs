import io
import streamlit as st
import pandas as pd
import duckdb


CSV = """
beverage,price
orange juice, 2.5
expresso, 2
Tea, 3
citronade, 3.5
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_prices
cookie juice, 2.5
chocolatine, 5
muffin, 4
cheese cake, 7
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages 
CROSS JOIN food_items
"""
solution_df = duckdb.sql(ANSWER_STR).df()


st.write(
    """
         # SQL SRS 
         SQL Spaced Repetition
         System"""
)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "Group by", "Windows Functions"),
        index=None,
        placeholder="Select contact method...",
    )

    st.write("You selected:", option)


st.header("enter your code")
query = st.text_area(label="write your sql command", key="user input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("There are some missing columns")

    rows_difference = result.shape[0] - solution_df.shape[0]
    if rows_difference != 0:
        st.write(f"result has {rows_difference} rows different than solution")


tab1, tab2 = st.tabs(["tables", "solution"])

with tab1:
    st.write("beverages")
    st.dataframe(beverages)
    st.write("foods")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution_df)

with tab2:
    st.write(ANSWER_STR)
