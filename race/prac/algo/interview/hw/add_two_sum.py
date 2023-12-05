# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/5
Describe: 两数之和
"""


def add_two_sum(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i, j]


def add_two_sum_1(numbers, target):
    n = len(numbers)
    for i in range(n):
        if target - numbers[i] in numbers[i + 1:]:
            return [i, numbers[i + 1:].index(target - numbers[i]) + i + 1]


def add_two_sum_2(numbers, target):
    hash_rec = dict()
    for i, num in enumerate(numbers):
        if target - numbers[i] in hash_rec:
            return [i, hash_rec[target - num]]
        hash_rec[numbers[i]] = i
