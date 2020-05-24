# encoding = utf-8
__author__ = "wwww.mcabana.com"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(2, 5)

print(p1.__dict__)
print(p1.x, p1.y)
print(getattr(p1, 'x', 20))     # 打印p1.x， 如果不存在则p1.x = 30
print(getattr(p1, 'y', 50))     # 打印p1.y， 如果不存在则p1.y = 50

p1.x = 10
setattr(p1, 'x', 100)   # 同上

p1.y = 20
setattr(p1, 'y', 200)   # 同上

p1.z = 30
if not hasattr(p1, 'z'):    # 如果 p1.z 不存在，则 p1.z = 300
    setattr(p1, 'z', 300)

print(p1.__dict__)

print(p1.__dict__['x'])     # 通过 __dict__ 直接访问
p1.__dict__['x'] = 1
print(p1.x)
getattr(p1, '__dict__')['x'] = 100
print(p1.x)