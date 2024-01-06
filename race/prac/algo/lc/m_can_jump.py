# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2024/1/6
Describe:55. 跳跃游戏
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""


def can_jump(nums):
    if len(nums) == 0 or len(nums) == 1:
        return True
    max_step = 0
    for i, num in enumerate(nums):
        if i == 0:
            max_step = max(max_step, num)
        else:
            max_step = max(max_step - 1, num)
        if max_step == 0 and i != len(nums) - 1:
            return False
    return True


def can_jump_1(nums):
    """贪心"""
    n, max_step = len(nums), 0
    for i in range(n):
        if i <= max_step:
            max_step = max(max_step, nums[i] + i)
            if max_step >= n - 1:
                return True
    return False


def can_jump_2(nums):
    """
    如果所有元素都>=1，则可直接判断为true。因为我可以一次走一步，像一只乌龟一样走到终点。
    如果有元素为0，可以把0当作“坑”，为了不掉进坑里，我需要判断坑之前的位置，是否允许我一次跳多格，
    像一只兔子一样越过这个坑，如果可以越过这个坑，则继续往终点走，并继续判断未来的其他坑。
    如果我永远都无法越过某一个坑，则返回false，我将不可能到达终点。
    :param nums:
    :return:
    56ms 击败 99.56% 使用 Python3 的用户
    """
    n = len(nums)
    if n == 0 or n == 1:
        return True
    for i in range(n):
        if i == 0 and nums[i] == 0:
            return False
        if nums[i] >= 1:
            continue
        if i == n - 1:
            return True
        for j in range(i - 1, -1, -1):
            if nums[j] >= i + 1 - j:
                break
        else:
            return False

    return True


if __name__ == '__main__':
    nums = [2, 0, 0]
    nums2 = [3, 2, 1, 0, 4]
    print(can_jump_2(nums))
