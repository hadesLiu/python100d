# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: tax.py
# @Time    : 2019/5/26 10:40 AM

"""
输入月收入和五险一金计算个人所得税(2017版)

Version: 0.1
Author: 骆昊

补：
计算公式：

应纳税所得额 = 工资收入金额 － 各项社会保险费 － 起征点(3500元)
diff = salary - insurance - 3500

应纳税额 = 应纳税所得额 x 税率 － 速算扣除数
tax = diff * rate - deduction

实发工资 = 工资收入金额 － 各项社会保险费 － 应纳税额
money = salary - insurance - tax

"""

salary = float(input('请输入收入：'))
insurance = float(input('请输入五险一金：'))

diff = salary - insurance - 3500

if diff <= 0:
    rate = 0
    dedunction = 0
elif diff <= 1500:
    rate = 0.03
    dedunction = 0
elif diff <= 4500:
    rate = 0.1
    dedunction = 105
elif diff <= 9000:
    rate = 0.2
    dedunction = 555
elif diff <= 35000:
    rate = 0.25
    dedunction = 1005
elif diff <= 55000:
    rate = 0.3
    dedunction = 2755
elif diff <= 80000:
    rate = 0.35
    dedunction = 5505
else:
    rate = 0.45
    dedunction = 13505

tax = abs(diff * rate - dedunction)

print('个人所得税：￥%.2f' % (tax, ))
print('实际收入：￥%.2f' % (salary - insurance - tax, ))
