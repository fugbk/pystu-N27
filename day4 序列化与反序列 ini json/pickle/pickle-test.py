# encoding = utf-8
__author__ = "Ang Li"

import pickle

filename = "pickle.txt"
a = '1'
b = 1
c = ['aaa', 127]

x = pickle.dumps(a)
print(type(x), x)   # dumps 到内存，是bytes 类型

# with open(filename, 'wb') as f:
#     pickle.dump(a, f)   # dump 到文件
#     pickle.dump(b, f)
#     pickle.dump(c, f)

print(pickle.loads(x))

with open(filename, 'rb') as f:
    for i in range(3):
        y = pickle.load(f)
        print(type(y), y)




