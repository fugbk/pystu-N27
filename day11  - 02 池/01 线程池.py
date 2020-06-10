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

    for _ in range(1000000000):
        sums += 1

    return threading.current_thread(), sums     # 执行函数的返回值就是 future.result()

f = executor.submit(calc)   # 如果线程池没有达到最大数，则启动线程，如果满了就等待
                            # 用线程池启动， 返回一个future给f， f中包含了启动的线程的信息
                            # 线程池创建线程，其实就是调用的threading.Thread()， daemon=True

print(type(f), f)   # running状态

while True:     # 因为没有阻塞主线程，所以要手动判断线程是否执行完了，多个线程要逐个判断
    time.sleep(1)
    if f.done():    # 因为没有阻塞主线程，所以要手动判断f是否执行完了
        print(f.result())   # 如果执行完，打印结果。如果没有执行完就打印，会阻塞在这
        break

# 此时f状态为finished

# 关闭线程池执行器
executor.shutdown()     # 关闭 会等待所有线程执行完

deltime = (datetime.datetime.now() - start).total_seconds()
print('end ~~~~~~~~~~~~~~~~~~~~~~', deltime)