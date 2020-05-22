# encoding = utf-8
__author__ = "Ang Li"

class Animal:
    def shout(self):
        print('Animal shouts')

class Cat(Animal):
    def shout(self):
        super().shout()     # 调用父类的shout方法  Animal shouts
        super(self.__class__, self).shout()     # 同上
        print('miao')

c = Cat()

c.shout()
