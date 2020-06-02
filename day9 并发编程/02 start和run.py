# encoding = utf-8
__author__ = "Ang Li"


import threading


def worker():
    print('in worker ~~~~~~~~')
    print(threading.get_ident(), threading.current_thread(), threading.main_thread())


t = threading.Thread(target=worker, name='worker')

# t.start()
t.run()