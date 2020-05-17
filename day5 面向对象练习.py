# encoding = utf-8
__author__ = "Ang Li"

"""
1、随机整数生成类
可以先设定一批生成数字的个数，可设定指定生成的数值的范围。运行时还可以调整每批生成数字的个数
"""

import random

class Random:
    # 生成随机数
    def __init__(self, start_num, end_num):
        """
        初始化随机数范围
        :param start_num: 开始的位置
        :param end_num:  结束的位置
        """
        self.start_num = start_num
        self.end_num = end_num
        if self.start_num > self.end_num:
            self.start_num, self.end_num = self.end_num, self.start_num

    def randoms(self, value=5):
        """
        生成随机数
        :param value: 随机数的个数
        :return: 随机数列表
        """
        return random.choices(list(range(self.start_num, self.end_num)), k=value)


a1 = Random(100, 1)

x = a1.randoms(20)
y = a1.randoms(20)
print(x)
print(y)



"""
2、打印坐标
使用上题中的类，随机生成20个数字，两两配对形成二维坐标系的坐标，把这些坐标组织起来，并打印输出
"""
class Coordinate:
    # 生成坐标
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def create(self):
        return list(map(lambda m,n:(m,n), self.x, self.y))


b1 = Coordinate(x, y)
c1 = b1.create()

print(*c1, sep='\n')

