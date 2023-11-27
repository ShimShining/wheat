# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/10
Describe: 分治策略 贪心策略
找零
"""


def coins_num(coin_vals: list, change):
    """贪心策略找零: 每次都用最大的面值去找(对于正常货币体系可以,但是特殊的不行,比如[1, 5, 10, 21, 25])"""
    coins = coin_vals[:]
    c = 0
    res = []
    while change > 0:
        max_coin = max(coins)
        if change - max_coin >= 0:
            c += 1
            change -= max_coin
            res.append((c, max_coin))
        else:
            coins.remove(max_coin)
    return c, res


def num_coins(coin_vals, change):
    """
    直接递归,耗时特别高
    :param coin_vals:
    :param change:
    :return:
    """
    min_coins = change
    if change in coin_vals:
        return 1
    for i in [c for c in coin_vals if c <= change]:
        num_c = 1 + num_coins(coin_vals, change - i)
        if num_c < min_coins:
            min_coins = num_c
    return min_coins


def num_coins_opt(coin_vals, change, know_result):
    """
    记录递归的中间结果
    有则查表(类似缓存的技术)
    :param coin_vals:
    :param change:
    :param know_result:
    :return:
    """
    min_coins = change
    if change in coin_vals:
        know_result[change] = 1
        return 1
    elif know_result[change] > 0:
        return know_result[change]
    for i in [c for c in coin_vals if c <= change]:
        num_c = 1 + num_coins_opt(coin_vals, change - i, know_result)
        if num_c < min_coins:
            min_coins = num_c
            know_result[change] = min_coins
    return min_coins


def num_coins_dp(coin_vals, change, min_coins):
    """
    动态规划
    :return:
    """
    for cents in range(1, change + 1):

        coin_count = cents
        for j in [c for c in coin_vals if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1

        min_coins[cents] = coin_count

    return min_coins[change]


def num_coins_dp_opt(coin_vals, change, min_coins, coins_used):
    """
    动态规划 优化
    :return:
    """
    for cents in range(1, change + 1):

        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_vals if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j

        min_coins[cents] = coin_count
        coins_used[cents] = new_coin

    return min_coins[change]


def print_coins(coin_used, change):
    coin = change
    while coin > 0:
        this_coin = coin_used[coin]
        print(f"this_coin=={this_coin}")
        coin = coin - this_coin


if __name__ == '__main__':
    print(coins_num([1, 5, 10, 25], 63))
    # print(num_coins([1, 5, 10, 25], 63))

    # print(num_coins_opt([1, 5, 10, 21, 25], 63, [0] * 64))

    # print(num_coins_dp([1, 5, 10, 21, 25], 63, [0] * 64))

    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt + 1)
    coin_cnt = [0] * (amnt + 1)
    print(num_coins_dp_opt(clist, amnt, coin_cnt, coins_used))
    print(coins_used)
    print("+++++++++++")
    print_coins(coins_used, amnt)

    print(coins_used)
