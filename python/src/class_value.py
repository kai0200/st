# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
'''
注意冒号和等号的区别
'''
from dataclasses import dataclass

@dataclass
class Dog(object):
    kind = 'canine'
    name: str       # 注意冒号和等号的区别 
    old: int

    def get(self, old):
        self.old = int(old)
        print(self.old)

d = Dog('Fido', 8)
d.get(6)
print(Dog.kind)
print(d.kind)
