# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/30
Describe: 给定长度为2n的data数组,data[i]表示一台服务器的capacity
其中每两台服务器可以凑成一对,现在要关闭每一对中的一台服务器
关闭小的cost + 1,关闭大的cost=0
给定数组data 和k, 返回关闭服务器后,还在运行的服务capacity之和大于等于k的最小cost
示例
data= [1,2,3,5,7,8] k=14
result:[1, 8],[2,3], [5,7]
关闭1,3,7 cost=1
"""

