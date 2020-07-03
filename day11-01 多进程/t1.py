# encoding = utf-8
__author__ = "mcabana.com"

import multiprocessing
import logging
import datetime

FORMAT = "%(asctime)s %(processName)s %(process)d: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc():
    sums = 0
    for _ in range(1000000000):
        sums += 1

    logging.info('sum is {}'.format(sums))
    # print(multiprocessing.current_process())    # 当前进程


if __name__ == '__main__':

    start = datetime.datetime.now()
    ps = []

    for _ in range(4):
        p = multiprocessing.Process(target=calc, name='calc-{}'.format(_))
        p.start()
        ps.append(p)

    print('active_children', multiprocessing.active_children())     # 所有活着的进程

    for p in ps:
        p.join()

    deltime = (datetime.datetime.now() - start).total_seconds()
    print(deltime)