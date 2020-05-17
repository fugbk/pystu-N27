# encoding = utf-8
__author__ = "Ang Li"
import sys


# 定义一个类, 这个类继承至 Exception异常类
class MyException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

try:
    print('before...')
    1 / 2
    print('after...')
except KeyError:
    print('key error')
except ZeroDivisionError as e:  # 将捕获的异常赋给了 e 这个标识符
    print('zero', e)
except Exception as e:  # 因为 MyException 继承至 Exception， 所以用 Exception 可以捕获到
    print('exc', e, type(e))    # 捕获到的异常，本质是一个类对象， 这个对象又赋给了 e
else:
    print('else~~~~~~~~~~')
finally:
    print('fin~~~~~~~~~')

print('-' * 30)


