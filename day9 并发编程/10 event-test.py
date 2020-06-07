# encoding = utf-8
__author__ = "mcabana.com"


import threading
import logging


FORMAT = "%(asctime)s %(threadName)s: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
e = threading.Event()


def worker(e:threading.Event):
    cups = []
    while not e.wait(0.5):
        cups.append(1)
        logging.info("I'm working, make cups {}".format(len(cups)))

        if len(cups) >= 10:
            logging.info("make end")
            e.set()     # 制作完10个，flag=True


def boss(e:threading.Event):
    logging.info("I'm boss, waiting for you")
    e.wait()    # 等待flag信号，等10个杯子
    logging.info("Good job.")


t1 = threading.Thread(target=worker, name="worker", args=(e,))
t2 = threading.Thread(target=boss, name="boss", args=(e,))

t2.start()
t1.start()
