# encoding = utf-8
__author__ = "Ang Li"


class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def shout(self):
        print('{} shouts'.format(self.__class__.__name__))


class Dog(Animal): pass
class Cat(Animal): pass

d = Dog('XiaoHei')
c = Cat('MiMi')

d.shout()
c.shout()

print(d.name, c.name)

print(Animal.mro(), Animal.__mro__)
print(Dog.mro(), Dog.__mro__)
print(Cat.mro(), Cat.__mro__)
print('----------------------')

print(Animal.__bases__, Animal.__base__)   # __bases__ 显示所有继承的基类，元组显示
print(Cat.__bases__, Cat.__base__)   # __base__ 只显示继承的所有基类的第一个，

print('*' * 30)

print(Animal.__subclasses__())





























