# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: convert.py
# @Time    : 2019/5/24 9:09 AM

"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: 骆昊
"""

value = float(input('请输入长度：'))
unit = input('请输入单位：')

if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print("请输入有效的单位")