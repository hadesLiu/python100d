# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: distance.py
# @Time    : 2019/6/3 7:01 PM

"""
    定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
"""
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指的位置

        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指的增量

        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        :return:
        """

        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算到另一个点的距离

        :param other: 另一个点
        :return: 距离长度
        """

        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p1.move_by(-1, 2)
    print(p1)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
