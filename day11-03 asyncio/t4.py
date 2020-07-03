# encoding = utf-8
__author__ = "mcabana.com"

 
"""
使用loop.creat_task() 或 asyncio.creat_task() 替代 future
"""


import asyncio


@asyncio.coroutine
def sleep():    # 本身是一个生成器函数, 通过asyncio.corotine转换成一个协程函数
    for i in range(3):
        print('~~~~~~~~~~~~')
        yield
    return 'res'


loop = asyncio.get_event_loop()     # 创建大循环

"""
方法二
使用loop.create_task 替代ensure_future, 可以直接获取result
"""
task = loop.create_task(sleep())    # 也是将协程对象封装为 future对象

loop.run_until_complete(task)
print('task', task.result())


loop.close()