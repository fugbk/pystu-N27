# encoding = utf-8
__author__ = "Ang Li"

class Person:
    """class Person ，定义人类"""
    # __new__(self)  实例化一个对象

    def __init__(self, name, age=18):  # 初始化函数
        self.name = name
        self.age = age

    def showage(self):  # 方法，方法中可以调用 初始化中的属性
        return "{} is {}".format(self.name, self.age)
        # 这里调用的 self.name, self.age 就是前面初始化时绑定的这个实例的name属性和age属性。


tom = Person('Tom', 21)  # 实例化一个tom
jerry = Person('Jerry')  # 实例化一个jerry

print(tom.name, tom.age)  # 打印 tom的属性
print(jerry.name, jerry.age)

print(tom.showage())  # 调用tom的方法
print(jerry.showage())

print('-' * 30)

