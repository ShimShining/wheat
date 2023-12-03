# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/8
Describe:字符串RGB排序
输入RGBGRB等字符,最后输出按照R在前,G在中,B在后排列
"""


def str_sort(s):

    r_s = ""
    g_s = ""
    b_s = ""
    for item in s:
        if item == "R":
            r_s += item
        elif item == "G":
            g_s += item
        else:
            b_s += item

    return r_s + g_s + b_s


if __name__ == "__main__":

    temp = "GBRGBR"
    res = str_sort(temp)
    print(res)

