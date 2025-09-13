import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("retail_sales.db")

# Load cleaned data
df = pd.read_sql("SELECT * FROM sales_cleaned", conn)

# Example Analysis 1: Sales by Month
monthly_sales = df.groupby(["Year", "Month"])["TotalSaleValue"].sum().reset_index()
plt.plot(monthly_sales["Month"], monthly_sales["TotalSaleValue"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales Value")
plt.savefig("report/monthly_sales.png")
plt.close()

# Example Analysis 2: Top 10 Selling Items
top_items = df.groupby("ItemDescription")["TotalSaleValue"].sum().nlargest(10)
top_items.plot(kind="bar")
plt.title("Top 10 Best-Selling Items")
plt.savefig("report/top_items.png")
plt.close()

print("✅ Analysis & plots generated")
conn.close()
