# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: palindromeNumber.py
# @Time    : 2019/5/30 10:21 PM

"""
函数的定义和使用 - 实现判断一个数是不是素数的函数
Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""
from math import sqrt


def is_prime(num):

    end = int(sqrt(num))+1

    for factor in range(2, end):
        if num % factor == 0:
            return False
    return True if num != 1 else False


# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(6))


"""
写一个程序判断输入的正整数是不是回文素数。
"""


def is_palindrome(num):

    temp = num
    num2 = 0

    while temp > 0:
        num2 = num2 * 10 + temp % 10
        temp //= 10
    return num2 == num


if __name__ == '__main__':
    num = int(input('请输入正整数'))
    if is_prime(num) and is_palindrome(num):
        print('%d 是回素数' % num)