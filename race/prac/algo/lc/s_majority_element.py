# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/30
Describe:169. 多数元素
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
输入：nums = [3,2,3]
输出：3
输入：nums = [2,2,1,1,1,2,2]
输出：2
"""


def majority_element(nums):
    """
    :param nums:
    :return:
    20ms 击败 91.19%使用 Python 的用户
    14.28MB 击败 25.86%使用 Python 的用户
    """
    max_count = 0
    major_elem = nums[0]
    for n in set(nums):
        c = nums.count(n)
        if c > max_count:
            max_count = c
            major_elem = n
    return major_elem


def majority_element_1(nums):
    """
    计数法
    :param nums:
    :return:
    16ms 击败 97.62%使用 Python 的用户
    14.45MB 击败 18.01%使用 Python 的用户
    """
    d = dict()
    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    # new_d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
    # return list(new_d.items())[0][0]
    # k_list = [k for k, v in sorted(d.items(), key=lambda x:x[1], reverse=True)]
    # return k_list[0]

    max_k = 0
    max_v = 0
    for k, v in d.items():
        if v > max_v:
            max_v = v
            max_k = k
    return max_k


def majority_element_2(nums):
    """
    排序取中间位置
    :param nums:
    :return:
    16ms 击败 97.62%使用 Python 的用户
    14.27MB 击败 26.66%使用 Python 的用户
    """
    nums.sort()
    return nums[len(nums) // 2]


#todo 分治算法
def majority_element_3(self, nums: list) -> int:
    def majority_element_rec(lo, hi) -> int:
        # base case; the only element in an array of size 1 is the majority
        # element.
        if lo == hi:
            return nums[lo]

        # recurse on left and right halves of this slice.
        mid = (hi - lo) // 2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid + 1, hi)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

        # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 3]
    print(majority_element_1(nums))
