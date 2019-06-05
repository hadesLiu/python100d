# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: clock.py
# @Time    : 2019/6/4 9:21 AM


class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """

        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """
        走字

        :return:
        """

        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """
        显示时间

        :return: 时：分：秒
        """

        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    c = Clock()
    print(c.show())


if __name__ == '__main__':
    main()
