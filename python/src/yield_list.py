# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

L = "abcdef"


def test(long_str):
    for c in long_str:
        yield c


for i in test(L):
    print(i)

# 读出文件里的没一个单词，并去掉重复的单词

with open('/etc/passwd', 'r') as page:
    unique_words = set(word for line in page for word in line.split(':'))

# 求1-9 数字阶乘的和
he = sum(i*i for i in range(10))
print(he)

# 求两个列表对应数字乘机的和
xvec = [22, 8, 32, 9]
yvec = [3, 7, 1, 23]

print(sum(x*y for x in xvec for y in yvec))

# 反向排序字符串
data = "golf"
print([char for char in data[::-1]])
