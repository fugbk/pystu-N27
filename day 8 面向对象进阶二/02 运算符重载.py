# encoding = utf-8
__author__ = "Ang Li"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):    # 实现等于比较
        return self.age == other.age    # 比较age

    def __lt__(self, other):    # 实现小于比较
        return self.age < other.age

    def __le__(self, other):    # 实现小于等于比较
        return self.age <= other.age

    def __str__(self):      # 定义实例的表示
        return "<Person: {},{}>".format(self.name, self.age)
    __repr__ = __str__

tom = Person('tom', 18)
jerry = Person('jerry', 21)

print(tom == jerry)     # 用的 __eq__
print(tom < jerry)      # 用的 __lt__
print(tom <= jerry)     # 用的 __le__
print(tom > jerry)      # 返过来也能做大于比较
print(sorted([jerry, tom]))     # 排序列表


# 就算没有这些魔术方法，直接比较也是可以的
print(tom.age < jerry.age)
print(tom.age - jerry.age)

print(sorted([tom.age, jerry.age]))