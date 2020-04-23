# encoding = utf-8
__author__ = "Ang Li"

import json

filename = 'test.json'

direct = {
    'name': 'Tom',
    'age': 21,
    'like': ['read', 'games', 1, '1'],
    'family': ('jeery', 'mike', 'marry'),
    'student': False,
    'work': None
}

d1 = json.dumps(direct)     # dump 到内存
print(type(d1), d1)   # 字符串类型，元组 会被转成 列表, 同时 False， None 会被映射

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(direct, f)

with open(filename, 'r', encoding='utf-8') as f:
    l1 = json.load(f)   # 反序列化数据
    print(type(l1), l1)     # 保持原数据类型不变， 元组会被转换为 列表

print(l1 == direct)