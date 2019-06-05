# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: clock.py
# @Time    : 2019/6/3 5:29 PM

"""
    定义一个类描述数字时钟，以及使用时钟
"""
import os
import time


class Clock(object):
    """数字时钟"""

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
        """走字"""

        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""

        print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))


def main():
    clock = Clock(17, 30, 20)
    clock.show()

    while True:
        clock.run()
        time.sleep(1)
        os.system('clear')
        clock.show()


if __name__ == '__main__':
    main()


