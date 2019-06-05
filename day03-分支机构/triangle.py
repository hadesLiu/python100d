# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: triangle.py
# @Time    : 2019/5/26 10:29 AM

"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and c + a > b:
    print('周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积：%f' % (area,))
else:
    print('不能构成三角形')
