# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

'''
try except els finally
'''


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as err:
        print('division by zero!:{0}'.format(err))
    else:
        print("result is :", result)
    finally:
        print("######executing finally clause!######")


if __name__ == '__main__':
    divide(4, 2)
    divide(4, 0)
