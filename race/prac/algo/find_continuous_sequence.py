# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/2
Describe:输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
示例 1：
输入：target = 9

输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15

输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""


class Solution:

    def find_continuous_sequence(self, target):
        l, r, s, res = 1, 2, 3, []

        while l < r:

            if s == target:
                res.append(list(range(l, r+1)))
            if s < target:
                r += 1
                s += r
            else:
                s -= l
                l += 1

        return res

    def find_continuous_sequence_opt(self, target):
        """
        和为target的递增序列最大长度( n <sqrt(2*target) )==> n*n + 2*n*left = target ==> left=0,n取最大值
        由递增数列n*(left+left+n)/2 = target 推导而来
        再根据这个来滑动选择数列的长度n,由2开始
        :param target:
        :return:
        """

        n = 2
        result = []
        while (n * n // 2) <= target:
            if target % n == 0:
                left = target // n - n // 2
            else:
                left = target // n - n // 2 + 1

            right = left + n - 1
            if (left + right) * n == target * 2:
                result.insert(0, list(range(left, right + 1)))
            n += 1
            print(f"n={n}")
        return result


if __name__ == "__main__":

    sol = Solution()
    temp_nums = [9, 0, 15]
    for num in temp_nums:
        print(sol.find_continuous_sequence(num))
