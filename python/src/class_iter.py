# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

'''
测试类的迭代
'''

class T(object):
    '''
    看过迭代器协议的幕后机制，给你的类添加迭代器行为就很容易了。 
    定义一个 __iter__() 方法来返回一个带有 __next__() 方法的对象。 
    如果类已定义了 __next__()，则 __iter__() 可以简单地返回
    '''
    def __init__(self, data):
        self.data = data
        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

t = T([1, 2, 3, 4, 5, 6, 7])

for n in range(t.index):  # next(t) 不是 t.next
    print(next(t))
    
