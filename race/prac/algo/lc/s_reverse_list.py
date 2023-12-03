# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/3
Describe: LCR 024. 反转链表
给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

输入：head = [1,2]
输出：[2,1]

输入：head = []
输出：[]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    迭代解法
    :param head:
    :return:
    """
    pre, cur = None, head
    while cur is not None:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre


def reverse_list_r(head):
    """
    递归解法
    :param head:
    :return:
    """
    if not head or head.next is None:
        return head
    p = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p

