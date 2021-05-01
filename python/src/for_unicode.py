# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
https://www.fuhaozi.com/unicode/   unicode list
"""
def loop_unicode_hex(start, end):
    return [chr(num) for num in range(int(start, 16), int(end, 16))]


if __name__ == "__main__":
    # 字母和数字符号
    for c in loop_unicode_hex('1D400', '1D7FF'):
        print(c, end=' ')

    # 麻将牌字符
    for c in range(0x1F000, 0x1F02F):
        print(chr(c), end=' ')

    for c in loop_unicode_hex('1F000', '1F02F'):
        print(c, end=' ')
