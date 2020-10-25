# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

def go2work(position, company = 'Sohu', time=9,):
    print("Your company {} is in: {}, work time is {}".format(
        position, company, time))



if __name__ == '__main__':
    go2work('HaiDian')
    go2work('HaiDian', company = 'HuaWei')
    go2work('HaiDian', company = 'HuaWei', time=996)
