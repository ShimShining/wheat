# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/24
Describe:92. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

输入：head = [5], left = 1, right = 1
输出：[5]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head: ListNode, left: int, right: int):
    """
    :param head:
    :param left:
    :param right:
    :return:
    40ms 击败 80.04%使用 Python3 的用户
    17.08MB 击败 5.01%使用 Python3 的用户
    """
    if left == right:
        return head
    cnt = 1
    cur = head
    pre = None
    while cur is not None and cnt < left:
        pre = cur
        cur = cur.next
        cnt += 1
    if cur is None:
        return head
    sp = None
    s_cur = cur
    swap = 0
    while s_cur is not None and swap < right - left + 1:
        nxt = s_cur.next
        s_cur.next = sp
        sp = s_cur
        s_cur = nxt
        swap += 1
    if left > 1:
        pre.next = sp
        cur.next = s_cur
    else:
        head = sp
        cur.next = s_cur
    return head


def reverse_between_1(head: ListNode, left: int, right: int):
    # 设置 dummyNode 是这一类问题的一般做法
    dummy_node = ListNode(-1)
    dummy_node.next = head
    pre = dummy_node
    for _ in range(left - 1):
        pre = pre.next

    cur = pre.next
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = pre.next
        pre.next = nxt
    return dummy_node.next


if __name__ == '__main__':
    a = ListNode(5)
    a.next = ListNode(3)
    l = 1
    r = 2
    b = reverse_between(a, l, r)
    print(b.val)
