# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/15
Describe:最小排列,给定一个数字，请编写一个函数，求出绝对值最小的组合。
备注：组合时0不可排在前面。

示例：
输入：312，输出：123
输入：-20，输出：-20
题目难度：中等
"""
import itertools


def min_permutation(n: int) -> int:

    str_n = str(abs(n))
    min_res = abs(n)
    tmp = itertools.permutations(str_n, len(str_n))
    for item in tmp:
        num = int("".join(item))
        if len(str(num)) == len(str_n):
            if n > 0:
                min_res = min(min_res, num)
            else:
                min_res = max(min_res, num)

    if n >= 0:
        return min_res
    return -min_res


def min_permutation_oth(n: int) -> int:
    s = str(n)
    res = []
    tmp = 0
    for i in s:
        if i == "0":
            tmp += 1
        elif i.isdigit():
            res.append(i)
    if n >= 0:
        res.sort()
        res.insert(1, tmp * "0")
        return int(''.join(res))
    else:
        res.sort(reverse=True)
        return int('-' + ''.join(res) + tmp*"0")


if __name__ == "__main__":
    assert min_permutation(312) == 123
    assert min_permutation(29394) == 23499
    assert min_permutation(-29394) == -99432
    assert min_permutation(-20) == -20
    assert min_permutation(0) == 0
    assert min_permutation(2000000) == 2000000
    assert min_permutation(2000020) == 2000002
    assert min_permutation(-2000000) == -2000000

    assert min_permutation_oth(312) == 123
    assert min_permutation_oth(29394) == 23499
    assert min_permutation_oth(-29394) == -99432
    assert min_permutation_oth(-20) == -20
    assert min_permutation_oth(0) == 0
    assert min_permutation_oth(2000000) == 2000000
    assert min_permutation_oth(2000020) == 2000002
    assert min_permutation_oth(-2000000) == -2000000
