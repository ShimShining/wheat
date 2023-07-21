# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/8
Describe:无序数据,找出元素element
1.比它前面的元素都大
2.比它后元素小
时间复杂度:O(n)
"""


def find_number(arr):
    length = len(arr)
    res = []
    if length == 0:
        return None
    if length == 1:
        return arr[0]
    for i in range(1, length - 1):
        # [3,1,7,9,5,12,8,7,13,14,16]
        if max(arr[:i]) < arr[i] < min(arr[i + 1:]):
            res.append(arr[i])

    return res


if __name__ == "__main__":
    temp = [3, 1, 7, 9, 5, 12, 8, 7, 13, 14, 16]
    res = find_number(temp)
    print(res)
