# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: commonDivisor.py
# @Time    : 2019/5/27 4:17 PM

"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

x = int(input('请输入第一个数字：'))
y = int(input('请输入第一个数字：'))
gcd = 1
lcm = 1

if x > y:
    smaller = y
else:
    smaller = x

for factor in range(1, smaller + 1):
    if x % factor == 0 and y % factor == 0:
        gcd = factor
        lcm = x * y // factor

print('最大公约数为：%d' % gcd)
print('最小公倍数为：%d' % lcm)


# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break
