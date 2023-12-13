# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/12
Describe:204. 计数质数
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
输入：n = 0
输出：0
输入：n = 1
输出：0
"""


def count_prime(n):
    """超时"""

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 2
        while i * i < num:
            if num % i == 0:
                return False
            i += 1
        return True

    cnt = 0
    for i in range(n):
        if is_prime(i):
            cnt += 1
    return cnt


def count_prime_1(n):
    dp = [1] * n
    cnt = 0
    for i in range(2, n):
        if dp[i] == 1:
            cnt += 1
        if i * i < n:
            j = i * i
            while j < n:
                dp[j] = 0
                j += i
    return cnt


def count_prime_2(n):
    primes = []
    dp = [1] * n
    for i in range(2, n):
        if dp[i] == 1:
            primes.append(i)
            j = 0
            while j < len(primes) and i * primes[j] < n:
                dp[i * primes[j]] = 0
                if i % primes[j] == 0:
                    break
                j += 1
    return len(primes)


if __name__ == '__main__':
    n = 10
    print(count_prime_2(n))
