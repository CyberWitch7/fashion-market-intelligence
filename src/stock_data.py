import yfinance as yf
import pandas as pd

ticker = "BC.MI"

stock = yf.Ticker(ticker)

data = stock.history(period="5y")

#only closing price
monthly_stock = data["Close"].resample("ME").last()

#calculate monthly percentage return
monthly_return = monthly_stock.pct_change()*100

#create a new dataframe
monthly_data = pd.DataFrame({
    "Stock_Close": monthly_stock,
    "Monthly_Return": monthly_return
})


print(monthly_data.head())
print(monthly_data.tail())