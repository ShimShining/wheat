# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/10
Describe: 122. 买卖股票的最佳时机 II
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。
你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润 。
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     总利润为 4 。
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。
"""


def max_profit(prices):
    """贪心算法"""
    max_p = 0
    n = len(prices)
    for i in range(1, n):
        max_p += max(0, prices[i] - prices[i - 1])
    return max_p


def max_profit_dp(prices):
    n = len(prices)
    dp = [[0] * 2 for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
    return dp[n - 1][0]


def max_profit_2(prices):
    """
    只需要将 dp[i−1][0]\textit{dp}[i-1][0]dp[i−1][0] 和 dp[i−1][1]\
    {dp}[i-1][1]dp[i−1][1] 存放在两个变量中，通过它们计算出 dp[i][0]\
    {dp}[i][0]dp[i][0] 和 dp[i][1]\textit{dp}[i][1]dp[i][1] 并存回对应的变量，
    以便于第 i+1i+1i+1 天的状态转移即可。
    :param prices:
    :return:
    """
    p = 0
    hold = -prices[0]
    pre_p = p
    pre_h = hold
    for i in range(1, len(prices)):
        p = max(pre_p, pre_h + prices[i])
        hold = max(pre_h, pre_p - prices[i])

        pre_p = p
        pre_h = hold
    return pre_p


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    print(max_profit_dp(prices))
