# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: verificationCode.py
# @Time    : 2019/6/3 8:30 AM


"""
    设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random
import string


def verfication_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认是4)

    :return:由大小写英文字母和数字构成的随机验证码
    """

    all_chars = string.digits + string.ascii_letters
    return "".join(random.sample(all_chars, code_len))


if __name__ == '__main__':
    print(verfication_code())
