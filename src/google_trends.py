import pandas as pd

file_path = "data/brunello_cucinelli_trends.csv"

data = pd.read_csv(file_path)

data["Time"] = pd.to_datetime(data["Time"])

print(data.head())
print()
print(data.tail())
print()
print(data.info())
