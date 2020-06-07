# encoding = utf-8
__author__ = "mcabana.com"


# 订单要求生产1000个杯子，组织10个工人生产。请忽略老板，关注工人生成杯子

import logging
import threading
import time


FORMAT = "%(asctime)s %(threadName)s %(thread)d: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

cups = []
lock = threading.Lock()


def worker(count=1000):
    logging.info("in the worker")
    while True:
        flag = lock.acquire(False)  # 适用非阻塞锁，需要去判断是否拿到锁
        if flag:    # True：拿到，False：没有拿到
            if len(cups) >= count:
                lock.release()
                break

            cups.append(1)
            time.sleep(0.0001)
            lock.release()
        else:
            logging.info('try again')

    logging.info('finishd cups {}'.format(len(cups)))


for i in range(10):
    t1 = threading.Thread(target=worker, name='worker-{}'.format(i))
    t1.start()

