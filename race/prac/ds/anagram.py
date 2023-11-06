# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/6
Describe: 判断两个长度相等的字符串是否是变位词,即组成单词的字母一样
逐个比较: O(N): n^2
排序再比较
暴力求解,先求解s1的全排列,再看s2是否在s1的全排列中
计数比较
"""


def anagram_sol1(s1, s2):
    """
    逐个比较
    1. s2 存到一个列表
    2. 遍历s1的每个字符
    3. 与s2的列表进行遍历比较
        3.1 找到 列表值置为None
        3.2 没找到 跳出循环
    :param s1:
    :param s2:
    :return:
    """

    list_a = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == list_a[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            list_a[pos2] = None
        else:
            still_ok = False
        pos1 += 1
    return still_ok


def anagram_sol2(s1, s2):
    """
    1. 将s1和s2 转换成列表
    2. 对s1和s2进行排序
    3. 遍历对比相同位置是否相等  \\ 比较两个列表是否相等
    :param s1:
    :param s2:
    :return:
    """
    list_a = list(s1)
    list_b = list(s2)

    list_a.sort()
    list_b.sort()

    pos = 0
    matches = True

    # if list_a != list_b:
    #     matches = False

    while pos < len(list_a) and matches:
        if list_a[pos] == list_b[pos]:
            pos += 1
        else:
            matches = False

    return matches


def anagram_sol3(s1, s2):

    # count_a = {}
    # count_b = {}
    # for item in s1:
    #     if item in count_a.keys():
    #         count_a[item] += 1
    #     else:
    #         count_a[item] = 1
    #
    # for item in s2:
    #     if item in count_b.keys():
    #         count_b[item] += 1
    #     else:
    #         count_b[item] = 1
    #
    # matches = True
    #
    # for k, v in count_a.items():
    #     if k not in count_b.keys() or count_a[k] != count_b[k]:
    #         matches = False
    #         break
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):   # for s in s1: pos = ord(s) - ord('a')
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    matches = True
    while j < 26 and matches:
        if c1[j] == c2[j]:
            j += 1
        else:
            matches = False
            break
    return matches


if __name__ == '__main__':

    a = 'abcd'
    b = 'cadb'
    c = 'abcdfgd'
    d = 'casdgdb'
    print(f"{a}和{b}是否变位词: {anagram_sol1(a, b)}")
    print(f"{c}和{d}是否变位词: {anagram_sol1(c, d)}")

    print(f"{a}和{b}是否变位词: {anagram_sol2(a, b)}")
    print(f"{c}和{d}是否变位词: {anagram_sol2(c, d)}")

    print(f"{a}和{b}是否变位词: {anagram_sol3(a, b)}")
    print(f"{c}和{d}是否变位词: {anagram_sol3(c, d)}")

