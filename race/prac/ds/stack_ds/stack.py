# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/7/18
Describe: 栈
"""


class ArrayStack:

    def __init__(self, capacity):

        self.n = capacity
        self.data = [0] * capacity
        self.count = 0

    def push(self, value):

        if self.count == self.n:
            return False
        self.data[self.count] = value
        self.count += 1
        return True

    def pop(self):

        if self.count == 0:
            return None
        self.count -= 1
        return self.data[self.count]


def tet_stack():
    array_stack = ArrayStack(5)
    data = ["a", "b", "c", "d", "e"]
    for i in data:
        array_stack.push(i)

    result = array_stack.push("a")
    assert not result
    data.reverse()
    for i in data:
        assert i == array_stack.pop()

    assert array_stack.pop() is None


class StackBasedOnLinkedList:

    def __init__(self):
        self.top = None

    def push(self, value):

        new_node = self.Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):

        if self.top is None:
            return -1
        value = self.top.value
        self.top = self.top.next
        return value

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None


def tet_static():
    stack = StackBasedOnLinkedList()
    data = [1, 2, 3, 4, 5]
    for i in data:
        stack.push(i)
    data.reverse()
    for i in data:
        assert i == stack.pop()
    assert stack.pop() == -1


class Stack:
    """
    Stack(): 创建一个空栈
    push(item): 将item 加入栈顶,无返回值
    pop(): 将栈顶数据项移除,并返回,栈被修改
    peek(): 窥视栈顶数据,返回栈顶的数据项,但不移除,栈不被修改
    is_empty(): 返回栈是否为空
    size(): 返回栈中有多少个数据项
    用列表实现
        列表的尾端作为栈顶
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):

        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack2:
    """
    Stack(): 创建一个空栈
    push(item): 将item 加入栈顶,无返回值
    pop(): 将栈顶数据项移除,并返回,栈被修改
    peek(): 窥视栈顶数据,返回栈顶的数据项,但不移除,栈不被修改
    is_empty(): 返回栈是否为空
    size(): 返回栈中有多少个数据项
    用列表实现
        列表的起始端作为栈顶
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):

        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == '__main__':

    s = Stack2()  # Stack()
    print(s.is_empty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
