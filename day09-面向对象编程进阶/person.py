# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: person.py
# @Time    : 2019/6/3 7:43 PM


class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        """
        初始化方法

        :param name: 姓名
        :param age: 年龄
        """

        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋' % self._name)
        else:
            print('%s正在玩斗地主' % self._name)


def main():
    p1 = Person('hiro', 12)
    p1.play()
    p1.age = 22
    p1.play()
    # AttributeError: can't set attribute
    # p1.name = 'tom'
    p1._gender = '男'
    # AttributeError: 'Person' object has no attribute '_phone'
    # p1._phone = '123'


if __name__ == '__main__':
    main()