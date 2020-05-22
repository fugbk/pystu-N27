# encoding = utf-8
__author__ = "Ang Li"


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):  # __str__ 和 __repr__ 用于定义实例的显示方式
        return "<A: x={}, y={}>".format(self.x, self.y)

    __repr__ = __str__  # 常用写法，因为在不同的调用中 __repr__和__str__的优先级不同

    def __bytes__(self):    # 返回bytes
        #return "<A: x={}, y={}>".format(self.x, self.y).encode()
        #return str(self).encode()
        return str(self.__class__.__dict__).encode()

a = A(4, 5)

print(a)    # 使用repr后实例不在以传统方式显示，显示自定义结果


print(bytes(a))     # 需要专门调用
