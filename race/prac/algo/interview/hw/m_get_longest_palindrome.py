# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/11
Describe: NC17 最长回文子串
对于长度为n的一个字符串A（仅包含数字，大小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。
数据范围： 1≤n≤1000
要求：空间复杂度 O(1)，时间复杂度 O(n 2)
进阶:  空间复杂度 O(n)，时间复杂度 O(n)
输入：
"ababc"
返回值：
3
说明：
最长的回文子串为"aba"与"bab"，长度都为3
输入：
"abbba"
返回值：
5
输入：
"b"
返回值：
1
"""


def get_longest_palindrome(A: str) -> int:
    n = len(A)
    dp = [[0] * n for i in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if A[i] == A[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]


def get_longest_palindrome_dfs(A: str) -> int:
    def dfs(s, i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return dfs(s, i + 1, j - 1) + 2
        return max(dfs(s, i + 1, j), dfs(s, i, j - 1))

    return dfs(A, 0, len(A) - 1)


def get_longest_palindrome_dp_2(A: str) -> int:
    s2 = A[::-1]
    n = len(A)
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]


if __name__ == '__main__':
    s = "ccbcabaabba"
    print(get_longest_palindrome_dfs(s))
    print(get_longest_palindrome_dp_2(s))
