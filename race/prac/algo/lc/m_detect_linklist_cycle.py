# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/4
Describe:LCR 022. 环形链表 II
给定一个链表，返回链表开始入环的第一个节点。
从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    32ms 击败 84.09%使用 Python 的用户
    19.55MB 击败 6.82%使用 Python 的用户
    """
    s = set()
    cur_node = head
    while cur_node is not None:
        if cur_node in s:
            return s
        s.add(cur_node)
        cur_node = cur_node.next
    else:
        return None


def detect_cycle_1(head):
    slow = head
    fast = head
    while fast is not None:
        slow = slow.next
        if fast.next is None:
            return None
        fast = fast.next.next
        if fast == slow:
            p = head
            while p != slow:
                p = p.next
                slow = slow.next
            return p
