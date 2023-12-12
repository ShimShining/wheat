# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/12
Describe:
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，
挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，
而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，
当然密码学会希望你寻找出“最佳方案”。
输入:
有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。
输出:
输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。

输入说明
1 输入一个正偶数 n
2 输入 n 个整数
输入：
4
2 5 6 13
输出：
2
输入：
2
3 6
输出：
0
"""


def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def match_prime_partner(evens, odd, visited, choose):
    for i, even in enumerate(evens):
        if is_prime(even + odd) and not visited[i]:
            visited[i] = True
            if choose[i] == 0 or match_prime_partner(evens, choose[i], visited, choose):
                choose[i] = odd
                return True
    return False


def find_prime_partner(arr):
    n = arr[0][0]
    nums = list(map(int, arr[1]))
    print(nums)
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    choose = [0] * len(evens)
    res = 0
    for odd in odds:
        visited = [0] * len(evens)
        if match_prime_partner(evens, odd, visited, choose):
            res += 1
    return res


if __name__ == '__main__':

    arr = [['4'], ['2', '5', '6', '13']]
    print(find_prime_partner(arr))


