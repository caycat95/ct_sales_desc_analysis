import pandas as pd

# Will make this dynamic, hard-coding a practice dataset on my machine for right now.
CSV_NAME = "~/supermarket_sales.csv"

df = pd.read_csv(CSV_NAME)
print(df)