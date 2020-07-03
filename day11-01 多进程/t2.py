# encoding = utf-8
__author__ = "mcabana.com"

 
import multiprocessing
import datetime


def calc(i):
    sum = 0
    for _ in range(1000000000): # 10亿
        sum += 1

    print('sum is {}'.format(sum))
    #return i, sum


if __name__ == '__main__':
    start = datetime.datetime.now() # 注意一定要有这一句
    ps = []
    for i in range(4):
        p = multiprocessing.Process(target=calc, args=(i,), name='calc-{}'.format(i))
        ps.append(p)
        p.start()

    for p in ps: p.join()

    # print(p.name, p.exitcode)

    delta = (datetime.datetime.now() - start).total_seconds()

    print(delta)

    # for p in ps:
    #     print(p.name, p.exitcode)

    print('===end====')