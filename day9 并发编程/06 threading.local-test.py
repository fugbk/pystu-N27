# encoding = utf-8
__author__ = "mcabana.com"


import threading


class B: pass


b = B()
a = threading.local()
print(a)

a.x = 100


def worker():
    a.y = 10
    b.c = 100
    print('in the worker', hasattr(a, 'x'), hasattr(a, 'y'))    # False, True
    print('in the worker', threading.current_thread().name, a.y)


t1 = threading.Thread(target=worker, name='worker1')

t1.start()
t1.join()

print('*', a.x)     # 100
print('*', hasattr(a, 'y'))     # False
print('*', hasattr(b, 'c'))
