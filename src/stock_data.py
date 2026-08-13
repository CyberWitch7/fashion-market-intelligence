import yfinance as yf

ticker = "BC.MI"

stock = yf.Ticker(ticker)

data = stock.history(period="5y")

print(data.head())
print(data.tail())

data.to_csv("data/brunello_cucinelli_stock.csv")

print("Data downloaded successfully")
print(f"Rows: {len(data)}")
print(data.head())