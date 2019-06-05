# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: tax2019.py
# @Time    : 2019/5/27 8:29 AM

"""
输入月收入和五险一金计算个人所得税(2019版)

补：
计算公式：

应纳税所得额 = 工资收入金额 － 各项社会保险费 － 起征点(3500元)
diff = salary - insurance - 3500

应纳税额 = 应纳税所得额 x 税率 － 速算扣除数
tax = diff * rate - deduction

实发工资 = 工资收入金额 － 各项社会保险费 － 应纳税额
money = salary - insurance - tax

"""