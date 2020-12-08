# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

'''
使用json保存结构化数据
'''
import json


l =  ['name', 'age', 'class', 'address', 'phoneNum']
d = {
    'name': 'Daiyu',
    'age': '15',
    'class': 'DaGuanYuan',
    'address': 'XiaoXiangGuan',
    'phoneNum': '9527001',
}


def read_json(file):
    with open(file) as f:
        x = json.load(f)
    return x

def write_json(value, file):
    with open(file, 'w') as f:
        x = json.dump(value, f)
    return x


if __name__ == '__main__':
    file = '/tmp/b.txt'
    write_json(d, file)
    print(read_json(file))
