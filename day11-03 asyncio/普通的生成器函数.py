# encoding = utf-8
__author__ = "mcabana.com"


def a():
    for i in range(4):
        print('a.{}'.format(i))
        yield   # 转换成一个生成器函数

def b():
    for i in 'abcd':
        print('b.{}'.format(i))
        yield   # 转换成一个生成器函数


x = a()
y = b()
for i in range(4):      # 利用yield实现多线程交替执行
    next(x)
    next(y)


