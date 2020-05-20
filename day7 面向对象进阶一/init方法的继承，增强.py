# encoding = utf-8
__author__ = "Ang Li"



class A:
    def __init__(self, c, d=10):
        self.c = c
        self.__d = d


class B(A):
    def __init__(self, a, b):
        super().__init__(7, 0)  # 同时调用父类的 __init__
        #A.__init__(self, 7, 0)     # 同super()

        self.a = a
        self.b = b

    def showvals(self):
        print(self.a, self.b)
        print(self.c)   # c 是普通属性，b 可以直接继承 A的
        print(self.__dict__)
        print(self._A__d)   # __d 是在A中定义的，只能使用_A__d


b = B(5, 1)
b.showvals()