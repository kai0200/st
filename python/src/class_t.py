# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4


class father(object):
    def __init__(self,age):
        self.age = age;
    def get_age(self):
        print(self.age);

class mother(object):
    def __init__(self,age):
        self.age = age;
    def get_age(self):
        print(self.age);

class son(father, mother):
    def __init__(self,age):
        super(son, self).__init__(age);
        self.toy_number = 5;
    def get_toy_number(self):
        print(self.toy_number);
    def test_super(self):
        super(son,self).get_age()

myson = son(6)
myson.get_age()
myson.get_toy_number()
myson.test_super()

