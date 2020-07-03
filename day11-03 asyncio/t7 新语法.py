# encoding = utf-8
__author__ = "mcabana.com"


import asyncio


@asyncio.coroutine
def wait():
    yield


# 获取future result的回调函数
def res(ts):
    print(ts.result())


"""
3.5之后的新语法, 代替@asyncio.coroutine, 
协程函数中不能出现yield, 
可以不包含await, async
"""
async def a():
    for i in range(3):
        print('a.{}'.format(i))
        """
        await后搭配一个awaitable对象, 表示该进行IO阻塞了, 该切换协程了
        await 会在此处暂停当前协程, 去执行其他协程
        awaitable对象可以是 协程对象, 也可以是实现了 __await__()方法的对象
        """
        await wait()
    return 'a 1000'


async def b():
    for i in 'abc':
        print('b.{}'.format(i))
        await wait()    # await搭配一个awaitable对象, 表示该进行IO阻塞了, 该切换协程了
    return 'b 1000'


loop = asyncio.get_event_loop()

task1 = loop.create_task(a())
task2 = loop.create_task(b())

task1.add_done_callback(res)    # 添加回调函数
task2.add_done_callback(res)

loop.run_until_complete(asyncio.wait((task1, task2)))   # 使用asyncio.wait() 将多个task放入


loop.close()

