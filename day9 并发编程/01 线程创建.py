# encoding = utf-8
__author__ = "Ang Li"


import threading


def add(x, y):
    print('add ~~~~~~~~~~{} + {} = {}'.format(x, y, x + y))
    print('in add {}'.format(threading.get_ident()))    # 在线程内，获取线程id


t1 = threading.Thread(target=add, name='add', args=(3,), kwargs={'y': 4})   # 创建一个线程对称

t1.start()
print(t1.ident, t1.name)    # 获取线程的id， 名字


