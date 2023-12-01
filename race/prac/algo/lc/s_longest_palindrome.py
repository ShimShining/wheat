# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/1
Describe:409. 最长回文串
给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。

在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。
输入:s = "abccccdd"
输出:7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
输入:s = "a"
输出:1
示例 3：

输入:s = "aaaaaccc"
输出:7
"""
from collections import Counter


def longest_palindrome(s: str):
    """
    :param s:
    :return:
    12ms 击败 98.72%使用 Python 的用户
    13.06MB 击败 41.88%使用 Python 的用户
    """
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    print(d)
    for v in d.values():
        ans += v // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans


def longest_palindrome_1(s: str):
    c = Counter(s)
    ans = 0
    for v in c.values():
        ans += v // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans


def longest_palindrome_2(s: str):
    """
    :param s:
    :return:
    16ms 击败 94.44%使用 Python 的用户
    13.08MB 击败 35.04%使用 Python 的用户
    """
    c = Counter(s)
    ans = 0
    add_one = False
    for v in c.values():
        if v % 2 == 0:
            ans += v
        else:
            add_one = True
            ans += (v - 1)
    return ans + int(add_one)


def longest_palindrome_3(s):
    """
    :type s: str
    :rtype: int
    """
    hash = [0] * 58
    # 初始化结果值
    res = 0
    # 统计字符串中的每个字符出现的次数
    for i in s:
        hash[ord(i) - ord('A')] += 1
    # 开始遍历
    for i in range(58):
        # 对当前字符成对的个数
        pairCnt = hash[i] // 2
        # 更新当前的结果值
        res += pairCnt * 2
        # 更新当前剩余的字符数
        hash[i] -= pairCnt * 2
    # 如果存在剩下的字符
    if sum(hash) != 0:
        return res + 1
    # 如果全是成对的字符
    else:
        return res


if __name__ == '__main__':
    s = "abccccdd"
    print(longest_palindrome(s))
