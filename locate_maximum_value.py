import numpy as np


def get_max_index(a):
    # return the index of the maximum value in given 1D array.
    return a.argmax()


def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print('# 32-bit integer array')
    print(a)
    print(30*'-')
    print('Maximum value: {}'.format(a.max()))
    print('Index of max.: {}'.format(get_max_index(a)))


if __name__ == '__main__':
    test_run()
