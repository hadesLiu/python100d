# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: palindromeNumber.py
# @Time    : 2019/5/28 9:04 AM

"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

num = int(input('请输入一个正整数：'))
temp = num
num2 = 0

while temp > 0:
    num2 = num2 * 10
    num2 = num2 + temp % 10
    temp = temp // 10

if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)

# num = int(input('请输入一个正整数：'))
# nstr = str(num)
# flag = True
#
# for i in range(len(nstr)//2):
#     print(nstr[i], nstr[-i-1])
#     if nstr[i] != nstr[-i-1]:
#         flag = False
#         break
#
# if flag:
#     print('%d 是一个回文数' % num)
# else:
#     print('%d 不是一个回文数' % num)
