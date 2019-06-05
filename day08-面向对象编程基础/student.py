# -*- coding: utf-8 -*-
# @Author  : hiro,
# @Mail    : hiroliu@yeah.net
# @FileName: test.py
# @Time    : 2019/6/3 5:09 PM


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s 正在学习 %s' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s 只能观看《熊出没》。' % self.name)
        else:
            print('%s 正在观看岛国爱情动作片。' % self.name)


def main():
    stu1 = Student('hiro', 28)
    stu1.study('python核心编程')
    stu1.watch_av()

    stu2 = Student('tom', 15)
    stu2.study('C++')
    stu2.watch_av()


if __name__ == '__main__':
    main()
