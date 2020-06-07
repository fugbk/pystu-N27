# encoding = utf-8
__author__ = "mcabana.com"


import threading
import time


def worker(timeout):
    print('in the', threading.current_thread().name, threading.current_thread().ident)
    time.sleep(timeout)
    print('finished ~~~~~~~~~~~~~~')


t1 = threading.Thread(target=worker, name='worker1', daemon=True, args=(10,))

t1.start()
t1.join()   # 使用join方法，将t1线程加入到主线程中去,进行阻塞。哪个线程启动它，就加入到哪里去

print('*' * 30)