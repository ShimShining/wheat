# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/5
Describe: 十六进制数转换为十进制
"""
import sys


def cast_hex_to_num(h: str):
    cast_map = {
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }
    s = 0
    n = len(h[2:])
    for i, c in enumerate(h[2:]):
        if c in cast_map:
            s += cast_map[c] * 16 ** (n - i - 1)
        else:
            s += int(c) * 16 ** (n - i - 1)
    return s


if __name__ == '__main__':
    h = "oxAA"
    print(cast_hex_to_num(h))
    for line in sys.stdin:
        a = line.split()
        n = cast_hex_to_num(a[0])
        print(n)
        # print(int(a[0]) + int(a[1]))
