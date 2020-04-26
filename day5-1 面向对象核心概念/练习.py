# encoding = utf-8
__author__ = "Ang Li"

class Person:
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

tom = Person('Tom') # 实例化、初始化
jerry = Person('Jerry', 20)
Person.age = 30

print(1, Person.age, tom.age, jerry.age) # 输出什么结果 30 18 20

print(2, Person.height, tom.height, jerry.height) # 输出什么结果 170 170 170

jerry.height = 175
print(3, Person.height, tom.height, jerry.height) # 输出什么结果 170 170 175

tom.height += 10
print(4, Person.height, tom.height, jerry.height) # 输出什么结果 170 180 175

Person.height += 15
print(5, Person.height, tom.height, jerry.height) # 输出什么结果 185 180 175

Person.weight = 70
print(6, Person.weight, tom.weight, jerry.weight) # 输出什么结果 70 70 70

print(7, tom.__dict__['height']) # 可以吗 180
print(8, tom.__dict__['weight']) # 可以吗 error