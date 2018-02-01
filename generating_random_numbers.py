import numpy as np


def test_run():
    print(30 * '-')
    print('Generating random numbers')
    print(np.random.rand(4, 5))
    print(30 * '-')
    print('Generating random numbers, using number from Gaussian distribution')
    print(np.random.normal(size=(2, 3)))
    print(30 * '-')
    print('Generating random numbers, using tpye int number 1D')
    print(np.random.randint(0, 10, size=5))
    print(30 * '-')
    print('Generating random numbers, using tpye int number 2D')
    print(np.random.randint(0, 10, size=(5, 2)))

if __name__ == '__main__':
    test_run()
