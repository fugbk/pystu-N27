# encoding = utf-8
__author__ = "Ang Li"


def foo():  # 函数中出现 yield 即为一个生成器函数，生成器函数返回一个生成器对象
    yield 1
    yield 100
    for i in range(4):
        yield i + 100
    return 10

f = foo()
print(f)

print(1, next(f))  # 1
print(2, next(f))  # 100
for i in range(4):
    print(i+3, next(f))  # 100, 101, 102, 103

print('last', next(f))

