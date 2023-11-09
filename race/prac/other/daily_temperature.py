# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: 多少天后温度会超过当天
"""


def daily_temperature(tmp):

    res = [0] * len(tmp)
    for i, item in enumerate(tmp):
        if i == len(tmp) - 1:
            break
        for j, val in enumerate(tmp[i+1:]):
            if val > item:
                res[i] = j + 1
                break
    return res


if __name__ == '__main__':
    t = [73, 74, 75, 71, 69, 72, 76, 73]

    print(daily_temperature(t))

