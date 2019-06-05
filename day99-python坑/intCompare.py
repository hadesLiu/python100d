# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: intCompare.py
# @Time    : 2019/6/3 5:00 PM


"""
对于整数对象，Python把一些频繁使用的整数对象缓存起来，保存到一个叫small_ints的链表中，在Python的整个生命周期内，
任何需要引用这些整数对象的地方，都不再重新创建新的对象，而是直接引用缓存中的对象。
Python把频繁使用的整数对象的值定在[-5, 256]这个区间，如果需要这个范围的整数，
就直接从small_ints中获取引用而不是临时创建新的对象。因为大于256或小于-5的整数不在该范围之内，
所以就算两个整数的值是一样，但它们是不同的对象。
"""


def main():
    x = y = -1
    while True:
        x += 1
        y += 1
        if x is y:
            print('%d is %d' % (x, y))
        else:
            print('Attention! %d is not %d', (x, y))
            break

    x = y = 0
    while True:
        x -= 1
        y -= 1
        if x is y:
            print('%d is %d' % (x, y))
        else:
            print('Attention! %d is not %d', (x, y))
            break


if __name__ == '__main__':
    main()
