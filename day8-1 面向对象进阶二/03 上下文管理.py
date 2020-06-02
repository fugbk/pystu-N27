# encoding = utf-8
__author__ = "mcabana.com"


class A:
    def __init__(self):
        print('init ~~~~~~~~')

    def __enter__(self):    # 资源申请
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 资源释放
        print('exit ~~~~~~~~~')


a = A()
with a as f:    # f = a.__enter__() , f 就是 __enter__ 的返回值
    print(a)
    print(f)
    print(a is f)

