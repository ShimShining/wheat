# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/8/30
Describe:一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""


class Solution:
    """
    35 / 35 个通过测试用例
    状态：通过
    执行用时: 8308 ms
    内存消耗: 15.8 MB
    """

    def singleNumbers(self, nums):

        res = []
        # for item in nums:
        for item in set(nums):
            if nums.count(item) == 1:
                res.append(item)

        return res


class SingleNumbers:
    """
    35 / 35 个通过测试用例
    状态：通过
    执行用时: 40 ms
    内存消耗: 15.8 MB
    """

    def singleNumbers(self, nums):

        x, y, n, m = 0, 0, 0, 1

        # 全组异或
        for num in nums:
            n ^= num
            print(n)

        # 找出二进制为 1 的那一位
        while n & m == 0:
            m <<= 1

        # 利用 m 进行分组，分别进行全组异或
        for num in nums:
            if num & m:
                x ^= num
            else:
                y ^= num
        return x, y


if __name__ == "__main__":
    sn = SingleNumbers()
    temp = [4, 3, 4, 6]
    res = sn.singleNumbers(temp)
    print(f"res is {res}")
