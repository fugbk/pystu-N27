# encoding = utf-8
__author__ = "Ang Li"


import threading
import time


def worker(timeout):
    print('in the', threading.current_thread().name, threading.current_thread().ident)
    time.sleep(timeout)
    print('{}: finished ~~~~~~~~~~~~~~~~'.format(threading.current_thread().name))


t1 = threading.Thread(target=worker, name='worker1', args=(10, ))   # 不设置daemon，则使用 主线程的daemon，是False
t2 = threading.Thread(target=worker, name='worker2', daemon=True, args=(10, ))
t3 = threading.Thread(target=worker, name='worker3', daemon=False, args=(5, ))

t1.setDaemon(True)      # 可通过setDaemon()方法设置daemon值，必须在线程执行前设置。

t1.start()
t2.start()
t3.start()
print('*' * 30)
