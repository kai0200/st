#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
Usage: python3 get-html-table.py HT15.html  > HT15_NEW.html
"""

import sys
from bs4 import BeautifulSoup


def get_data(url):
    soup = BeautifulSoup(url, 'lxml')
    # 需要调整find_all里的内容
    for item in soup.find_all('table'):
        print(item)


if __name__ == '__main__':
    file = sys.argv[1]
    with open(file, 'r') as htmlfile:
        get_data(htmlfile)
