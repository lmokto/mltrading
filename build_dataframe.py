import pandas as pd


def test_run():
    # Define data range yy-mm-dd
    start_date = '2018-01-01'
    end_date = '2018-01-26'
    dates = pd.date_range(start_date, end_date)
    #print(30 * '-')
    #print('Date Range {start} - {end}'.format(start=start_date, end=end_date))
    #print(dates)
    #print(30 * '-')
    #print('Data Frame with index dates')
    # Create a empty dataframe.
    df1 = pd.DataFrame(index=dates)
    #print(df1)
    #print(30 * '-')
    #print('Join the two dataframes.')
    # Read HCP.csv data into temporary dataframe
    dfSPY = pd.read_csv('data/SPY.csv', index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])
    # Rename column 'Adj Close' to 'SPY'
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
    #print(dfSPY)
    print(30 * '-')
    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY, how='inner')
    # Drop nan values.
    # df1.dropna()
    symbols = ['GOOG', 'IBM', 'GLD']
    # print('Join Symbols {names}'.format(names=str(symbols)))
    for symbol in symbols:
        df_temp = pd.read_csv('data/{name}.csv'.format(name=symbol), index_col='Date', parse_dates=True,
                              usecols=['Date', 'Adj Close'],  na_values=['nan'])
        new_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(new_temp)
        #print(new_temp)

    # Slicing dataframes

    # select range for date
    subset_df1 = df1['2018-01-19':'2018-01-24']
    # select column

    print(subset_df1[['GOOG', 'GLD']])


if __name__ == '__main__':
    test_run()
