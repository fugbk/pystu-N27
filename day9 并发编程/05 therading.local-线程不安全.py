# encoding = utf-8
__author__ = "mcabana.com"


import threading


class A:
    def __init__(self):
        self.x = 100


a = A()
y = 10
print(a.x)


def worker():
    global y

    for c in range(1000000):
        a.x += 1
    print('in the', threading.current_thread().name, a.x)
    # a.x += 1
    # print(a.x)  # 在线程内，可以修改类属性


for i in range(5):
    threading.Thread(target=worker).start()

print('*' * 30, a.x)
