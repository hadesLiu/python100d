# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: calculateDay.py
# @Time    : 2019/6/3 10:24 AM


"""
    计算指定的年月日是这一年的第几天
"""


def is_leap_year(year):
    """
    判断是否是闰年
    :param year: 年份
    :return: 返回True 或 False
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1989, 2, 28))
    print(which_day(1996, 3, 1))


if __name__ == '__main__':
    main()
