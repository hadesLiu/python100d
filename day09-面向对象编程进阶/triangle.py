# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: triangle.py
# @Time    : 2019/6/3 9:04 PM
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        """
        初始化

        :param a: 边长a
        :param b: 边长b
        :param c: 边长c
        """
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """
        判断能否构成三角形

        :return: True or False
        """

        return a + b > c and b + c > a and c + a > b

    def perimeter(self):
        """
        三角形周长

        :return: 周长长度
        """

        return self.a + self.b + self.c

    def area(self):
        """
        三角形面积

        :return: 三角形面积
        """

        half = self.perimeter() / 2
        return sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))


def main():
    a, b, c = 3, 4, 1

    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t1 = Triangle(3, 4, 5)
        print(t1.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t1))
        print(t1.area())
        # print(Triangle.area(t1))
    else:
        print('无法构成三角形')


if __name__ == '__main__':
    main()

