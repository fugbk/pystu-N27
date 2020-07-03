# encoding = utf-8
__author__ = "mcabana.com"

"""
带未来值的事件循环
"""

import asyncio


@asyncio.coroutine
def sleep():    # 本身是一个生成器函数, 通过asyncio.corotine转换成一个协程函数
    for i in range(3):
        print('~~~~~~~~~~~~')
        yield
    return 'res'


future = asyncio.ensure_future(sleep())     # 将协程对象封装为future对象, 包含协程对象执行完后的返回值

print(1, future)    # 准备状态的future

loop = asyncio.get_event_loop()     # 创建大循环
loop.run_until_complete(future)     # 将future对象放入大循环中

print(2, future)    # 结束状态的future, 包含协程对象的返回值

print(future.result())  # 获取返回值

loop.close()