import numpy as np


def test_run():
    a = np.random.rand(5, 4)
    print('Array {0}'.format(a))
    print('Assigning a value to a particular location')
    a[0, 0] = 1
    print('Modified (replaced one element) {0}'.format(a))


if __name__ == '__main__':
    test_run()
