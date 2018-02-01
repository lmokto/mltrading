import pandas as pd


def get_max_column(symbol, column):
    """
    :param symbol: 
    :param column: 
    :return: 
    """
    df = pd.read_csv('data/{name}.csv'.format(name=symbol))
    return df[column].max()


def test_run():
    column = 'Close'
    symbol = 'HCP'
    print(30 * '--')
    print('Max column {clm_name} in data/{sym_name}.csv.'.format(clm_name=column, sym_name=symbol))
    print(get_max_column(symbol, column))


if __name__ == '__main__':
    test_run()
