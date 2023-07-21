# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/7
Describe:腾讯音乐测试二面编程题
给定三个数,判定是否能组成三角形,如果能组成,返回类型
不能组成:返回-1
能组成,返回三角形类型(普通,等腰,等边),0
示例:输入,2,3,4
输出: '普通', 0
"""


def judge_triangle(arr):
    length = len(arr)
    min_len = min(arr)
    if length != 3 or min_len < 0:
        return -1
    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[i] + arr[j] <= arr[3 - i - j]:  # 此条件已覆盖到0,0,0
                return -1

    if len(set(arr)) == 3:
        return '普通', 0
    if len(set(arr)) == 2:
        return '等腰', 0
    if len(set(arr)) == 1:
        return '等边', 0


if __name__ == "__main__":

    temp = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [2, 2, 3], [2, 2, 2], [2, 2, 1], [0, 0, 0], [1, 2], [-1, 2, 3]]

    for elem in temp:
        res = judge_triangle(elem)
        print(res)
