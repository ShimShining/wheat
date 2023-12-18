# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/18
Describe: 吃burger1 需要m分钟, 吃Burger2需要n分钟
给定总时间,在不浪费时间的前提下,可以吃得最多的汉堡
"""


def max_eat_burgers(burger1, burger2, total_time):
    if total_time == 0:
        return 0
    if total_time < 0:
        return -1
    burger1_cnt = max_eat_burgers(burger1, burger2, total_time - burger1)
    burger2_cnt = max_eat_burgers(burger1, burger2, total_time - burger2)
    # 如果都是-1 那就只能返回-1了,这个1就不能加了
    if burger1_cnt == -1 and burger2_cnt == -1:
        return -1
    return max(burger1_cnt, burger2_cnt) + 1


def max_eat_burgers_cache(burger1, burger2, total_time, cache):
    if total_time == 0:
        return 0
    if total_time < 0:
        return -1
    if cache[total_time] != -2:
        return cache[total_time]
    burger1_cnt = max_eat_burgers_cache(burger1, burger2, total_time-burger1, cache)
    burger2_cnt = max_eat_burgers_cache(burger1, burger2, total_time- burger2, cache)
    if burger1_cnt == -1 and burger2_cnt == -1:
        cache[total_time] = -1
        return -1
    cache[total_time] = max(burger2_cnt, burger1_cnt) + 1
    return cache[total_time]


if __name__ == '__main__':
    m, n, tt = 3, 5,  55  # 4, 9, 54 == 11  4, 9, 22 == 3  3, 5, 54  == 18   3, 5,  55 == 17
    print(max_eat_burgers(m, n, tt))
    dp = [-2] * (tt+1)
    print(max_eat_burgers_cache(m, n, tt, dp))
