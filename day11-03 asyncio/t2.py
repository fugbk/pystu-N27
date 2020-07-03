# encoding = utf-8
__author__ = "mcabana.com"

# 事件循环的使用示例

import asyncio


@asyncio.coroutine
def sleep():    # 本身是一个生成器函数, 通过asyncio.corotine转换成一个协程函数
    for i in range(3):
        print('~~~~~~~~~~~~')
        yield


print(asyncio.iscoroutinefunction(sleep))   # 是不是一个协程函数？
print(asyncio.iscoroutine(sleep()))  # 是不是一个协程对象？

# 创建一个事件循环
loop = asyncio.get_event_loop()

# 将协程对象加入到这个事件大循环中
loop.run_until_complete(sleep())

# 停止事件循环
loop.close()

