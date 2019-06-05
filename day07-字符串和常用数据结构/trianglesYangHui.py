# -*- coding: utf-8 -*-
# @Author  : hiro, 
# @Mail    : hiroliu@yeah.net
# @FileName: trianglesYangHui.py
# @Time    : 2019/6/3 11:00 AM

"""
    打印杨辉三角
　　　　　　　　１
　　　　　　　１　１
　　　　　　１　２　１
　　　　　１　３　３　１
"""


def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end=' ')
        print()



# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()


# def triangles(num):
#     L = [1]
#     S = []
#     print(L)
#     for i in range(num):
#         L = [1] + S + [1]
#         S = []
#
#         for i in range(len(L) - 1):
#             S.append(L[i] + L[i + 1])
#         print(L)
#
#
# def main():
#     triangles(5)
#
#


if __name__ == '__main__':
    main()


