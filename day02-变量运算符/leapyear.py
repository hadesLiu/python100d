# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: leapyear.py
# @Time    : 2019/5/24 8:57 AM

"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""

year = int(input("请输入年份："))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     is_leap = True
# else:
#     is_leap = False

is_leap = ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

print(is_leap)
