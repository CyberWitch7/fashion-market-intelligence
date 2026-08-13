import pandas as pd

# -------------------------
# Load stock data
# -------------------------

stock = pd.read_csv("data/brunello_cucinelli_stock.csv")

stock["Date"] = pd.to_datetime(stock["Date"], utc=True)

stock["Month"] = stock["Date"].dt.to_period("M")

monthly_stock = (
    stock.groupby("Month")
    .agg(
        Stock_Close=("Close", "last")
    )
)

monthly_stock["Monthly_Return"] = (
    monthly_stock["Stock_Close"].pct_change() * 100
)


# -------------------------
# Load Google Trends data
# -------------------------

trends = pd.read_csv(
    "data/brunello_cucinelli_trends.csv",
    parse_dates=["Time"]
)

trends["Month"] = trends["Time"].dt.to_period("M")

trends = trends[["Month", "Brunello Cucinelli"]]

trends = trends.rename(
    columns={"Brunello Cucinelli": "Search_Interest"}
)

trends = trends.set_index("Month")


# -------------------------
# Merge both datasets
# -------------------------

merged = monthly_stock.join(trends, how="inner")

print(merged.head())
print()
print(merged.tail())
print()
print(merged.info())

merged.to_csv("data/brunello_cucinelli_monthly.csv")

print("\nMerged dataset saved successfully.")