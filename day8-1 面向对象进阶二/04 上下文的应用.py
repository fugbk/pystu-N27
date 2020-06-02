# encoding = utf-8
__author__ = "www.mcabana.com"


# 计算add函数的执行时间

import time
import datetime


def add(x, y):
    time.sleep(1)
    return x + y


class Timeit:
    """
    计算函数的执行时间
    """
    def __init__(self, fn):     # fn是传入的函数，只是一个“标识符”
        self._fn = fn

    def __enter__(self):
        self.start = datetime.datetime.now()    # 记录开始时间
        return self._fn     # 返回传入的函数，

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()   # 结束时间 - 开始时间
        print('function <{}> took {}s'.format(self._fn.__name__, delta))


with Timeit(add) as t:
    print(t is add)     # 因为 Timeit.__enter__() 返回的是传入的add， 所以t is add
    t(3, 4)     # ==> add(3, 4)




