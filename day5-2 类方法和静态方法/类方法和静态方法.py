# encoding = utf-8
__author__ = "Ang Li"

class Person:

    # @classmethod
    # def cls_method(cls):
    #     print(cls, type(cls), id(cls))

    @staticmethod
    def static_method(a, b):
        print('static', a, b)



print(Person.static_method)
print(Person().static_method)

Person.static_method(100, 200)
Person().static_method(100, 200)
print(*Person.__dict__.items(), sep='\n')

# print(Person.cls_method)    # 类直接调用方法，也有了绑定
# print(Person().cls_method)      # 使用类实例调用方法，其实绑定的还是 类本身
# print()
# Person.cls_method()     # 类执行类的方法，注入的self 是 类本身
# Person().cls_method()   # 此时实例执行类的方法注入的self 是 类本身



# 属性方法
class Dog(object):
    name = "Alex" # 定义类变量
    def __init__(self,name):55
        self.name = name # 定义实例变量

    @property
    def sleep(self):
        print("Dog %s is sleeping..." %(self.name))


d = Dog("Tom")
d.sleep     # 把一个实例方法，当做一个实例属性来访问。