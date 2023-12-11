# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/11
Describe:NC28 最小覆盖子串
给出两个字符串 s 和 t，要求在 s 中找出最短的包含 t 中所有字符的连续子串。
数据范围：0≤10000
0≤∣S∣,∣T∣≤10000，保证s和t字符串中仅包含大小写英文字母
要求：进阶：空间复杂度 O(n) ， 时间复杂度 O(n)
例如：
S="XDOYEZODEYXNZ"
T="XYZ"
找出的最短子串为"YXNZ".
注意：
如果 s 中没有包含 t 中所有字符的子串，返回空字符串 “”；
满足条件的子串可能有很多，但是题目保证满足条件的最短的子串唯一。
输入：
"XDOYEZODEYXNZ","XYZ"
返回值：
"YXNZ"
输入：
"abcAbA","AA"
返回值：
"AbA"
"""


def min_window(S: str, T: str):
    t_dict = dict()
    for s in T:
        if s in t_dict:
            t_dict[s] += 1
        else:
            t_dict[s] = 1
    window_dict = dict()
    for k in t_dict:
        if k not in window_dict:
            window_dict[k] = 0

    def check(cur_dict, obj_dict):
        for k in obj_dict:
            if cur_dict[k] < obj_dict[k]:
                return False
        return True

    start = 0
    min_length = float("inf")
    res = ""
    for end in range(len(S)):
        if S[end] in T:
            window_dict[S[end]] += 1
        while check(window_dict, t_dict):
            if end - start + 1 < min_length:
                min_length = end - start + 1
                res = S[start:end + 1]
            if S[start] in T:
                window_dict[S[start]] -= 1
            start += 1
    return res
