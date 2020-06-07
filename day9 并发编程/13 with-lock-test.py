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
        with lock as b:     # 适用阻塞锁，lock 的__enter__（） 会上锁，退出时__exit__() 释放锁
            if len(cups) >= count:
                break

            cups.append(1)
            time.sleep(0.0001)

    logging.info('finishd cups {}'.format(len(cups)))


for i in range(10):
    t1 = threading.Thread(target=worker, name='worker-{}'.format(i))
    t1.start()

