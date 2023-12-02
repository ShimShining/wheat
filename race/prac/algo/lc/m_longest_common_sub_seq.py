# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/1
Describe:LCR 095. 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：
它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
"""


def longest_common_seq(text1, text2):
    l1 = len(text1)
    l2 = len(text2)
    if l1 <= l2:
        short_s = text1
        long_s = text2
    else:
        short_s = text2
        long_s = text1
    ans = 0
    for i in range(len(short_s)):
        long_s_list = list(long_s)
        cur_cnt = 0
        if short_s[i] in long_s:
            cur_cnt += 1
            pre_char = short_s[i]
        else:
            continue
        for j in range(i + 1, len(short_s)):
            # todo 重复字符不能判断, index会取到前一个字符的索引
            if short_s[j] in long_s_list and long_s_list.index(short_s[j]) > long_s_list.index(pre_char):
                cur_cnt += 1
                long_s_list.pop(long_s_list.index(pre_char))
                pre_char = short_s[j]
        ans = max(cur_cnt, ans)
    return ans


def longest_common_seq_dp(text1, text2):
    """
    dp 动态规划
    :param text1:
    :param text2:
    :return:
    212ms 击败 91.01%使用 Python 的用户
    20.96MB击败 43.82%使用 Python 的用户
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == '__main__':
    t1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    t2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(longest_common_seq(t1, t2))
