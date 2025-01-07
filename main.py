import pandas as pd

# Will make this dynamic, hard-coding a practice dataset on my machine for right now.
CSV_NAME = "~/supermarket_sales.csv"

def pd_read_csv():
    df = pd.read_csv(CSV_NAME)
    return df

def calc_total_profit(df):
    return df['gross income'].sum()

def calc_total_rev(df):
    return df['Total'].sum()

def get_unique_branches(df):
    return df['Branch'].unique()

def divide_branch(df, branch):
    return df.loc[df['Branch'] == branch]

# A majority of what is in main right now is for testing/brainstorming.
def main():
    df = pd_read_csv()
    total_profit = calc_total_profit(df)
    total_rev = calc_total_rev(df)
    unique_branches = get_unique_branches(df)
    print(unique_branches)
    branch = divide_branch(df, unique_branches[0])
    branch_trev = calc_total_rev(branch)
    print(branch_trev)
    print(total_rev)

    

if __name__ == "__main__":
    main()

