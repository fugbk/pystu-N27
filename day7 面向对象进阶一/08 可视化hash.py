# encoding = utf-8
__author__ = "Ang Li"


class A:
    def __init__(self, name):
        self.name = name

    def __hash__(self):    # 用于hash的魔术方法
        return 123          # 定义实例的哈希值

    def __str__(self):  # 定义实例的表现
        return self.name
    __repr__ = __str__

    def __eq__(self, other):    # 两个实例相等 a == b ==> a.__eq__(b)
        return self.name == other.name


a = A('Tom')
b = A('Tom')

print(hash(a), hash(b))     # a b 的哈希值相同
print({a, b})   # 集合是否会去重
print(a == b)   # 此时 a == b
print(a is b)   # 两个实例is永远不成立

