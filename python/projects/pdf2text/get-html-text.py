#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
Usage: python3 get-html-table.py HT15.html  > HT15_NEW.html
"""

import sys
import re
from bs4 import BeautifulSoup


def get_data(url):
    L = []
    soup = BeautifulSoup(url, 'lxml')
    for item in soup.find_all('section_header'):
        line = item.string.strip()
        L.append(line)

    return L


if __name__ == '__main__':
    file = sys.argv[1]
    with open(file, 'r') as htmlfile:
        lines = get_data(htmlfile)
        n1 = lines.index('1、固定利率。按照以下第')
        n2 = lines.index('一、乙方选择按')
        for num, item in enumerate(lines):
            if '本合同项下受托支付金额人民币' in item:
                n3 = num
        money = re.findall(r"\d+\.?\d*", lines[n3])
        n4 = lines.index('还款期数共')

        print("%s|%s|%s|%s" % (lines[n1+1],
                               lines[n2+1].split()[0],
                               money[0],
                               lines[n4 + 1]))
