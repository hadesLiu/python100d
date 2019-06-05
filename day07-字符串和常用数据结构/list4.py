# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: list4.py
# @Time    : 2019/6/1 10:34 AM


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
