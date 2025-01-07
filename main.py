import pandas as pd

# Will make this dynamic, hard-coding a practice dataset on my machine for right now.
CSV_NAME = "~/supermarket_sales.csv"

def pd_read_csv():
    df = pd.read_csv(CSV_NAME)
    return df

def main():
    df = pd_read_csv()
    print(df)

if __name__ == "__main__":
    main()

