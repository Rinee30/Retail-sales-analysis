import sqlite3
import pandas as pd

# Load dataset
df = pd.read_csv("data/retail_sales.csv")

# Connect to SQLite
conn = sqlite3.connect("retail_sales.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    TransactionID TEXT,
    TransactionTime TEXT,
    ItemCode TEXT,
    ItemDescription TEXT,
    NumberOfItemsPurchased INTEGER,
    CostPerItem REAL,
    Country TEXT
)
''')

# Insert data
df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Database setup complete with sales data")
conn.close()