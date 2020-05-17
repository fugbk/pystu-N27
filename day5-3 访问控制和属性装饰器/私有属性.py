# encoding = utf-8
__author__ = "Ang Li"

class Person:
    def __init__(self, name, age=19):
        self.name = name
        self.__age = age    # 属性前面加上__，意为私有属性，通过字面访问不到

    def __showage(self):    # 实例方法，也可以转为 私有方法
        return "{} is {}.".format(self.name, self.__age)        # 在实例内部可通过字面直接访问


tom = Person('Tom')

print(*Person.__dict__.items(), sep='\n')
print()
print(*tom.__dict__.items(), sep='\n')
# print(tom.name, tom._Person__age, tom._Person__showage())

print(tom.name, tom._Person__age, tom._Person__showage())   # 实例外部，在前面加上_Person 可以访问到私有属性和方法

# print(tom.name, tom.age, tom.showage())     # 通过字面意思访问不到
# print(tom.name, tom.__age, tom.__showage())   # 通过字面意思访问不到