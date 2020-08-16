# encoding = utf-8
__author__ = "mcabana.com"

import asyncio


@asyncio.coroutine
def a():
    for _ in 'abc':
        print('a', _)
        yield
    return 'a() return = 1000'


@asyncio.coroutine
def b():
    for i in range(7):
        print('b', i)
        yield
    return 'b() return = 2000'


def cb(future):
    print(future.result())


loop = asyncio.get_event_loop()

ts = []
for t in (a(), b()):
    t = asyncio.ensure_future(t)
    t.add_done_callback(cb)
    ts.append(t)

# ret 中保存了每个任务的状态, 及返回值
ret = loop.run_until_complete(asyncio.wait(ts))

loop.close()