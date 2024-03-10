import streamlit as st
import pandas as pd
import duckdb as db


st.write('SQL Spaced Repetition '
         'System')

option = st.selectbox(
   "What would you like to review?",
   ("Joins", "Groupby", "windows Functions"),
   index=None,
   placeholder="Select contact method...",
)

st.write('You selected:', option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label='write your sql command')
    result = db.query(sql_query).df()
    st.write(f"your sql command is: {sql_query}")
    st.dataframe(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


