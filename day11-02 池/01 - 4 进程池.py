# encoding = utf-8
__author__ = "mcabana.com"


import multiprocessing
import datetime
import logging
from concurrent.futures import ProcessPoolExecutor


start = datetime.datetime.now()
FORMAT = "%(asctime)s %(processName)s %(process)d %(threadName)s %(thread)d: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc():
    sums = 0
    logging.info('in the worker')
    for _ in range(1000000000):
        sums += 1
    return "{}, {}".format(multiprocessing.current_process(), sums)     # 执行函数的返回值就是 future.result()


if __name__ == '__main__':      # 进程要写在 main 中
    # 先定义一个进程池执行器
    executor = ProcessPoolExecutor(4)     # 此进程池中最多创建 4 个进程同步执行
                                            # 如果是None 则是 os.cpu_count() * 5 或者 1 * 5
    with executor:
        fs = []
        # 多个启动进程
        for i in range(4):
            f = executor.submit(calc)
            fs.append(f)    # 加入进程列表


    # 获取多个进程的执行结果
    for f in fs:
        print(f.result())


    # 关闭进程池执行器
    executor.shutdown()     # 关闭 会等待所有进程程执行完


    delta = (datetime.datetime.now() - start).total_seconds()
    print('end ~~~~~~~~~~~~~~~~~~~~~~', delta)