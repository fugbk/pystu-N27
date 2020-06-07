# encoding = utf-8
__author__ = "mcabana.com"


import threading
import logging
import time


FORMAT = "%(asctime)s %(threadName)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

print('start ~~~~~~~~~')

lock = threading.Lock()
lock.acquire()


def worker():
    logging.info("in the worker")
    lock.acquire()
    logging.info('get lock')


t1 = threading.Thread(target=worker, name="worker")
t1.start()

time.sleep(3)

lock.release()