# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2024/1/14
Describe:134. 加油站
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，
否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
示例 1:
输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引

示例 2:

输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
"""


def can_complete_circuit(gas, cost):
    """180ms 击败11.22%使用 Python3 的用户"""
    n = len(gas)
    start = 0

    while start < n:
        end = start + 1
        total_gas = gas[start]
        while total_gas >= cost[(end % n) - 1]:
            total_gas -= cost[(end % n) - 1]
            total_gas += gas[end % n]
            if end % n == start:
                return start
            end += 1

        start = end
        if start >= n:
            return -1


def can_complete_circuit_1(gas, cost):
    """124ms击败42.13%使用 Python3 的用户"""
    n = len(gas)
    i = 0
    while i < n:

        sum_gas = 0
        sum_cost = 0
        cnt = 0
        while cnt < n:
            j = (i + cnt) % n
            sum_gas += gas[j]
            sum_cost += cost[j]
            if sum_gas < sum_cost:
                break
            cnt += 1
        if cnt == n:
            return i
        else:
            i = i + cnt + 1
    return -1


def can_complete_circuit_2(gas, cost):
    n = len(gas)
    over = 0
    min_index = -1
    min_cost = float('inf')
    for i in range(n):
        over += gas[i] - cost[i]
        if over < min_cost and over < 0:
            min_cost = over
            min_index = i
    if over < 0:
        return -1
    return (min_index + 1) % n


def can_complete_circuit_3(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    n = len(gas)
    total, start = 0, 0
    for i in range(n):
        total += gas[i] - cost[i]
        if total < 0:
            start = i + 1
            total = 0
    return start


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    gas1 = [2, 3, 4]
    cost1 = [3, 4, 3]
    print(can_complete_circuit(gas1, cost1))
