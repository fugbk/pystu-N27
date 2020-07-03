# encoding = utf-8
__author__ = "mcabana.com"

"""
回调
"""

import asyncio


@asyncio.coroutine
def sleep():
    for i in range(3):
        print('~~~~~~~~~~~~')
        yield
    return 'res 1000'


def bro(ts):  # 回调函数必须要传入一个参数, 就是task
    print('bro {}'.format(ts.result()))     # 获取future


loop = asyncio.get_event_loop()
task = loop.create_task(sleep())

print(1, task)

# 向task中添加回调函数, task执行完, 立即执行回调函数
task.add_done_callback(bro)

print(2, task)

loop.run_until_complete(task)
print(3, task)


loop.close()
