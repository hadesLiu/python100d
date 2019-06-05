# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: marquee.py
# @Time    : 2019/6/3 8:03 AM


"""
    在屏幕上显示跑马灯文字
"""
import os
import time


def main():

    content = '北京欢迎你为你开天辟地…………'

    while True:
        # 清屏
        os.system('clear')
        print(content)
        # 休眠1s
        time.sleep(1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()






