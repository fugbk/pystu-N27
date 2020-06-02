# encoding = utf-8
__author__ = "www.mcabana.com"

import time
import logging
import os
from logging.handlers import TimedRotatingFileHandler


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(BASE_DIR, "test.log")   # 日志文件路径

# 日志文件格式
FORMAT = "%(asctime)s %(processName)s %(levelname)s: %(message)s"

# 日志同时打印到屏幕 --- 利用了Handler的传播属性
logging.basicConfig(format=FORMAT)

# 实例化Logger 级别为 DEBUG，这些是写入文件的日志
log = logging.getLogger('debug')
log.setLevel(logging.DEBUG)

# 定义handler ， 文件模式，追加写入， 使用TimedRotatingFileHandler 按时间轮询, 也可以按大小轮询
handler = TimedRotatingFileHandler(log_file, 's', 10, encoding='utf-8')
log.addHandler(handler)     # 添加到 logger

# 开启 传播，用来将warning日志打印到标准输出
log.propagate = True

# 定义一个格式化器
formater = logging.Formatter(FORMAT)    # 调用 FORMAT 格式

# 将格式化器添加到 Handle
handler.setFormatter(formater)

# 日志轮询切割测试
for i in range(20):
    time.sleep(3)
    log.debug('test in debug {:03}'.format(i))
    log.info('test in info {:03}'.format(i))

