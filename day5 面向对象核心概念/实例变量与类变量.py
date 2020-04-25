# encoding = utf-8
__author__ = "Ang Li"


class Person:
    age = 20

    def __init__(self, name):
        self.name = name

    def showage(self):
        print(self.name, 'is',self.age)


tom = Person('Tom')

print(Person.age)       # 类变量 - 20
tom.showage()       # 实例变量未定义时，会使用类变量 - 20
print(tom.name, tom.age)    # - 20
print()

tom.age += 5    # 此时相当于 定义了一个 实例变量， tom.age = 25, Person.age = 20

print('tom', tom.age)       # 输出的是实例变量的值 - 25
print('Person', Person.age)     # 类变量没有更改还是 20

tom.showage()   # 调用的tom的age
print('-' * 30)


Person.age = 17     # 修改类变量为 17

jerry = Person('Jerry')     # 新实例一个对象
print(Person.age)       # 类变量已经是 17
print(jerry.name, 'is', jerry.age)      # jerry.age 没有定义，使用的是Person.age - 17

print(tom.age)      # tom.age 依然是前面定义的 25
