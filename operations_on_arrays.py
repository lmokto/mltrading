import numpy as np


def test_run():
    np.random.seed(693) # seed the random number generator
    a = np.random.randint(0, 10, size=(2, 5)) # 5x4 random integers in [0, 10]
    print('Array: {0}'.format(a))
    print(30*'-')
    print('Statistics: MIN, MAX, MEAN (across rows, cols, and overall')
    print('Minimum of each column: {}'.format(a.min(axis=0)))
    print('Minimum of each row: {}'.format(a.min(axis=1)))
    print('Mean of all elements {}'.format(a.mean()))

if __name__ == '__main__':
    test_run()
