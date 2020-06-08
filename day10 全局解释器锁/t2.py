# encoding = utf-8
__author__ = "mcabana.com"


import logging
import datetime
logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")
start = datetime.datetime.now()
# 计算
def calc():
    sum = 0
    for _ in range(1000000000): # 10亿
        sum += 1

calc()
calc()
calc()
calc()
delta = (datetime.datetime.now() - start).total_seconds()
logging.info(delta)
