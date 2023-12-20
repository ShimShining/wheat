# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/19
Describe: 环形字符串s
找出lox字符都恰好出现了偶数次(0次也算偶数次)
"""


def max_sub_str(s: str):
    if not s or not ("l" in s or 'o' in s or 'x' in s):
        return len(s)
    ss = s + s

    def is_match(i, j):
        if j - i > len(s)-1:
            return False
        ch = ss[i: j + 1]
        return ch.count("l") % 2 == 0 and ch.count("o") % 2 == 0 and ch.count("x") % 2 == 0

    start = 0
    end = 0
    cnt = 0
    while start < len(s) and end < len(ss):
        if end - start > len(s)-1:
            start += 1
        if is_match(start, end):
            cnt = max(cnt, end - start + 1)
        end += 1
    return cnt


if __name__ == '__main__':
    s = "alolobo"
    print(max_sub_str(s))
