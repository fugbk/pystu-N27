# encoding = utf-8
__author__ = "mcabana.com"


"""
多个task交替执行, 并获取每个task的执行结果
"""

import asyncio


@asyncio.coroutine
def a():
    for i in range(3):
        print('a.{}'.format(i))
        yield   # 转换成一个生成器函数
    return 'a 1000'

@asyncio.coroutine
def b():
    for i in 'abc':
        print('b.{}'.format(i))
        yield   # 转换成一个生成器函数
    return 'b 1000'


# 获取future result的回调函数
def res(ts):
    print(ts.result())

loop = asyncio.get_event_loop()

task1 = loop.create_task(a())   # task1
task2 = loop.create_task(b())   # task2

task1.add_done_callback(res)    # 添加回调函数
task2.add_done_callback(res)

# 使用asyncio.wait() 将多个task放入
loop.run_until_complete(asyncio.wait((task1, task2)))


loop.close()

