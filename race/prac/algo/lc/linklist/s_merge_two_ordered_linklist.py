# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/4
Describe:21.合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
输入：l1 = [], l2 = []
输出：[]
输入：l1 = [], l2 = [0]
输出：[0]

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    """
    :param list1:
    :param list2:
    :return:
    16ms 击败 94.82%使用 Python 的用户
    13.07MB 击败 43.48%使用 Python 的用户
    """
    new_list = ListNode(-1)
    new_node = new_list
    while list1 and list2:
        if list1.val <= list2.val:
            new_node.next = list1
            list1 = list1.nexy
        else:
            new_node.next = list2
            list2 = list2.next
        new_node = new_node.next
    new_node.next = list1 if list1 else list2
    return new_list.next


def merge_two_lists_1(list1, list2):
    """
    :param list1:
    :param list2:
    :return:
    24ms 击败 53.43%使用 Python 的用户
    13.08MB 击败 38.38%使用 Python 的用户
    """
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        list1.next = merge_two_lists_1(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_1(list1, list2.next)
        return list2



