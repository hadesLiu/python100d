# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: circle.py
# @Time    : 2019/5/24 8:49 AM

"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""
import math

radius = float(input("请输入圆的半径："))

perimeter = 2 * math.pi * radius

area = math.pi * radius * radius

print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
