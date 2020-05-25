# encoding = utf-8
__author__ = "www.mcabana.com"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('init ~~~~~~~~~~~~~~')

    # def __setattr__(self, key, value):
    #     print('setattr ~~~~~~~')
    #     #setattr(self, key, value)
    #     self.__dict__[key] = value  # 通过操作实例的 dict 进行属性定义，也要经过 __getattribute__()

    def __getattr__(self, item):
        print('getattr ~~~~~~~~')

    def __getattribute__(self, item):   # 所有通过实例访问的属性，都要先经过这里
        print('getattribute ~~~~~~~~~')
        #return object.__getattribute__(self, item)  # 在Point中找不到，就去它的父类中去找
        #return super().__getattribute__(item)   # 同上
        raise AttributeError


p1 = Point(4, 5)

print(p1.__dict__)
print(p1.x, p1.y)




