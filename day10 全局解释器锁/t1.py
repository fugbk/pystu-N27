# encoding = utf-8
__author__ = "mcabana.com"


import threading
import logging
import datetime


FORMAT = "%(asctime)s %(threadName)s %(thread)d: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


start_time = datetime.datetime.now()

def calc():
    sum = 0
    for _ in range(1000000000):
        sum += 1

    # logging.info('sum is {}'.format(sum))



t1 = threading.Thread(target=calc, name='worker')

t1.start()
t1.join()


deltime = (datetime.datetime.now() - start_time).total_seconds()
logging.info('use {}s'.format(deltime))