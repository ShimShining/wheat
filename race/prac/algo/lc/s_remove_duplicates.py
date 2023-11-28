# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/28
Describe: 删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。
nums 的其余元素与 nums 的大小不重要。
返回 k 。

输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
"""


def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    32ms 击败 33.64%使用 Python 的用户
    14.20MB 击败 28.63%使用 Python 的用户
    """
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)


def remove_duplicates_1(nums):
    """
    双指针(快慢指针)
    :param nums:
    :return:
    24ms 击败 74.90%使用 Python 的用户
    13.83MB 击败 53.82%使用 Python 的用户
    """
    if len(nums) < 2:
        return len(nums)
    fast = 1
    slow = 1
    while fast < len(nums):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


def remove_duplicates_2(nums):
    """双指针 从0开始"""
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1



if __name__ == '__main__':
    nums = [1, 1, 2]
    remove_duplicates(nums)
    print(nums)



