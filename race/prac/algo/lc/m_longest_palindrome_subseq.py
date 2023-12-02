# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/1
Describe:516. 最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb"

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb"
"""


def longest_palindrome_subseq(s):
    """
    动态规划
    :param s:
    :return:
    时间 808ms 击败 85.71%使用 Python 的用户
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(
                    dp[i + 1][j], dp[i][j - 1]
                )
    return dp[0][-1]


def longest_palindrome_subseq_dfs(s):
    def dfs(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return dfs(i + 1, j - 1) + 2
        return max(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, len(s) - 1)


def dp_longest_padlindrome_sub_str(s):
    """
    将s反转,问题转换为求两个字符串的最长公共子序列
    :param s:
    :return:
    """
    n = len(s)
    s2 = s[::-1]
    dp = [[0] * (n + 1) for _ in range(n+ 1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]


if __name__ == '__main__':
    s = "cbbcd"
    print(longest_palindrome_subseq(s))
    print(dp_longest_padlindrome_sub_str(s))
