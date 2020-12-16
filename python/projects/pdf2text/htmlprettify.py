# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
"""
Beautifulsoup prettify html to stdout
$ python3 htmlprettify.py name.html | more
"""

from bs4 import BeautifulSoup
import sys


with open(sys.argv[1], 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
    print(soup.prettify())
