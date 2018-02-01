import numpy as np


def test_run():
    print(30*'-')
    print('Print numpy empty 1D')
    print(np.empty(5))
    print(30*'-')
    print('Print numpy empty 3D')
    print(np.empty((5, 4, 3)))
    print('Array of 1s')
    print(np.ones((5, 4)))

if __name__ == '__main__':
    test_run()
