# encoding = utf-8
__author__ = "Ang Li"

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age       # 通过私有属性，隐藏了内部数据，同时提供相应的接口来访问修改属性 --- 封装

    @property       #将方法转换为 属性   getter
    def age(self):
        return self.__age * 10

    @age.setter     # 修改属性的值    setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        print('del ~~~~~~~~~~~~~~~~~')
        del self.__age

tom = Person('Tom')

# 获得age
print(tom.name, tom.age)
# 修改age
tom.age = 100
print(tom.name, tom.age)

# del tom.age
print(tom.name, tom.age)
print('-' * 30)

class Person2:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age


    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def del_age(self):
        del self.__age

    age = property(get_age, set_age, del_age)

tom = Person2('Tom')
print(tom.name, tom.age)
tom.age = 100
print(tom.name, tom.age)