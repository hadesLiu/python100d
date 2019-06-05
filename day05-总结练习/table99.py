# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: table99.py
# @Time    : 2019/5/28 9:06 AM

"""
输出乘法口诀表(九九表)
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for row in range(1, 10):
    for column in range(1, row + 1):
        print('%d * %d = %d' % (column, row, column * row), end='\t')
    print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()