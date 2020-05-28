# encoding = utf-8
__author__ = "Ang Li"


import logging
import os

BASE_PWD = os.path.dirname(os.path.abspath(__file__))
print(BASE_PWD)

log_file = ""

# 日志格式
FORMAT = "%(asctime)s %(levelname)s: %(message)s"  # %()代表格式，s 代表当做字符串处理

# basicConfig 只能定义一次，是全局生效的                 # filename=, 定义日志输出文件
logging.basicConfig(level=logging.DEBUG, format=FORMAT, filename='d:/output.txt', filemode='w')     # 也可以定义日志级别，定义输出格式

# 使用RootLogger直接进行日志输出，不用实例化了
logging.root.setLevel(logging.INFO)     # 先设置 级别 为 INFO
logging.info('test logging info +')


handle = logging.StreamHandler()   # 定义一个Handle
logging.root.addHandler(handle)     # 添加到 logger
handle.setLevel(logging.DEBUG)

# 定义一个格式
formater = logging.Formatter("%(asctime)s [%(message)s]")    # 传进来一个字符串，表示格式
# 添加到 Handle
handle.setFormatter(formater)

logging.info('test root info')
logging.debug('test root debug')