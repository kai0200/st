# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

with open('/etc/hosts') as f:
    for line in f.readlines():
        print(line,)
        print(f.tell())

with open('/tmp/a.txt', 'w') as fw:
    for n in range(33, 127):
        fw.write('{number}-{char}\n'.format(number = n, char = chr(n)))
