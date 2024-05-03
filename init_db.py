import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
# --------------------------------------------------------------------
#                  Exercises list
#   ------------------------------------------------------------------
data = {
    "theme": ["cross join", "window_functions"],
    "exercise name": ["beverages_and_food", "simple_window"],
    "tables": [["beverages", "food_items"], "simple_window"],
    "last_reviewed": ["1970-01-01", "1970-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")
#   ------------------------------------------------------------------
#                   CROSS JOIN EXERCISES
#   ------------------------------------------------------------------
CSV = """
beverage,price
orange juice, 2.5
expresso, 2
Tea, 3
citronade, 3.5
"""
beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item,food_prices
cookie juice, 2.5
chocolatine, 5
muffin, 4
cheese cake, 7
"""

food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")
