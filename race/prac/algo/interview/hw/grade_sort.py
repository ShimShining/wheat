# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/9
Describe:HJ68 成绩排序
给定一些同学的信息（名字，成绩）序列，请你将他们的信息按照成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。
例示：
jack      70
peter     96
Tom       70
smith     67
从高到低  成绩
peter     96
jack      70
Tom       70
smith     67
从低到高
smith     67
jack      70
Tom       70
peter     96
输入描述：
第一行输入要排序的人的个数n，第二行输入一个整数表示排序的方式，之后n行分别输入他们的名字和成绩，以一个空格隔开
输出描述：
按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开
输入
3
0
fang 90
yang 50
ning 70
输出
fang 90
ning 70
yang 50
"""


def grade_sort(arr):
    sort_flag = bool(int(arr[1][0]))
    g = arr[2:]
    if not g or len(g) == 1:
        return g
    g = sorted(g, key=lambda x: int(x[1]), reverse=not sort_flag)
    return g


if __name__ == '__main__':
    arr = [['3'], ['1'], ['fang', '90'], ['jack', 70], ['yang', '50'], ['ning', '70']]
    print(grade_sort(arr))
