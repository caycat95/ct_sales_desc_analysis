import pandas as pd

# Will make this dynamic, for now hard-coded dataset.
CSV_NAME = "~/supermarket_sales.csv"


def pd_read_csv(csv_name):
    if not csv_name.endswith('.csv'):
        print("Error: Not a CSV file.")
        raise ValueError
    else:
        try:
            df = pd.read_csv(csv_name)
        except FileNotFoundError:
            print("Error: File not found/does not exist.")
            raise
        else:
            return df


def calc_total_profit(df):
    return df['gross income'].sum()


def calc_total_rev(df):
    return df['Total'].sum()


def calc_min(df, column_name):
    return df[column_name].min()


def calc_max(df, column_name):
    return df[column_name].max()


def get_column_values(df, column_name):
    return df[column_name].unique()


def get_column_rows(df, column_index, column):
    return df.loc[df[column_index] == column]


# A majority of what is in main right now is for testing/brainstorming.
def main():
    df = pd_read_csv(CSV_NAME)

    unique_cities = get_column_values(df, 'City')
    print(unique_cities)
    city = get_column_rows(df, 'City', unique_cities[2])
    city_min = calc_min(city, 'Total')
    print(city_min)


if __name__ == "__main__":
    main()
