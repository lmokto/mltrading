import numpy as np


def test_run():
    a = np.random.rand(5, 4)
    print('Array {0}'.format(a))
    print(30*'-')
    print('Accessing a element position (3, 2)')
    print(a[3, 2])
    print(30*'-')
    print('Element in defined range [0, 1:3]')
    print(a[0, 1:3])
    print(30*'-')
    print('Top-left corner')
    print(a[0:2, 0:2])
    print(30*'-')
    print('Slicing n:m:t specifies a range that starts at, n and stop before m in array')
    print('will select columns, 0, 2 for every row')
    print(a[:, 0:3:2])

if __name__ == '__main__':
    test_run()
