# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/7
Describe:HJ23 删除字符串中出现次数最少的字符
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

数据范围：输入的字符串长度满足 1≤n≤20  ，保证输入的字符串中仅出现小写字母
删除字符串中出现次数最少的字符后的字符串。
输入：aabcddd
输出：aaddd
"""


def remove_char(s):
    cnt = dict()
    for c in s:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    min_cnt = len(s)
    min_char = []
    for k, v in cnt.items():
        if v < min_cnt:
            min_cnt = v
    for k, v in cnt.items():
        if v == min_cnt:
            min_char.append(k)
    ss = []
    if min_char:
        ss = list(s)
        for c in min_char:
            for i in range(min_cnt):
                ss.remove(c)
    return "".join(ss)



def remove_char_1(s):
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    res = ''
    min_cnt = min(d.values())
    for c in s:
        if d[c] != min_cnt:
            res += c
    return res


if __name__ == '__main__':
    s = "aabcddd"
    print(remove_char(s))