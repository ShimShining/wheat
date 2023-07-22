# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/8/31
Describe:在一个数组 nums 中除一个数字只出现一次之外，
其他数字都出现了三次。请找出那个只出现一次的数字。
输入：nums = [3,4,3,3]
输出：4
输入：nums = [9,1,7,9,7,9,7]
输出：1
"""


class Solution:

    def singleNumber(self, nums) -> int:
        """
        32 / 32 个通过测试用例
        状态：通过
        执行用时: 2076 ms
        内存消耗: 15.8 MB
        """

        for item in set(nums):
            if (nums.count(item) == 1):
                return item

    def single_number_a(self, nums):
        """
        32 / 32 个通过测试用例
        状态：通过
        执行用时: 200 ms
        内存消耗: 15.8 MB
        :param nums:
        :return:
        """
        bit_mask = 1 << 31
        res = 0

        for j in range(32):

            bit_sum = 0
            for num in nums:

                if bit_mask & num: bit_sum += 1

            res = (res << 1) + bit_sum % 3
            bit_mask >>= 1

        return res

    def single_number(self, nums):
        """
        32 / 32 个通过测试用例
        状态：通过
        执行用时: 228 ms
        内存消耗: 15.7 MB
        :param nums:
        :return:
        """
        max_value = max(nums)
        high = self.high_bit(max_value)
        bit_mask = 1 << high
        res = 0

        for j in range(high+1):

            bit_sum = 0
            for num in nums:

                if bit_mask & num: bit_sum += 1

            res = (res << 1) + bit_sum % 3
            bit_mask >>= 1

        return res

    def low_bit(self, num):
        return num & (-num)

    def high_bit(self, num):
        p = self.low_bit(num)
        while(p != num):
            num -= p
            p = self.low_bit(num)
        return len(bin(p)) - 2

    def single_number_b(self, nums):

        nums.sort()
        length = len(nums)
        i = 0
        while i < length - 3:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 3
        return nums[-1]

    def single_num_c(self, nums):
        """
        32 / 32 个通过测试用例
        状态：通过
        执行用时: 36 ms
        内存消耗: 13.9 MB
        :param nums:
        :return:
        """
        a = 0
        b = 0

        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a

        return a


if __name__ == "__main__":
    temp_a = [3, 4, 3, 3]
    temp_b = [9, 1, 7, 9, 7, 9, 7]
    sol = Solution()
    print(sol.single_number(temp_a))
    assert sol.single_number(temp_a) == 4
    assert sol.single_number(temp_b) == 1
