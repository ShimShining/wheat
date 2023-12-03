#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:
"""
"""

//java版本
 2public class LRUCache {
 3  class LinkedNode {
 4    int key;
 5    int value;
 6    LinkedNode prev;
 7    LinkedNode next;
 8  }
 9
10  private void addNode(LinkedNode node) {
11    node.prev = head;
12    node.next = head.next;
13    head.next.prev = node;
14    head.next = node;
15  }
16
17  private void removeNode(LinkedNode node){
18    LinkedNode prev = node.prev;
19    LinkedNode next = node.next;
20    prev.next = next;
21    next.prev = prev;
22  }
23
24  private void moveToHead(LinkedNode node){
25    removeNode(node);
26    addNode(node);
27  }
28
29  private LinkedNode popTail() {
30    LinkedNode res = tail.prev;
31    removeNode(res);
32    return res;
33  }
34
35  private Hashtable<Integer, LinkedNode> cache = new Hashtable<Integer, LinkedNode>();
36  private int size;
37  private int capacity;
38  private LinkedNode head, tail;
39
40  public LRUCache(int capacity) {
41    this.size = 0;
42    this.capacity = capacity;
43    head = new LinkedNode();
44    tail = new LinkedNode();
45    head.next = tail;
46    tail.prev = head;
47  }
48
49  public int get(int key) {
50    LinkedNode node = cache.get(key);
51    if (node == null) return -1;
52    moveToHead(node);
53    return node.value;
54  }
55
56  public void put(int key, int value) {
57    LinkedNode node = cache.get(key);
58
59    if(node == null) {
60      LinkedNode newNode = new LinkedNode();
61      newNode.key = key;
62      newNode.value = value;
63      cache.put(key, newNode);
64      addNode(newNode);
65      ++size;
66      if(size > capacity) {
67        LinkedNode tail = popTail();
68        cache.remove(tail.key);
69        --size;
70      }
71    } else {
72      node.value = value;
73      moveToHead(node);
74    }
75  }
76}
"""


# 1、创建节点
class Node(object):
    # 初始化方法
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


# 2、创建循环链表
class DoubleLinKList(object):
    # 初始化方法
    def __init__(self):
        self._head = None

    # 3、判断是否为空
    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    # 4、求其长度
    def length(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    # 遍历
    def travel(self):
        """遍历链表"""
        print("你要遍历的链表元素有：", end=" ")
        cur = self._head
        while cur != None:
            print("%s " % cur.item, end=" ")
            cur = cur.next
        print("")

    # 5、头插
    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self._head
            # 将_head的头节点的prev指向node
            self._head.prev = node
            # 将_head 指向node
            self._head = node

    # 6、尾插
    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    # 7、查找
    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    # 8、指定位置插入
    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0 or pos > self.length() + 1:
            print("你输入的位置有误，请重新输入")
        elif pos == 1:
            self.add(item)
        elif pos == self.length() + 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 1
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node

    # 9、删除
    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur.next.prev = None
                    # 将_head指向第二个节点
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next


# 验证
if __name__ == '__main__':
    double_link = DoubleLinKList()
    # 头插
    double_link.add(1)
    # 遍历
    double_link.travel()
    # 尾插
    double_link.append(2)
    double_link.travel()
    # 按照索引插入
    double_link.insert(3, 4)
    double_link.travel()

    double_link.insert(3, 3)
    double_link.travel()
    # 删除
    double_link.remove(3)
    double_link.travel()