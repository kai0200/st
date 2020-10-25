# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

'''
测试*arg **keys
'''


def find_student(school, *arguments, **keywords):
    print(school)
    for arg in arguments:
        print(arg)

    for key in keywords:
        print(key, ':', keywords[key])


if __name__ == '__main__':
    find_student('新华小学', 1, 2, 3, 4, id='No9527', name='HuangShiRen')
