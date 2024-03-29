# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: perfectNumber.py
# @Time    : 2019/5/27 9:29 PM

"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

import time
import math

start = time.clock()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)
end = time.clock()
print("执行时间:", (end - start), "秒")

# import time
#
# start = time.clock()
# for i in range(1, 10000):
#     res = 0
#     for j in range(1, i):
#         if i % j == 0:
#             res = res + j
#     if res == i:
#         print('%d 是完美数' % res)
# end = time.clock()
# print("执行时间：", (end - start), "秒")

