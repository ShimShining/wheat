# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/25
Describe: bytedance 面试题
找出重复的数字, 组成一个数组
输入: [1, 2, 3, 4, 2, 5, 3]
输出: [2, 3]
"""


def find_sub_repeat_arr(arr):
    if not arr or len(arr) == 1:
        return []
    count = dict()
    for val in arr:
        if val not in count:
            count[val] = 1
        else:
            count[val] += 1
    res = []
    for k in count.keys():
        if count[k] > 1:
            res.append(k)
    return res


def find_sub_repeat_arr_1(arr):
    if not arr or len(arr) == 1:
        return []
    res = []
    count = dict()
    for val in arr:
        if val not in count:
            count[val] = 1
        else:
            count[val] += 1
            if val not in res:
                res.append(val)
    return res


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 2, 5, 3]
    print(find_sub_repeat_arr(arr))
    print(find_sub_repeat_arr_1(arr))
