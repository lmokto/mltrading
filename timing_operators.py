import time


def test_run():
    print('Using time function')
    print(30*'-')
    t1 = time.time()
    print(30*'*')
    print(30 * '*')
    print(30 * '*')
    t2 = time.time()
    end_seconds = t2-t1
    print('The time token by print statment is : {0}'.format(end_seconds))


if __name__ == '__main__':
    test_run()
