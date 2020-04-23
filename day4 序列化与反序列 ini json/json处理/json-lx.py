# encoding = utf-8
__author__ = "Ang Li"

import json
from configparser import ConfigParser

# 将my.ini 转换成json格式

s_file = "my.ini"
d_file = "my.json"

cfg = ConfigParser()
cfg.read(s_file)


def get_section():
    """
    将所有section 转换为字典
    :return: dict_list, section 与 option value的嵌套结构
    """
    dict_list = {}
    for section in cfg.sections():
        dict_list[section] = {}
        for i in cfg.options(section):
            dict_list[section][i] = cfg.get(section, i)
    return dict_list


def to_json(list):
    """
    json 序列化
    :param list: ini 转换后的 字典数据
    :return:
    """
    with open(d_file, 'w', encoding='utf-8') as f:
        json.dump(list, f)


if __name__ == "__main__":
    to_json(get_section())