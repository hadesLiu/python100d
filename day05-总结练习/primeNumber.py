# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: primeNumber.py
# @Time    : 2019/5/28 9:06 AM

"""
输出2~99之间的素数
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from math import sqrt

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=' ')