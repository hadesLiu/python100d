# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: palindromeNumber.py
# @Time    : 2019/5/30 10:21 PM

"""
函数的定义和使用 - 实现判断一个数是不是回文数的函数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def is_palindrome(num):

    temp = num
    num2 = 0

    while temp > 0:
        num2 = num2 * 10 + temp % 10
        temp //= 10
    return num2 == num


print(is_palindrome(12321))

print(is_palindrome(12322))

print(is_palindrome(6))