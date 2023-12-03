# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/3
Describe:统计出现次数最多的字母
"""


def count_max_repeated_char(s):
    d = dict()
    max_cnt = 0
    max_c = ""
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
        if d[c] > max_cnt:
            max_cnt = d[c]
            max_c = c

    return max_c, max_cnt


if __name__ == '__main__':
    s = "aabbbccccssfd"
    s = "abcd"
    print(count_max_repeated_char(s))

