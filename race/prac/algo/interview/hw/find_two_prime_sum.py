# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/12
Describe:HJ60 查找组成一个偶数最接近的两个素数
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，
本题目要求输出组成指定偶数的两个素数差值最小的素数对。
输入描述：
输入一个大于2的偶数
输入：
20
输出：
7
13
输入：
4
输出：
2
2
"""


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def find_two_prime_sum(arr):
    n = int(arr[0])
    left, right = n // 2, n // 2
    while right < n:
        if is_prime(left) and is_prime(right):
            return left, right
        left -= 1
        right += 1


if __name__ == '__main__':
    a = ['20']
    print(find_two_prime_sum(a))
