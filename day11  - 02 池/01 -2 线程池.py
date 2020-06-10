# encoding = utf-8
__author__ = "mcabana.com"


import threading
import datetime
import time
import logging
from concurrent.futures import ThreadPoolExecutor

start = datetime.datetime.now()

FORMAT = "%(asctime)s %(threadName)s %(thread)d: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


# 先定义一个线程池执行器
executor = ThreadPoolExecutor(4)    # 此线程池中最多创建 4 个线程异步执行
                                    # 如果是None 则是 os.cpu_count() * 5 或者 1 * 5

def calc():
    sums = 0
    logging.info('in the worker')

    for _ in range(100000000):
        sums += 1

    return threading.current_thread(), sums     # 执行函数的返回值就是 future.result()


fs = []
# 多个启动线程
for i in range(4):
    f = executor.submit(calc)
    fs.append(f)    # 加入线程列表


# 获取多个线程的状态
while True:
    time.sleep(1)
    flag = True
    for f in fs:
        if f.done():    # 判断每个线程是否done了
            logging.info(f.result())

        flag = f.done() and True    # 有一个线程没有done()，就会是False
    if flag:    # 如果是False，就继续等待
        break


# 关闭线程池执行器
# executor.shutdown()     # 关闭 会等待所有线程执行完


deltime = (datetime.datetime.now() - start).total_seconds()
print('end ~~~~~~~~~~~~~~~~~~~~~~', deltime)