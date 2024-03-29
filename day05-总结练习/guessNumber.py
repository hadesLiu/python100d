# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: guess.py
# @Time    : 2019/5/28 9:03 AM

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    num = int(input('请输入一个1~100之间的整数：'))

    if num > answer:
        print('小一点')
    elif num < answer:
        print('大一点')
    else:
        print('猜对了')
        break

print('您总共猜了%d次' % counter)

if counter > 7:
    print('您的智商余额明显不足')

