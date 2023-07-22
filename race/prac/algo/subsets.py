# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/10/1
Describe:给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
输入：nums = [0]
输出：[[],[0]]
"""


class Solution:

    def subsets(self, nums):
        """
        使用递归
        :param nums:
        :return:
        """
        res = []

        def dfs(temp, index):
            res.append(temp)
            for index in range(index, len(nums)):
                dfs(temp + [nums[index]], index + 1)

        dfs([], 0)
        return res


if __name__ == "__main__":
    sol = Solution()
    tmp_a = [1, 2, 3]
    tmp_b = [0]
    res1 = sol.subsets(tmp_a)
    res2 = sol.subsets(tmp_b)
    print(f"{tmp_a}的子集为:{res1}")
    print(f"{tmp_b}的子集为:{res2}")
