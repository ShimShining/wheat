# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/8
Describe:
"""


class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):

        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if item == current.get_data():
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None and found:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def pop(self, pos=None):   # todo
        if self.head is None:
            return None
        if not pos:
            # pos = self.size()
            cur = self.head
            pre = None
            while cur.get_next() is not None:
                pre = cur
                cur = cur.get_next()
            if pre is None:
                self.head = None
            else:
                pre.set_next(cur.get_next())
            return cur.get_data()
        else:
            if pos < self.size() - 1:
                return None
            n = 0
            cur = self.head
            pre = None
            while n < pos:
                pre = cur
                cur = cur.get_next()
                n += 1
            if pre is None:
                self.head = None
            else:
                pre.set_next(cur.get_next())
            return cur.get_data()


if __name__ == '__main__':

    u = UnorderedList()
    u.add(10)
    print(u.pop())
    u.add(11)
    print(u.search(10))
    print(u.pop())
    print(u.is_empty())
    print(u.search(10))