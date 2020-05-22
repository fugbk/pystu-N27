# encoding = utf-8
__author__ = "Ang Li"


class A:
    def __init__(self, name):
        self.name = name

    # def __hash__(self):    # 用于hash的魔术方法
    #     return 123          # 定义实例的哈希值
    #
    # def __str__(self):  # 定义实例的表现
    #     return self.name
    # __repr__ = __str__
    #
    # def __eq__(self, other):    # 两个实例相等 a == b ==> a.__eq__(b)
    #     return self.name == other.name


a = A('Tom')
b = A('Tom')


print(hash(a), hash(b))