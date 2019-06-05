# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: association.py
# @Time    : 2019/6/5 3:23 PM
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法

        :param x: 横坐标
        :param y: 总坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置

        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """

        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动的增量

        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        :return:
        """

        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算到另一点的距离

        :param other: 另一个点
        :return: 距离长度
        """

        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        """点对象的字符串表达式"""

        return '(%s, %s)' % (self.x ,self.y)


def main():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    print(p1)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
