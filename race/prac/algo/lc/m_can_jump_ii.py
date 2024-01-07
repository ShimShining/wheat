# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2024/1/7
Describe: 跳跃游戏 II
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
输入: nums = [2,3,0,1,4]
输出: 2
"""


def can_jump_ii_count(nums):
    """
    正向查找
    :param nums:
    :return:
    44ms 击败 96.79% 使用 Python3 的用户
    """
    n = len(nums)
    cnt = 0
    i = 0
    while i < n:
        cur_steps = nums[i] + i
        if cur_steps >= n - 1:
            if i < n - 1:
                cnt += 1
            return cnt
        max_steps = cur_steps
        max_index = cur_steps
        for j in range(i + 1, cur_steps + 1):
            if j + nums[j] > max_steps:
                max_steps = j + nums[j]
                max_index = j
        cnt += 1
        i = max_index
    return cnt


def can_jump_ii_count_1(nums):
    """反向查找 572ms"""
    pos = len(nums) - 1
    steps = 0
    while pos > 0:
        for i in range(pos):
            if i + nums[i] >= pos:
                pos = i
                steps += 1
                break
    return steps


def can_jump_ii_count_2(nums):
    """方法二：正向查找可到达的最大位置"""
    n = len(nums)
    max_pos, end, step = 0, 0, 0
    for i in range(n - 1):
        if max_pos >= i:
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                end = max_pos
                step += 1
    return step


if __name__ == '__main__':
    nums = [1, 2, 1, 1, 1]
    nums2 = [2, 3, 1, 1, 4]
    print(can_jump_ii_count(nums2))
    print(can_jump_ii_count_1(nums2))
    print(can_jump_ii_count_2(nums2))
