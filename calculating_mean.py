import numpy as np


def test_run():
    a = np.array([(20, 25, 10), (0, 1, 2)])
    print('Array a {0}'.format(a))
    print(30*'-')
    print('Calculating MEAN')
    mean = a.mean()
    print(mean)
    print(30*'-')
    print('Masking')
    a[a<mean] = mean
    print(a)
    

if __name__ == '__main__':
    test_run()