import streamlit as st
import pandas as pd
import duckdb as db
import io

csv = '''
beverages, price
orange juice, 2.5
expresso, 2
Tea, 3
citronade, 3.5
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item, food_price
cookie juice, 2.5
chocolatine, 5
muffin, 4
cheeze cake, 7
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = '''
SELECT * FROM beverages 
CROSS JOIN food_items
'''
solution = db.sql(answer).df()


st.write("""
         # SQL SRS 
         SQL Spaced Repetition
         System""")

with st.sidebar:
    option = st.selectbox(
       "What would you like to review?",
       ("Joins", "Group by", "windows Functions"),
       index=None,
       placeholder="Select contact method...",
    )

    st.write('You selected:', option)


st.header('enter your code')
query = st.text_area(label='write your sql command', key='user input')
if query:
    result = db.query(query).df()
    st.dataframe(result)


tab1, tab2 = st.tabs(["tables", "solution"])

with tab1:
    st.write("beverages")
    st.dataframe(beverages)
    st.write("foods")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution)

with tab2:
    st.write(answer)




