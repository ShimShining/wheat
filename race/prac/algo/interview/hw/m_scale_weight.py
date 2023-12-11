# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/11
Describe:HJ41 称砝码
现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
输入描述：
对于每组测试数据：
第一行：n --- 砝码的种数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])
输出描述：
利用给定的砝码可以称出的不同的重量数
注：
称重重量包括 0
输入：
2
1 2
2 1
输出：
5
说明：
可以表示出0，1，2，3，4五种重量。
"""


def scale_weight(arr):
    """超时"""
    weights = arr[1]
    nums = arr[2]
    n = len(arr[1])
    for i in range(n):
        weights.extend([int(weights[i])] * (int(nums[i]) - 1))
    for i in range(len(weights)):
        weights[i] = int(weights[i])
    print(weights)
    weights.sort()
    length = len(weights)
    res = set()
    path = []
    visited = [False] * length

    def trace(w, k):
        if k == length:
            res.add(sum(path))
            return
        for i in range(len(w)):
            if i > 0 and w[i] == w[i - 1] and not w[i - 1]:
                continue
            if not visited[i]:
                res.add(sum(path))
                visited[i] = True
                path.append(weights[i])
                trace(weights, k + 1)
                path.pop()
                visited[i] = False

    trace(weights, 0)
    return len(res)


def scale_weight_1(arr):
    weights = arr[1]
    nums = arr[2]
    n = len(arr[1])
    for i in range(n):
        weights.extend([int(weights[i])] * (int(nums[i]) - 1))
    for i in range(len(weights)):
        weights[i] = int(weights[i])
    res = {0}
    for i in weights:
        for j in list(res):
            res.add(i + j)
    return len(res)


if __name__ == '__main__':
    a = [['2'], ['1', '2'], ['2', '1']]
    a2 = [["1"], ['75'], ['5']]
    # print(scale_weight(a))
    print(scale_weight_1(a))
