import pandas as pd
import math
import sys


def get_csv():
    return sys.argv[1]


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
    return math.floor(df['gross income'].sum() * 100) / 100


def calc_total_rev(df):
    return math.floor(df['Total'].sum() * 100) / 100


def calc_min(df, column_name):
    return df[column_name].min()


def calc_max(df, column_name):
    return df[column_name].max()


def get_column_values(df, column_name):
    return df[column_name].unique()


def get_column_rows(df, column_index, column):
    return df.loc[df[column_index] == column]


def get_gender_ratio(amount_f, amount_m, amount_rows):
    ratio_f = amount_f / amount_rows
    ratio_m = amount_m / amount_rows
    return ratio_f, ratio_m


# A majority of what is in main right now is for testing/brainstorming.
def main():
    csv_name = get_csv()
    df = pd_read_csv(csv_name)

    unique_cities = get_column_values(df, 'City')
    print(unique_cities)
    city = get_column_rows(df, 'City', unique_cities[2])
    city_min = calc_min(city, 'Total')
    print(city_min)


if __name__ == "__main__":
    main()
