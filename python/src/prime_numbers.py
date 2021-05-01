# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

'''
Print prime number # 素数
'''


# test filter

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(list(filter(lambda x: x%2, L)))

# search prime number

def _odd_iter(): # odd num 奇数
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x%n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    for n in primes():
        if n < 99999:
            print(n)
        else:
            break
