# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/27
Describe:
dp  背包问题 weight = 20
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



