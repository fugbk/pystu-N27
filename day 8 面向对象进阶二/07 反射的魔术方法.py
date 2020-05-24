# encoding = utf-8
__author__ = "www.mcabana.com"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):    # 访问不存在的属性，会到这里，结果就是return值，就不会抛出异常了
        setattr(self, item, 100)  # 可以设置一个新的
        #return 100  # 也可以返回一个默认值, return返回的不会出现在 dict 中
        #return "{} missing".format(item)


p1 = Point(4, 5)

print(p1.x, p1.y, p1.z)
print(p1.__dict__)

