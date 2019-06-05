# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: lottery.py
# @Time    : 2019/6/3 11:34 AM


"""
双色球随机选号程序
Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

from random import randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    :param balls: 列表，双色球号码
    :return: 标准格式的双色球号码
    """
    for index in range(len(balls)):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % balls[index], end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    :return: 六个1-33的号码和一个1-16的号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
