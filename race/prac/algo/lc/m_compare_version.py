# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/4
Describe: 165. 比较版本号
给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。
每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，
以此类推。例如，2.5.33 和 0.1 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。
也就是说，修订号 1 和修订号 001 相等 。
如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，
因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。
返回规则如下：

如果 version1 > version2 返回 1，
如果 version1 < version2 返回 -1，
除此之外返回 0
输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"
输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有指定下标为 2 的修订号，即视为 "0"
输入：version1 = "0.1", version2 = "1.1"
输出：-1
解释：version1 中下标为 0 的修订号是 "0"，version2 中下标为 0 的修订号是 "1" 。0 < 1，所以 version1 < version2

1 <= version1.length, version2.length <= 500
version1 和 version2 仅包含数字和 '.'
version1 和 version2 都是 有效版本号
version1 和 version2 的所有修订号都可以存储在 32 位整数 中
"""
from itertools import zip_longest


def compare_version(version1, version2):
    """
    :param version1:
    :param version2:
    :return:
    12ms 击败 96.23%使用 Python 的用户
    13.23MB 击败 13.21%使用 Python 的用户
    """

    v1_list = version1.split(".")
    v2_list = version2.split(".")
    n = max(len(v1_list), len(v2_list))

    v1_sum = 0
    v2_sum = 0
    for i in range(n):
        if len(v1_list) > i:
            v1_sum += int(v1_list[i]) * pow(10, n - i - 1)
        if len(v2_list) > i:
            v2_sum += int(v2_list[i]) * pow(10, n - i - 1)
        # 在高位进行熔断,不然低位溢出会有问题 2.5.33和2.6.0(计算完的话v1=283,v2=260 ; 实际在第二位版本号就已经比出大小了, v2>v1)
        if v1_sum != v2_sum:
            return 1 if v1_sum > v2_sum else -1
    return 0


def compare_version_1(version1, version2):
    """
    :param version1:
    :param version2:
    :return:
    44ms 击败 54.46%使用 Python3 的用户
    """
    for v1, v2 in zip_longest(version1.split("."), version2.split("."), fillvalue=0):
        x, y = int(v1), int(v2)
        if x != y:
            return 1 if x > y else -1
    return 0


def compare_version_3(version1, version2):
    """
    双指针
    :param version1:
    :param version2:
    :return:
    36ms 击败 91.29%使用 Python3 的用户
    16.11MB 击败 15.74%使用 Python3 的用户
    """
    n, m = len(version1), len(version2)
    i, j = 0, 0
    while i < n or j < m:
        x = 0
        while i < n and version1[i] != ".":
            x = x * 10 + ord(version1[i]) - ord('0')
            i += 1
        i += 1
        y = 0
        while j < m and version2[j] != ".":
            y = y * 10 + ord(version2[j]) - ord('0')
            j += 1
        j += 1
        if x != y:
            return 1 if x > y else -1
    return 0


if __name__ == '__main__':
    v1 = "2.5.33"
    v2 = "2.6.0"
    print(compare_version(v1, v2))


