# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: 任意进制转换
"""


def atoi_digit(char):
    if '0' <= char <= '9':
        return ord(char) - ord('0')
    return 10 + ord(char) - ord('A')


def itoa_digit(num):
    if num < 10:
        return chr(num + ord('0'))
    return chr(num - 10 + chr('A'))


def atoi(a, M):
    """
    M 进制转十进制
    :param a:
    :param M:
    :return:
    """
    if not a:
        return 0
    return M * atoi(a[:-1], M) + atoi_digit(a[-1])


def itoa(i, N):
    """
    十进制转N进制
    :param i:
    :param N:
    :return:
    """
    if not i:
        return ''
    return itoa(i // N, N) + itoa_digit(i % N)


def transfer(s, M, N):
    return itoa(atoi(s, M), N)


if __name__ == '__main__':
    M, N = 8, 16
    num = "111"
    print(transfer(num, M, N))
