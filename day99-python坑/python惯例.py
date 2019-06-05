# -*- coding: utf-8 -*-
# @Author  : hiro,
# @Mail    : hiroliu@yeah.net
# @FileName: python惯例.py
# @Time    : 2019/6/5 10:39 AM

# a, b, c = 3, 5, 9

# the_max = a if a > b else b
# the_max = c if c > the_max else c
#
# print(the_max)


# def the_max(x, y):
#     return x if x > y else y
#
# print(the_max(the_max(a, b), c))


# if __name__ == '__main__':

# name = 'jackfrued'
# fruits = ['apple', 'orange', 'grape']
# owners = {'1001': '骆昊', '1002': '王大锤'}
#
# if name and fruits and owners:
#     print('I love fruits.')

# name = 'Hao LUO'
# if 'L' in name:
#     print('The name has an L in it.')

# a, b = b, a

# chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
# name = ''.join(chars)
# print(name)

# d = {'x': '5'}
# try:
#     value = int(d['x'])
#     print(value)
# except (KeyError, TypeError, ValueError):
#     value = None

# fruits = ['orange', 'grape', 'pitaya', 'blueberry']
# for index, fruit in enumerate(fruits):
#     print(index, ':', fruit)

# data = [7, 20, 3, 15, 11]
# result = [num * 3 for num in data if num > 10]
# print(result)


# keys = ['1001', '1002', '1003']
# values = ['骆昊', '王大锤', '白元芳']
# d = dict(zip(keys, values))
# print(d)
