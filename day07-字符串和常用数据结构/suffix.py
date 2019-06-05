# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: suffix.py
# @Time    : 2019/6/3 9:51 AM


"""
    设计一个函数返回给定文件名的后缀名。
"""


def main(filename, has_dot=False):
    """
    设计一个函数返回给定文件名的后缀名。

    :param filename: 给定的文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 返回给定文件名的后缀名
    """

    pos = filename.rfind('.')
    if 0 < pos < len(filename) -1:
        index = pos if has_dot else pos + 1
        # if has_dot:
        #     index = pos
        # else:
        #     index = pos + 1
        return filename[index:]
    else:
        return ''
    # suffix = filename.strip().split('.')[1]
    # return suffix


if __name__ == '__main__':
    print(main('login.sh', has_dot=True))
