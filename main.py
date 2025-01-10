import pandas as pd
import math
import sys


def get_csv():
    return sys.argv[1]


def pd_read_csv(csv_name):
    if not csv_name.endswith('.csv'):
        print("Error: Not a CSV file.")
        sys.exit()
    else:
        try:
            df = pd.read_csv(csv_name)
        except FileNotFoundError:
            print("Error: File not found/does not exist.")
            sys.exit()
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


def get_row_amount(df):
    return df.shape[0]


def get_column_values(df, column_name):
    return df[column_name].unique()


def get_column_rows(df, column_index, column):
    return df.loc[df[column_index] == column]


def get_gender_ratio(amount_f, amount_m, amount_rows):
    ratio_f = (amount_f / amount_rows) * 100
    ratio_m = (amount_m / amount_rows) * 100
    return ratio_f, ratio_m


# A majority of what is in main right now is for testing/brainstorming.
def main():
    csv_name = get_csv()
    df = pd_read_csv(csv_name)

    print(get_row_amount(df))

    unique_cities = get_column_values(df, 'City')
    print(unique_cities)
    city = get_column_rows(df, 'City', unique_cities[2])
    city_min = calc_min(city, 'Total')
    print(city_min)
    print()
    amount_rows = get_row_amount(df)
    unique_genders = get_column_values(df, 'Gender')
    print(unique_genders)
    females = get_column_rows(df, 'Gender', unique_genders[0])
    print(females)
    males = get_column_rows(df, 'Gender', unique_genders[1])
    print(males)
    print(get_row_amount(females))
    print(get_row_amount(males))
    print(get_gender_ratio(get_row_amount(females), get_row_amount(males), get_row_amount(df)))
    print(df.min())
    print(df.max())


if __name__ == "__main__":
    main()
