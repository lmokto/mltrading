import pandas as pd
import matplotlib.pyplot as plt

# https://es.wikipedia.org/wiki/Media_m%C3%B3vil
# https://es.wikipedia.org/wiki/Bandas_de_Bollinger


def plot_data(df, title='Stock Prices'):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()


def get_data(symbol, dates):
    df1 = pd.DataFrame(index=dates)
    df_symbol = pd.read_csv('data/{name}.csv'.format(name=symbol), index_col='Date', parse_dates=True,
                        usecols=['Date', 'Adj Close'], na_values=['nan'])
    df_symbol = df_symbol.rename(columns={'Adj Close': symbol})
    df1 = df1.join(df_symbol, how='inner')
    return df1


def test_run():
    dates = pd.date_range('2018-01-01', '2018-01-26')
    df1 = get_data('SPY', dates)
    ax = df1['SPY'].plot(title='SPY rolling mean', label='SPY')
    rm_SPY = df1['SPY'].rolling(window=20, center=False).mean()
    rm_SPY.plot(label='Rolling mean', ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()

if __name__ == '__main__':
    test_run()
