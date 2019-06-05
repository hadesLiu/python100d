# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: rectangle.py
# @Time    : 2019/6/5 2:45 PM

"""
    定义和使用矩形类
"""


class Rect(object):
    """矩形类"""

    def __init__(self, length=0.0, width=0.0):
        """
        初始化方法

        :param length: 长度
        :param width: 宽度
        """

        self._length = length
        self._width = width

    def perimeter(self):
        """计算周长"""

        return self._length * 2 +  self._width * 2

    def area(self):
        """计算面积"""

        return self._length * self._width

    def __str__(self):
        """矩形对象的字符串表达式"""

        return '矩形[%f, %f]' % (self._length, self._width)

    def __del__(self):
        """析构器"""

        print('销毁矩形对象')


def main():
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())

    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())


if __name__ == '__main__':
    main()
