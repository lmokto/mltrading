import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    symbol = 'HCP'
    df = pd.read_csv('data/{name}.csv'.format(name=symbol))
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show()


if __name__ == '__main__':
    test_run()