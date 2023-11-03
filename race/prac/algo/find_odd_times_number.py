# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/3
Describe: 异或 : 一个数与0异或都等于这个数,一个数与自己异或等于0,异或满足交换律和结合律
1. 一个数组中n个数,只有一个数字出现了奇数次,其他数字出现了偶数次.找出这个数字
2. 一个数组中n个数,只有两个数字出现了奇数次,其他数字出现了偶数次.找出这两个数字
"""


def find_odd_times_numbers(nums):
    num_count = {}
    for item in nums:
        if item not in num_count.keys():
            num_count[item] = 1
        else:
            num_count[item] += 1
    # print(num_count)
    res = []
    for k, v in num_count.items():
        if v % 2 != 0:
            res.append(k)

    return res


def find_one_odd_times_number(nums):

    if not nums:
        return
    if len(nums) < 2:
        return nums[0]

    res = 0
    for item in nums:
        res ^= item
    return res


def find_two_odd_times_numbers(nums):
    if not nums:
        return
    if len(nums) < 3:
        return nums[0], nums[1]

    tmp = 0
    for item in nums:
        tmp ^= item   # tmp的结果就是 两个奇数次的数字的异或  a^b
    # 提取出最右侧的1,不等于0的数最右侧的1提取出来
    diff_bit = tmp & (~tmp + 1)   # a b不相等,那么一定有1位上,a,b不同,那么一定有一个数字的某一位是1,对应另外一个数字就是0

    res1 = 0
    for item in nums:
        if diff_bit & item == 0:
            res1 ^= item

    res2 = res1 ^ tmp
    return res1, res2


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 2, 2, 3, 3, 3]
    arr1 = [2]

    r = find_one_odd_times_number(arr)
    r1 = find_one_odd_times_number(arr1)
    print(r, r1)

    r = find_odd_times_numbers(arr)
    r1 = find_odd_times_numbers(arr1)
    print(r, r1)

    arr2 = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    arr3 = [1, 2]

    r = find_two_odd_times_numbers(arr2)
    r1 = find_two_odd_times_numbers(arr2)
    print(r, r1)

    r = find_odd_times_numbers(arr3)
    r1 = find_odd_times_numbers(arr3)
    print(r, r1)

