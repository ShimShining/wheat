# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/24
Describe:二叉搜索树
"""


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, cur_node):
        # 递归左子树
        if key < cur_node.key:
            if cur_node.has_left_child():
                self._put(key, val, cur_node.left_child)
            else:
                cur_node.left_child = TreeNode(key, val, parent=cur_node)
        # 递归右子树
        else:
            if cur_node.has_right_child():
                self._put(key, val, cur_node.right_child)
            else:
                cur_node.right_child = TreeNode(key, val, parent=cur_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, cur_node):
        if not cur_node:
            return None
        if cur_node.key == key:
            return cur_node
        if key < cur_node.key:
            return self._get(key, cur_node.left_child)
        else:
            return self._get(key, cur_node.right_child)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self.get(item):   # if self._get(item, self.root):
            return True
        return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError(f"Error, key={key} not in tree.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"Error, key={key} not in tree.")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        """
        1. 叶子节点
        2. 被删除的节点有一个子节点
            左
            右
        3. 两个子节点
        :param node:
        :return:
        """
        if node.is_leaf():   # 1. 叶子节点
            if node == node.parent.left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None
        elif node.has_both_children():
            succ = node.find_successor()
            succ.splice_out()
            node.key = succ.key
            node.payload = succ.payload
        else:  # 被删除的节点有一个子节点
            if node.has_left_child():
                if node.is_left_child():  # 左子节点删除
                    node.left_child.parent = node.parent
                    node.parent.left_child = node.left_child
                elif node.is_right_child():  # 右子节点删除
                    node.left_child.parent = node.parent
                    node.parent.right_child = node.left_child
                else:   # 根节点删除
                    node.replace_node_data(node.left_child.key, node.left_child.payload,
                                           node.left_child.left_child, node.left_child.right_child)
            else:
                if node.is_left_child(): # 左子节点删除
                    node.right_child.parent = node.parent
                    node.parent.left_child = node.right_child
                elif node.is_right_child():  # 右子节点删除
                    node.right_child.parent = node.parent
                    node.parent.right_child = node.right_child
                else:  # 根节点
                    node.replace_node_data(node.right_child.key, node.right_child.payload,
                                           node.right_child.left_child, node.right_child.right_child)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key   # 键值
        self.payload = val  # 数据项
        self.left_child = left  # 左子树
        self.right_child = right  # 右子树
        self.parent = parent   # 父节点

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():  # 摘除叶子节点
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent


if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree[3] = 'red'
    my_tree[4] = 'blue'
    my_tree[6] = 'yellow'
    my_tree[2] = 'pink'
    print(3 in my_tree)
    print(my_tree[6])
    del my_tree[3]
    print(my_tree[2])
    for key in my_tree:
        print(key, my_tree[key])

