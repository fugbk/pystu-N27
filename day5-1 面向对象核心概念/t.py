# encoding = utf-8
__author__ = "Ang Li"


class Person:
    age = 100

    def __init__(self, name):
        self.name = name

tom = Person('Tom')

print(tom.age)  # tom 中没有定义age，访问的是类的，如果类中没有会接着访问上层的父类的
print(*tom.__dict__.items())    # 但是这种访问，是直接访问，tom实例并不会 并不会新增一个age属性。

