# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/9
Describe:NC37 合并区间
给出一组区间，请合并所有重叠的区间。 请保证合并后的区间按区间起点升序排列。
数据范围：区间组数 ，区间内 的值都满足 要求：空间复杂度 ，时间复杂度 进阶：空间复杂度 ，时间复杂度
示例1
输入
[[10,30],[20,60],[80,100],[150,180]]
输出
[[10,60],[80,100],[150,180]]
示例2
输入
[[0,10],[10,20]]
输出
[[0,20]]
"""


class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b


def merge(intervals: list):
    if not intervals:
        return intervals
    intervals = sorted(intervals, key=lambda x: x.start)
    res = []
    n = len(intervals)
    res.append(intervals[0])
    count = 0
    for i in range(1, n):
        origin = res[count]
        cur = intervals[i]
        if cur.start > origin.end:
            res.append(cur)
            count += 1
        else:
            res.pop()
            max_end = max(cur.end, origin.end)
            res.append(Interval(origin.start, max_end))
    return res


def merge_1(intervals: list):
    if not intervals or len(intervals) == 1:
        return intervals
    n = len(intervals)
    res = []
    intervals = sorted(intervals, key=lambda x:x.start)
    res.append(intervals[0])
    for i in range(1, n):
        pre = res.pop()
        cur = intervals[i]
        if cur.start > pre.end:
            res.append(pre)
            res.append(cur)
        else:
            max_e = max(pre.end, cur.end)
            res.append(Interval(pre.start, max_e))
    return res


if __name__ == '__main__':
    ls = [Interval(10, 30), Interval(20, 60), Interval(80, 100), Interval(150, 180)]
    r = merge(ls)
    print(type(r))
    for item in r:
        print(item)
        print(item.start, item.end)
