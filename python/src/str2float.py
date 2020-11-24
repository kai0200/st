# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
'''
map/reduce/lambda/三个函数的理解
'''


from functools import reduce


def char2num(c):
    ''' 字母转数字 '''
    return({
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '0': 0,
    }[c])

def num2char(n):
    ''' 单个数字转字符 '''
    return({
        0: '0' ,
        1: '1' ,
        2: '2' ,
        3: '3' ,
        4: '4' ,
        5: '5' ,
        6: '6' ,
        7: '7' ,
        8: '8' ,
        0: '0' ,
    }[n])

def str2num(s):
    ''' 字符串转数字 reduce ×10 map生成数字 '''
    return(reduce(lambda x,y: x*10 + y, map(char2num, s)))

def num2str(n):
    ''' 数字转字符串  取余数add进list，
    取整循环到上一位， list -1 反序，
    map找到对应char， reduce连接成字符串'''
    L = []
    while n > 0:
        L.append(n % 10)
        n = n // 10
    return(reduce(lambda x,y: x+y, map(num2char, L[::-1])))

def int2dec(n):
    ''' 整数转为0. 开头的小数'''
    return(n/10**len(num2str(n)))  # 这里实际上可以用len(str(n)) 

def str2float(s):
    ''' 字符串转浮点数 '''
    # 这里的逻辑是把字符串按“.”分成两段，xy正常都转为正整数，y变为0.开头小数，然后相加。
    return(reduce(lambda x,y: x+int2dec(y), map(str2num, s.split('.'))))

#print(char2num('0'))
#print(str2num('111'))
#print(num2str(1))
#print(int2dec(123))
print(str2float('123.123'))


