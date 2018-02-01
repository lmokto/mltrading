import numpy as np


def test_run():
    a = np.random.rand(5, 4)
    print('Array {0}'.format(a))
    print('Accessing using list of indices')
    indices = np.array([1, 2, 3, 4])
    print(a[indices])


if __name__ == '__main__':
    test_run()
