import pandas as pd


def get_mean_value(symbol, column):
    """
    :param symbol: 
    :param column: 
    :return: 
    """
    df = pd.read_csv('data/{name}.csv'.format(name=symbol))
    return df[column].mean()


def test_run():
    column = 'Close'
    symbol = 'HCP'
    print(30 * '--')
    print('Mean column {clm_name} in data/{sym_name}.csv.'.format(clm_name=column, sym_name=symbol))
    print(get_mean_value(symbol, column))


if __name__ == '__main__':
    test_run()
