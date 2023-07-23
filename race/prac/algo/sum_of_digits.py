# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/2
Describe:给定一个正整数，请编写一个python函数，将它的字面数字进行累加总和，
并列出算式。例如1234 ，那么返回1 + 2 + 3 + 4 = 10 。

题目难度：简单
"""


def sum_of_digits(num: int) -> str:

    s = str(num)
    res = ""
    for i in range(len(s)):
        if i < len(s) - 1:
            res = res + s[i] + " + "
        else:
            res += s[i]
    return res + " = " + str(eval(res))

    # s = 0
    # y = ''
    # for i in range(len(str(num))):
    #     s += int(str(num)[i])
    #     y += str(num)[i] + " + "
    #
    # return y[:-2] + f'= {s}'


if __name__ == "__main__":

    assert sum_of_digits(1234) == "1 + 2 + 3 + 4 = 10"
    assert sum_of_digits(64323) == "6 + 4 + 3 + 2 + 3 = 18"
    assert sum_of_digits(8) == "8 = 8"

