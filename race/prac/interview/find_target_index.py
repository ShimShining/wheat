# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/8/9
Describe:给定一个整数数组 nums 和一个目标值 m，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。数组中同一个元素不能使用两遍。

比如nums= [1,2,2,3,4,5] ,m=6 返回结果为：0,5 1,4 或 0,5 2,4
"""


def is_contains(list_a, list_b):
    if set(list_a) & set(list_b):
        return True
    return False


def classify(indexs):
    classify_dict = {}
    tmp = indexs[:]
    length = len(tmp)
    added = []
    for i in range(length):
        if tmp[i] not in added:
            classify_dict[i] = []
            classify_dict[i].append(tmp[i])
            added.append(tmp[i])
            for j in range(i+1, length):
                if is_contains(tmp[i], tmp[j]) and tmp[j] not in added:
                    classify_dict[i].append(tmp[j])
                    added.append(tmp[j])

    return classify_dict


def find_target_index(nums, target):

    if len(nums) < 2:
        return []
    tmp = []
    for i, num in enumerate(nums):

        if target - num in nums and nums.index(target - num) != i:
            j = nums.index(target - num)
            if [i, j] not in tmp and [j, i] not in tmp:
                tmp.append([i, j])
    print(tmp)
    """
    归类是个组合性问题分出来的带有重复标签的组放在一起算一类
    [[0, 8], [1, 7], [2, 7], [4, 3], [5, 3], [6, 3]]
    0,8算一类
    1,7 | 2,7 算一类
    4,3 | 5,3 | 6,3 算一类
    总共的结果有1*2*3=6种
    下面处理并不能满足这种,怎么处理?TODO
    """
    res = []
    if tmp:
        classify_dict = classify(tmp)
        print(classify_dict)
        keys = classify_dict.keys()
        print(keys)
    # TODO 根据字典的分组进行拼装

    #     length = len(tmp)
    #     for i in range(length-1):
    #         var = tmp[i]
    #         for j in range(i+1, length):
    #             if not set(tmp[i]) & set(tmp[j]):
    #                 var +=  tmp[j]
    #                 print(var)
    #                 res.append(var)
    # return res


if __name__ == "__main__":
    # [] 0,正数
    # [0] 0,正数
    # [0,0,0,0,0] 0,正数
    # [1] 1,0,大于1
    # [1,1,1,1,1,1] 1,0,大于1
    # [0,1,1,2,1,8] 1,0,大于1
    # [0,1,2,3,4,5,6] 1,0,大于1,target=7,5,10
    nums_a = [1, 2, 2, 3, 4, 5]
    nums = [1, 2, 2, 3, 3, 3, 3, 4, 5]    # badecase
    # nums = [1, 1, 1, 1]
    res = find_target_index(nums, 6)
    print(res)
