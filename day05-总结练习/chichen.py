# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: chichen.py
# @Time    : 2019/5/28 8:41 AM

"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for x in range(21):
    for y in range(34):
        if 14 * x + 8 * y == 200:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, 100-x-y))

