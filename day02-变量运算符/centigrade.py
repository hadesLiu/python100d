# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: temprature.py
# @Time    : 2019/5/22 5:33 PM

"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
"""


# 华氏温度：fahrenheit，摄氏温度：centigrade

f = int(input("请输入华氏温度："))
c = (f - 32) / 1.8

print('%.1f华氏度 = %.1f摄氏度' % (f, c))
