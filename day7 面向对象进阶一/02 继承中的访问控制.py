# encoding = utf-8
__author__ = "Ang Li"

# 牢记：类中的私有属性会被重命名为 _Class__name，它所在的类

class Animal:

    __a = 100
    __b = 7
    c = 20

    def __init__(self):
        self.__a += 1   # self._Animal = self._Animal__a + 1
        self.c = 25     # self.c = 25
        self.__d = 16   # self._Animal__d = 16

    def showa(self):
        print(self.__a)     # self._Animal__a, 101
        print(self.c)   # self.c, 1
        print(self.__class__.__a)
        print(self.__dict__)
        print(self.__class__.__dict__)

    def showb(self):
        print(self.__b)


class Cat(Animal):
    __a = 31    # _Cat__a = 31
    c = 1


c = Cat()   # 实例c初始化时，会执行父类的__init__， 此时会生成一个新的 c.c
c.showa()


