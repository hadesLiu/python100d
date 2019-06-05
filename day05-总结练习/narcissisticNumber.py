# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: narcissisticNumber.py
# @Time    : 2019/5/27 5:52 PM


"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
如: 153 = 1**3 + 5**3 + 3**3
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

na_num = []

for num in range(100, 1000):

    x = num // 100
    y = num // 10 % 10
    z = num % 10

    if x ** 3 + y ** 3 + z ** 3 == num:
        na_num.append(num)

print('100~999之间的所有水仙花数为：%s' % na_num)
