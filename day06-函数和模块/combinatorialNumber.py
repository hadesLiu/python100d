# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: combinatorialNumber.py
# @Time    : 2019/5/30 9:46 PM

"""
函数的定义和使用 - 计算组合数C(7,3)
Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 将求阶乘的功能封装成一个函数
def factorial(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result


print(factorial(7)//factorial(3)//factorial(4))
