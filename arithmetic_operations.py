import numpy as np


def test_run():
    a = np.array([(2, 3, 4), (1, 1, 1)])
    b = np.array([(5, 3, 4), (1, 1, 1)])
    print('Original array B = {0}'.format(b))
    print('Original array A = {0}'.format(a))
    print(30 * '-')
    print('Multiply array A * 2 ')
    print(2 * a)
    print(30 * '-')
    print('Add the two arrays A + B')
    print(a + b)
    print(30 * '-')
    print('Multiply array A * B')
    print(a * b)
    print(30 * '-')
    print('Divide array A / B')
    print(a / b)


if __name__ == '__main__':
    test_run()
