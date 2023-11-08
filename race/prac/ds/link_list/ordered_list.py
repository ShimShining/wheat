# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/8
Describe: 有序表
"""
from race.prac.ds.link_list.unordered_list import Node


class OrderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):

        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.get_next()
        return count

    def remove(self, item):

        cur = self.head
        pre = None
        found = False
        while cur is not None and found:
            if cur.get_data() == item:
                found = True
            else:
                pre = cur
                cur = cur.get_next()
        if pre is None and found:
            self.head = cur.get_next()
        elif pre is not None and found:
            pre.set_next(cur.get_next())
        else:
            raise ValueError(f"未找到数据{item}")

    def search(self, item):

        cur = self.head
        found = False
        stop = False
        while cur is not None and not found and not stop:
            if cur.get_data() == item:
                found = True
            else:
                if cur.get_data() > item:
                    stop = True
                cur = cur.get_next()
        return found

    def add(self, item):

        cur = self.head
        previous = None
        stop = False
        while cur is not None and not stop:
            if cur.get_data() > item:
                stop = True
            else:
                previous = cur
                cur = cur.get_next()
        tmp = Node(item)
        if previous is None:
            tmp.set_next(self.head)
            self.head = tmp    # 注意将表头指向新加的数据
        else:
            tmp.set_next(cur)  # 证实下 set_next顺序是否影响 没有影响
            previous.set_next(tmp)
            # tmp.set_next(cur)

    def pop(self, pos=None):   # todo
        data = None
        if self.head is None:
            return data
        if not pos:
            pos = self.size() - 1
        if pos < self.size() - 1:  # 传入的pos可能大于size
            return data
        n = 0
        cur = self.head
        pre = None
        while n < pos:
            pre = cur
            cur = cur.get_next()
            n += 1
        if pre is None:
            data = self.head.get_data()
            self.head = None
        else:
            if cur is None:
                pre.set_next(None)
            else:
                pre.set_next(cur.get_next())
        return cur.get_data()


if __name__ == '__main__':

    ol = OrderedList()
    ol.add(5)
    ol.add(9)
    ol.add(12)
    print(ol.size())
    print(ol.search(5))
    ol.add(7)
    print(ol.size())
    print(ol.search(7))

    print(ol.pop())
    print(ol.pop())
    print(ol.pop())
    print(ol.pop())