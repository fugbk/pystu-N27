# encoding = utf-8
__author__ = "Ang Li"


class Person:
    age = 20

    def __init__(self, name):
        self.name = name

tom = Person('Tom')

tom.age += 5

print(Person.age, tom.age)
print(tom.__class__, type(tom.__class__))   # 实例的 __class__ 方法，返回的是实例的 类对象
print(tom.__class__.age)    # 访问类属性