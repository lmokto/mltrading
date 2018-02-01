import pandas as pd


def test_run():
    start_date = '2018-01-01'
    end_date = '2018-01-26'
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)
    dfSPY = pd.read_csv('data/SPY.csv', index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])
    # Rename column 'Adj Close' to 'SPY'
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY, how='inner')
    symbols = ['GOOG', 'IBM', 'GLD', 'XOM']
    for symbol in symbols:
        df_temp = pd.read_csv('data/{name}.csv'.format(name=symbol), index_col='Date', parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        new_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(new_temp)
    # select range for date
    subset_df1 = df1['2018-01-19':'2018-01-24']
    print(30 * '-')
    print('Show the  array of the following symbols')
    print(30 * '-')
    print(subset_df1[['IBM', 'XOM', 'GOOG', 'GLD']])
    print(30 * '-')
    print('Show the MEAN of the following symbols')
    print(30 * '-')
    print(subset_df1[['IBM', 'XOM', 'GOOG', 'GLD']].mean())
    print(30 * '-')
    print('Show the MEDIAN of the following symbols')
    print(30 * '-')
    print(subset_df1[['IBM', 'XOM', 'GOOG', 'GLD']].median())
    print(30 * '-')
    print('Show the STD of the following symbols')
    print(30 * '-')
    print(subset_df1[['IBM', 'XOM', 'GOOG', 'GLD']].std())
    print(30 * '-')
    print('Show the SUM of the following symbols')
    print(30 * '-')
    print(subset_df1[['IBM', 'XOM', 'GOOG', 'GLD']].sum())
    print(30 * '-')
    print('Show the PROD of the following symbols')
    print(30 * '-')
    print(subset_df1[['IBM', 'XOM', 'GOOG', 'GLD']].prod())
    print(30 * '-')
    print('Show the MODE of the following symbols')
    print(30 * '-')
    print(subset_df1[['IBM', 'XOM', 'GOOG', 'GLD']].mode())


if __name__ == '__main__':
    test_run()
