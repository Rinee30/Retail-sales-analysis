import sqlite3
import pandas as pd

conn = sqlite3.connect("retail_sales.db")

# Load into pandas
df = pd.read_sql("SELECT * FROM sales", conn)

# Handle missing values
df = df.dropna()

# Create new calculated fields
df["TotalSaleValue"] = df["NumberOfItemsPurchased"] * df["CostPerItem"]

# Extract month & year
df["TransactionTime"] = pd.to_datetime(df["TransactionTime"])
df["Month"] = df["TransactionTime"].dt.month
df["Year"] = df["TransactionTime"].dt.year

# Save cleaned data
df.to_sql("sales_cleaned", conn, if_exists="replace", index=False)

print("✅ Data cleaned and stored")
conn.close()
