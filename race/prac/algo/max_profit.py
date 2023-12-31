# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/7
Describe:假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少?

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

0 <= 数组长度 <= 10^5
"""


class Solution:

    def max_profit(self, nums: list):
        cost, profit = float("inf"), 0
        for price in nums:
            cost = min(cost, price)
            profit = max(profit, price - cost)

        # l = len(prices)
        # for i in range(l-1):
        #     for j in range(i+1,l):
        #         profit = max(prices[j]-prices[i], profit)
        # return profit

        return profit


if __name__ == "__main__":
    sol = Solution()
    tmp_list = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
    for item in tmp_list:
        res = sol.max_profit(item)
        print(res)
