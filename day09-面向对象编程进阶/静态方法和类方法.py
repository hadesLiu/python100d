# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: 静态方法和类方法.py
# @Time    : 2019/6/4 9:07 AM


class A(object):

    def __init__(self, bar):
        self.bar = bar

    def foo(self):
        print('hello', self)

# class A(object):
#
#     bar = 1
#
#     @classmethod
#     def class_foo(cls):
#         print('hello', cls)
#         print(cls.bar)


# class A(object):
#
#     bar = 1
#
#     @staticmethod
#     def static_foo():
#         print('hello', A.bar)


def main():
    a = A('123')
    a.foo()
    print(a.bar)

    # A.class_foo()

    # A.static_foo()


if __name__ == '__main__':
    main()
