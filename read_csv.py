import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/HCP.csv")
    print(30 * '--')
    print('First 5 rows.')
    print(df.head())
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html
    print(30 * '--')
    print('Last 5 rows.')
    print(df.tail())
    print(30 * '--')
    print('Rows between index 10 and 20.')
    print(df[10:20])
    # TODO: Print last 5 rows of the data frame


if __name__ == "__main__":
    test_run()
