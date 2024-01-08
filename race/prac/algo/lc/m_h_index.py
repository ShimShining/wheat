# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2024/1/8
Describe: 274. H 指数
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，
并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5
输入：citations = [1,3,1]
输出：1
"""


def h_index(citations: list) -> int:
    """
    :param citations:
    :return:
    36 ms 击败 93.81% 使用 Python3 的用户
    """
    n = len(citations)
    citations.sort(reverse=True)
    index = 0
    for i in range(n):
        if citations[i] >= i + 1:
            index += 1
    return index


def h_index_1(citations: list) -> int:
    n = len(citations)
    index = 0
    arr = [0] * (n + 1)
    for i in citations:
        if i >= n:
            arr[n] += 1
        else:
            arr[i] += 1
    for i in range(n, -1, -1):
        index += arr[i]
        if index >= i:
            return i
    return 0


def h_index_2(citations: list) -> int:
    left, right = 0, len(citations)
    while left < right:
        # +1 防止死循环
        mid = (left + right + 1) >> 1
        cnt = 0
        for v in citations:
            if v >= mid:
                cnt += 1
        if cnt >= mid:
            # 要找的答案在 [mid,right] 区间内
            left = mid
        else:
            # 要找的答案在 [0,mid) 区间内
            right = mid - 1
    return left


if __name__ == '__main__':
    citations = [0, 1, 0]
    print(h_index(citations))
