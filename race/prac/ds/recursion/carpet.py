# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: 谢尔宾斯基地毯
"""


def carpet(n, char):

    def check(n, x, y):
        if n <= 1:
            return True
        n2 = n // 3
        if n2 <= x < n2 * 2 and n2 <= y < n2 * 2:
            return False
        return check(n2, x % n2, y % n2)

    for y in range(n):
        for x in range(n):
            if check(n, x, y):
                print(char, end="")
            else:
                print(" " * len(char), end="")
        print("")


if __name__ == '__main__':
    carpet(27, "[]")

