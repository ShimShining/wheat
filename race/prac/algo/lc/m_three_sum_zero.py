# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/3
Describe:LCR 007. 三数之和
给定一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

输入：nums = []
输出：[]

输入：nums = [0]
输出：[]
"""


def three_sum(nums):
    """
    超出时间限制
    :param nums:
    :return:
    """
    res = []
    if not nums or len(nums) < 3:
        return res
    n = len(nums)
    nums.sort()
    for i in range(n):
        for j in range(i + 1, n):
            if -(nums[i] + nums[j]) in nums[j + 1:]:
                tmp = [nums[i], nums[j], -(nums[i] + nums[j])]
                if tmp not in res:
                    res.append(tmp)
    return res


def three_sum_1(nums):
    """
    :param nums:
    :return:
    440ms 击败 56.86%使用 Python 的用户
    18.50MB 击败 47.06%使用 Python 的用户
    """
    res = []
    if not nums or len(nums) < 3:
        return res
    n = len(nums)
    nums.sort()
    # 枚举 a
    for i in range(n):
        # 需要和上一次枚举的数不相同
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # c 对应的指针初始指向数组的最右端
        k = n - 1
        target = -nums[i]
        # 枚举 b
        for j in range(i + 1, n):
            # 需要和上一次枚举的数不相同
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # 需要保证 b 的指针在 c 的指针的左侧
            while j < k and nums[j] + nums[k] > target:
                k -= 1
            # 如果指针重合，随着 b 后续的增加
            # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
            if j == k:
                break
            if nums[j] + nums[k] == target:
                res.append([nums[i], nums[j], nums[k]])
    return res


if __name__ == '__main__':
    nums = [1, 2, -2, -1]
    print(three_sum(nums))
