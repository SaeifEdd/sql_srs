import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
# --------------------------------------------------------------------
#                  Exercises list
#   ------------------------------------------------------------------
data = {
    "theme": ["cross join", "cross join"],
    "exercise name": ["beverages_and_food", "sizes_and_trademarks"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
    "last_reviewed": ["1980-01-01", "1970-01-01"],
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

size_csv = """
size
XS
M
L
XL
"""

size = pd.read_csv(io.StringIO(size_csv))
con.execute("CREATE OR REPLACE TABLE sizes AS SELECT * FROM size")

trademark_csv = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""

trademark = pd.read_csv(io.StringIO(trademark_csv))
con.execute("CREATE OR REPLACE TABLE trademarks AS SELECT * FROM trademark")
