# encoding = utf-8
__author__ = "Ang Li"


class A:pass

a = A()
# print(bool(A))      # 缺省类的布尔值是True
# print(bool(a))      # 缺省实例的布尔值是True


# 更改实例的布尔值
class B:
    # def __bool__(self):     # 布尔魔术方法，对实例生效
    #     return False    # bool(B()) = False

    def __len__(self):  # 没有布尔方法，但是有len方法，则以 len方法的返回结果为准
        return 0        # 返回 0 布尔值是False， 返回非0 布尔值是True。len的返回值必须>=0

b = B()
print(bool(B))
print(bool(b))
print(len(b))

