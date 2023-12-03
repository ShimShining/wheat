# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/3
Describe:2351. 第一个出现两次的字母
给你一个由小写英文字母组成的字符串 s ，请你找出并返回第一个出现 两次 的字母。
如果 a 的 第二次 出现比 b 的 第二次 出现在字符串中的位置更靠前，则认为字母 a 在字母 b 之前出现两次。
s 包含至少一个出现两次的字母。
输入：s = "abccbaacz"
输出："c"
解释：
字母 'a' 在下标 0 、5 和 6 处出现。
字母 'b' 在下标 1 和 4 处出现。
字母 'c' 在下标 2 、3 和 7 处出现。
字母 'z' 在下标 8 处出现。
字母 'c' 是第一个出现两次的字母，因为在所有字母中，'c' 第二次出现的下标是最小的。

输入：s = "abcdd"
输出："d"
解释：
只有字母 'd' 出现两次，所以返回 'd' 。
"""


def repeated_character(s):
    """
    :param s:
    :return:
    16ms 击败 80.39%使用 Python 的用户
    12.97MB 击败 41.18%使用 Python 的用户
    """
    d = dict()
    for c in s:
        if c in d:
            return c
            # d[c] += 1
            # if d[c] >= 2:
            #     return c
        else:
            d[c] = 1


def repeated_character_opt(s):
    """
    状态压缩  二进制0-25位表示是否已经遍历到当前最字符
        第一次遍历到, 对应位由0 变位1
        第二次遍历到, 对应位与为真,返回字符c
    :param s:
    :return:
    8ms 击败 98.04%使用 Python 的用户
    12.92MB 击败 66.67%使用 Python 的用户
    """
    seen = 0
    for c in s:
        pos = ord(c) - ord('a')
        if seen & (1 << pos):
            return c
        seen |= (1 << pos)
