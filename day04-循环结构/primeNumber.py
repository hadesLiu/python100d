# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: primeNumber.py
# @Time    : 2019/5/27 8:44 AM

"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

# num = int(input('请输入正整数：'))
# n = 0
#
# if num <= 1:
#     print('不是素数')
#
# for i in range(2, num):
#     remain = num % i
#     if remain == 0:
#         n = n + 1
#
# if n > 0:
#     print("不是素数")
# else:
#     print("是素数")