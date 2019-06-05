# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: maxElement.py
# @Time    : 2019/6/3 10:03 AM

"""
    设计一个函数返回传入的列表中最大和第二大的元素的值。
"""


def main(li):
    """
    返回传入的列表中最大和第二大的元素的值
    :param li: 传入的列表
    :return: 列表中最大和第二大的元素的值
    """
    m1, m2 = (li[0], li[1]) if li[0] > li[1] else (li[1], li[0])
    for index in range(len(li)):
        if m1 < li[index]:
            m2 = m1
            m1 = li[index]
        elif m2 < li[index]:
            m2 = li[index]
    return m1, m2


if __name__ == '__main__':
    print(main([3, 5, 9]))
