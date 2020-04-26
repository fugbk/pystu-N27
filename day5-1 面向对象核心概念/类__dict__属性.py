# encoding = utf-8
__author__ = "Ang Li"

class Person:
    x = 100
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def showage(self):
        return "{} is {}".format(self.name, self.age)

print(*Person.__dict__.items(), sep='\n')   # 类字典 __dict__
print('-' * 30)

tom = Person('Tom', 20)
print(*tom.__dict__.items(), sep='\n')      # 实例字典


