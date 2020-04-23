# encoding = utf-8
__author__ = "Ang Li"


from configparser import ConfigParser

filename = "test.ini"
cfg = ConfigParser()
cfg.read(filename)

# 获取所有的 section
for value in cfg:
    print(value)


# 获取的section name 以及 section 对象
for k,v in cfg.items():
    print(type(k), k, type(v), v)
print()

# 获取section 以及包含的字段，返回的是一个列表，元组格式返回kv对
for k,v in cfg.items():
    print(k, cfg.items(k))

for k in cfg.sections():   # 获取所有section 不包含 DEFAULT
    print(k)
    print(cfg.options(k))   # 获取section中的所有option，所有key中依然包括DEFAULT
print()

print(cfg.has_section('tttt'))      # 判断是否有这个section
print(cfg.has_option('mysql', 'port'))      # 判断这个section 中是否有这个option（缺失值也算）
print('------------------------')


# 获取 section 下 option 的值
x = cfg.get('mysqld', 'port')
print(type(x), x)       # 纯文本文件都是字符串类型
# 可以指定数据类型
y = cfg.getint('mysqld', 'port')
print(type(y), y)
# 获取布尔型
z = cfg.getboolean('mysql', 'testbl')
print(type(z), z)
print()

# 获取value 设置默认值, 获取mysql 下的 ttt 的值，如果没有则设置aaa，这里设置的值，可以是任意类型
print(cfg.get('mysql', 'ttt', fallback='aaa'))
print('------------------------')

if cfg.has_section('t1'):
    cfg.remove_section('t1')

# 增加section, 这里的操作都是在内存中进行的，增加完之后，需要手动写一下文件
cfg.add_section('t1')
cfg.set('t1', 'k1', 'v1')
print(cfg.get('t1', 'k1'))

with open(filename, 'w+', encoding='utf-8') as f:
    cfg.write(f)


# 本质双层字典结构=== {'mysql':{'port': 3306}｝---> ｛section: {option: value}｝
print(cfg['mysqld']['port'])
cfg['t2'] = {'k2': 'v2'}       # 通过嵌套字典结构，写入section ，option
print(cfg.get('t2', 'k2'))
cfg['t3'] = {'k3': 'v3', 'k4': 'v4'}    # 同时写入多个 option
print(cfg['t3']['k4'])
print('-------------------------------------')

# 关于缺省值， 如果section 中没有option 则适用DEFAULT。如果有，则优先适用option
cfg.set('t1', 'name', '100')    # 纯文本文件中，输入必须都是字符串格式
print(cfg.get('t1', 'name'))
print(cfg.get('t2', 'name'))
with open(filename, 'w+', encoding='utf-8') as f:
    cfg.write(f)