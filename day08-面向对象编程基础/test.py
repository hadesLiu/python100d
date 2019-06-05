# -*- coding: utf-8 -*-
# @Author  : hiro,
# @Mail    : hiroliu@yeah.net
# @FileName: test.py
# @Time    : 2019/6/3 5:09 PM


class Test(object):

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # print(test.__foo)
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()







