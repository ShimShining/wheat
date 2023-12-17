# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/17
Describe:LCR 023. 相交链表
给定两个单链表的头节点 headA 和 headB ，请找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点
intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    node_set = set()
    cur_a = headA
    cur_b = headB
    while cur_a:
        node_set.add(cur_a)
        cur_a = cur_a.next
    while cur_b:
        if cur_b in node_set:
            return cur_b
        cur_b = cur_b.next
    return None


def get_intersection_node_1(headA, headB):
    if not headA or not headB:
        return None
    cur_a = headA
    cur_b = headB
    done = False
    while not done:
        if cur_a == cur_b:
            return cur_a
        cur_a = cur_a.next if cur_a else headB
        cur_b = cur_b.next if cur_b else headA
