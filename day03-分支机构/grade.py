# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: grade.py
# @Time    : 2019/5/24 9:23 AM

"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分    --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
Author: 骆昊
"""

score = float(input('请输入成绩：'))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('对应的等级是：', grade)