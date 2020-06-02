# encoding = utf-8
__author__ = "Ang Li"


import logging

l1 = logging.Logger('t1')

l3 = logging.getLogger('t4')    # 推荐使用,如果不指定name，返回的是RootLogger

print([l3, type(l3), l3.name, l3.level, l3.parent, l3.parent.name])     # 父类是root

# 消息输出
l3.info('test  l3 info message')
l3.warning('test l3 warning')
print(l3.getEffectiveLevel(), l3.level)     # 打印有效级别，级别

print('*' * 30)

l3.level = 20   # 设置级别，有效级别
print(l3.getEffectiveLevel(), l3.level)     # 打印有效级别，级别

# 其他方法设置级别
l1.setLevel(10)
print(l1.getEffectiveLevel(), l1.level)

l1.setLevel(logging.DEBUG)    # 推荐 使用
print(l1.getEffectiveLevel(), l1.level)

