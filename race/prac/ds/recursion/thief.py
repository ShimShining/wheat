# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/10
Describe: dp  背包问题 weight = 20
item    weight    value
1         2         3
2         3         4
3         4         8
4         5         8
5         9         10

m(i, W)
前i(1<=i<=5)个宝物中,组合不超过W(1<=W<=20)重量.得到的最大价值
m(i, W)应该是m(i-1, W) 和 m(i-1, W-Wi) + vi 两者的最大值
从m(1,1)开始计算到m(5, 20)
m(i, W)
    0                                   i == 0
    0                                   w == 0
    m(i-1, W)                           wi > W
    max{m(i-1, W), m(i-1, W-Wi) + vi}   otherwise
"""
# 物品的重量和价值
tr = [
    None,
    {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}
]
# 背包最大承受重量
m_w = 20


def thief(t, max_weight):
    # 初始化二维表格m[(i,w)]
    # value表示当前i个宝物,最大重量w的组合,所得到的最大价值
    # 当i什么都不取或者w=0,价值均为0
    m = {(i, w): 0 for i in range(len(t)) for w in range(max_weight + 1)}

    # 逐个填写二维表格
    for i in range(1, len(t)):
        for w in range(1, max_weight + 1):
            if t[i]['w'] > w:    # 装不下第i个宝物
                m[(i, w)] = m[(i-1, w)]   # 不装第i个宝物
            else:
                # 装得下,第i个宝物, 取装和不装第i个宝物的最大价值
                m[(i, w)] = max(m[(i-1, w)], t[i]['v'] + m[(i-1), w - t[i]['w']])

    return m[(len(t) - 1, max_weight)]


# 宝物的重量和价值
tr2 = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}
m = dict()   # 初始化记忆化表格 最大承重,key是不同(组合宝物,重量)的元组, value是对应的最大价值


def thief_recursion(tr: set, w):
    if tr == set() or w == 0:
        m[(tuple(tr), w)] = 0    # 变成tuple是因为key需要不可变类型,集合是可变类型
        return 0
    if (tuple(tr), w) in m:
        return m[(tuple(tr), w)]
    else:
        v_max = 0
        for t in tr:
            if t[0] <= w:
                # 逐个从集合中去掉某个宝物,递归调用
                # 选出所有价值中最大值
                v = thief_recursion(tr-{t}, w-t[0]) + t[1]
                v_max = max(v_max, v)
        m[(tuple(tr), w)] = v_max
        return v_max


if __name__ == '__main__':
    print(thief(tr, 20))
    print(thief_recursion(tr2, 20))


