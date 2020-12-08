# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

'''
测试类继承 super
'''

class father(object):
    def __init__(self, nation):
        self.nation = nation

    def get(self, nation):
        self.nation = nation

    def put(self):
        print("Father", self.nation)

class mother(object):
    def __init__(self, nation):
        self.nation = nation

    def get(self, nation):
        self.nation = nation

    def put(self):
        print("Moter", self.nation)

class son(father, mother):
    def __init__(self, nation, city):
        super(son, self).__init__(nation)
        self.city = city

    def super_get(self, nation):
        #super(son, self).get(nation)
        father.get(nation)

    def super_put(self):
        #super(son, self).put() # python2
        super().put()         # python3
        #return(self.nation)

s = son('China', 'BeiJing')
s.put()
s.super_put()
