# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: circle.py
# @Time    : 2019/6/3 7:27 PM

"""
练习
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)
Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""
from math import pi


class Circle(object):

    def __init__(self, radius):
        """
        初始化方法

        :param radius: 半径
        """

        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        """
        周长

        :return: 2 * pi * radius
        """

        return 2 * pi * self._radius

    @property
    def area(self):
        """
        面积

        :return:
        """

        return pi * self._radius * self._radius


def main():
    radius = float(input('请输入泳池的半径：'))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('围墙的造价为：%.2f' % (big.perimeter * 32.5))
    print('过道的造价为：%.2f' % ((big.area - small.area) * 25))


if __name__ == '__main__':
    main()