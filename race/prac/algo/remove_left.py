# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/14
Describe:给定一个由正整数组成的列表nums，请编写一个函数，
若某个元素出现重复，则将其左侧相同值的元素都移除，并返回余下的列表。
示例：
输入：[3,4,4,3,6,3]，输出：[4,6,3]
说明：首先索引0和3的元素3会被去除，然后索引1的元素4会被去除。

题目难度：简单
"""


def remove_left(nums: list) -> list:
    if not nums:
        return []
    tmp = dict()
    for i, num in enumerate(nums):
        tmp[num] = i
    sort_tmp = sorted(tmp.items(), key=lambda item: item[1])
    print(sort_tmp)
    return [item[0] for item in sort_tmp]


def remove_left_oth1(nums: list) -> list:

    res = []
    nums.reverse()
    # print(nums)
    for num in nums:
        if num not in res:
            res.append(num)
    res.reverse()
    return res


if __name__ == "__main__":
    assert remove_left([3, 4, 4, 3, 6, 3]) == [4, 6, 3]
    assert remove_left([1, 2, 1, 2, 1, 2, 3]) == [1, 2, 3]
    assert remove_left([1, 2, 3, 4]) == [1, 2, 3, 4]

    assert remove_left_oth1([3, 4, 4, 3, 6, 3]) == [4, 6, 3]
    assert remove_left_oth1([1, 2, 1, 2, 1, 2, 3]) == [1, 2, 3]
    assert remove_left_oth1([1, 2, 3, 4]) == [1, 2, 3, 4]
