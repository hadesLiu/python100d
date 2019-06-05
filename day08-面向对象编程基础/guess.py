# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: guess.py
# @Time    : 2019/6/5 11:34 AM

"""
    面向对象版本的猜数字游戏
"""
from random import randint


class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint

    def reset(self):
        """
        重置赋值

        :return:
        """
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        """
        猜测数字的方法

        :param your_answer: 猜测的数字
        :return: True or False
        """
        self._counter += 1

        if your_answer > self._answer:
            self._hint = '输入再小一点'
        elif your_answer < self._answer:
            self._hint = '输入再大一点'
        else:
            self._hint = '恭喜你猜对了'
            return True

        return False


def main():
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('请输入：'))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter >= 7:
            print('智商余额不足！')
        play_again = input('再玩一次？yes | no') == 'yes'


if __name__ == '__main__':
    main()











