import pandas as pd


# https://es.wikipedia.org/wiki/Media_m%C3%B3vil
# https://es.wikipedia.org/wiki/Bandas_de_Bollinger

def plot_data(df, title='Stock Prices'):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()


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
    print(subset_df1[['SPY']].mean())


if __name__ == '__main__':
    test_run()
