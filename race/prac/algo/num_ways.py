# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/9/16
Describe:青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
输入：n = 2
输出：2

输入：n = 7
输出：21
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
"""


class Solution(object):
    def num_ways_rec(self, n):
        """
        递归方式求解,耗时不通过
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n <= 2:
            return n
        return self.num_ways_rec(n - 2) + self.num_ways_rec(n - 1) % 1000000007

    def num_ways_dp(self, n):
        """
        dp状态转移
        :param n:
        :return:
        """
        dp = [0] * (n + 2)  # n=0的时候用到了index=1 所以保证dp至少有两个
        dp[0] = 1
        dp[1] = 1
        if n <= 1:
            return dp[n]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def num_ways(self, n):
        """
        51 / 51 个通过测试用例
        状态：通过
        执行用时: 12 ms
        内存消耗: 13.3 MB
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n <= 2:
            return n
        first = 1
        sec = 2
        for i in range(3, n + 1):
            tmp = first + sec
            first = sec
            sec = tmp
        return tmp


if __name__ == "__main__":
    sol = Solution()
    tmp_n = [0, 2, 7]
    for n in tmp_n:
        res = sol.num_ways(n)
        res1 = sol.num_ways_rec(n)
        res2 = sol.num_ways_dp(n)
        print(f"num_ways:{n}阶台阶有{res}种方式到达")
        print(f"num_ways_rec:{n}阶台阶有{res1}种方式到达")
        print(f"num_ways_dp:{n}阶台阶有{res2}种方式到达")

