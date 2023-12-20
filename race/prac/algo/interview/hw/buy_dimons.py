# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/19
Describe: 宝石购买
"""


def buy_dimons(arr):
    if len(arr) < 3:
        return 0
    n = int(arr[0][0])
    games = [int(arr[i][0]) for i in range(1, n + 1)]
    money = int(arr[-1][0])
    cnt = 0
    for i in range(len(games) - 1):
        cost = games[i]
        if cost > money:
            continue
        dis = 1
        for j in range(i + 1, len(games)):
            cost += games[j]
            if cost <= money:
                dis += 1
                cnt = max(cnt, dis)
            else:
                break
    return cnt


def buy_dimons_1(arr):
    if len(arr) < 3:
        return 0
    n = int(arr[0][0])
    games = [int(arr[i][0]) for i in range(1, n + 1)]
    money = int(arr[-1][0])
    cnt = 0
    start = 0
    cost = games[start]
    for end in range(1, len(games)):

        while cost > money and start <= end:
            cost -= games[start]
            start += 1
        cnt = max(cnt, end - start)
        cost += games[end]
    return cnt


if __name__ == '__main__':
    arr = [['7'], ['8'], ['4'], ['6'], ['3'], ['1'], ['6'], ['7'], ['10']]
    arr2 = [['7'], ['11'], ['11'], ['11'], ['11'], ['11'], ['61'], ['71'], ['10']]
    print(buy_dimons(arr))
    print(buy_dimons_1(arr))
