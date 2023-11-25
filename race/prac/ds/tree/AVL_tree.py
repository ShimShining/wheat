# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/25
Describe: avl 树
"""

# -*- coding: utf-8 -*-
import unittest

"""
Author : shining
Date: 2023/11/24
Describe:二叉搜索树
"""


class AVLTree:
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
            self.root = AVLTreeNode(key, val)
        self.size += 1

    def _put(self, key, val, cur_node):
        # 递归左子树
        if key < cur_node.key:
            if cur_node.has_left_child():
                self._put(key, val, cur_node.left_child)
            else:
                cur_node.left_child = AVLTreeNode(key, val, parent=cur_node)
                self.update_balance(cur_node.left_child)  # 更新节点的平衡因子
        # 递归右子树
        else:
            if cur_node.has_right_child():
                self._put(key, val, cur_node.right_child)
            else:
                cur_node.right_child = AVLTreeNode(key, val, parent=cur_node)
                self.update_balance(cur_node.right_child)  # 更新节点的平衡因子

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance_factor < 0:  # 右重需要左旋
            if node.right_child.balance_factor > 0:  # 右子节点左重需要先右旋
                # 先做右旋
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                # 只做左旋
                self.rotate_left(node)
        elif node.balance_factor > 0:  # 左重需要右旋
            if node.left_child.balance_factor < 0:  # 左子结点右重先做左旋
                # 先做左旋
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                # 只需要做右旋
                self.rotate_right(node)

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
        if self.get(item):  # if self._get(item, self.root):
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
        if node.is_leaf():  # 1. 叶子节点
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
                else:  # 根节点删除
                    node.replace_node_data(node.left_child.key, node.left_child.payload,
                                           node.left_child.left_child, node.left_child.right_child)
            else:
                if node.is_left_child():  # 左子节点删除
                    node.right_child.parent = node.parent
                    node.parent.left_child = node.right_child
                elif node.is_right_child():  # 右子节点删除
                    node.right_child.parent = node.parent
                    node.parent.right_child = node.right_child
                else:  # 根节点
                    node.replace_node_data(node.right_child.key, node.right_child.payload,
                                           node.right_child.left_child, node.right_child.right_child)

    def rotate_left(self, rot_root):
        """左旋"""
        new_root = rot_root.right_child
        rot_root.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root

        new_root.left_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rotate_right(self, old_root):
        """右旋"""
        new_root = old_root.left_child
        old_root.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = old_root
        new_root.parent = old_root.parent
        if old_root.is_root():
            self.root = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.left_child = new_root
            else:
                old_root.parent.right_child = new_root

        new_root.right_child = old_root
        old_root.parent = new_root
        old_root.balance_factor = old_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(old_root.balance_factor, 0)


class AVLTreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # 键值
        self.payload = val  # 数据项
        self.left_child = left  # 左子树
        self.right_child = right  # 右子树
        self.parent = parent  # 父节点
        self.balance_factor = 0

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


class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = AVLTree()

    def testAuto1(self):
        self.bst.put(30, 'a')
        self.bst.put(50, 'b')
        self.bst.put(40, 'c')
        assert self.bst.root.key == 40

    def testAuto2(self):
        self.bst.put(50, 'a')
        self.bst.put(30, 'b')
        self.bst.put(40, 'c')
        assert self.bst.root.key == 40

    def testAuto3(self):
        self.bst.put(50, 'a')
        self.bst.put(30, 'b')
        self.bst.put(70, 'c')
        self.bst.put(80, 'c')
        self.bst.put(60, 'd')
        self.bst.put(90, 'e')
        assert self.bst.root.key == 70

    def testAuto3(self):
        self.bst.put(40, 'a')
        self.bst.put(30, 'b')
        self.bst.put(50, 'c')
        self.bst.put(45, 'd')
        self.bst.put(60, 'e')
        self.bst.put(43, 'f')
        assert self.bst.root.key == 45
        assert self.bst.root.left_child.key == 40
        assert self.bst.root.right_child.key == 50
        assert self.bst.root.balance_factor == 0
        assert self.bst.root.left_child.balance_factor == 0
        assert self.bst.root.right_child.balance_factor == -1

    def testAuto4(self):
        self.bst.put(40, 'a')
        self.bst.put(30, 'b')
        self.bst.put(50, 'c')
        self.bst.put(10, 'd')
        self.bst.put(35, 'e')
        self.bst.put(37, 'f')
        assert self.bst.root.key == 35
        assert self.bst.root.left_child.key == 30
        assert self.bst.root.right_child.key == 40
        assert self.bst.root.balance_factor == 0
        assert self.bst.root.left_child.balance_factor == 1
        assert self.bst.root.right_child.balance_factor == 0


if __name__ == '__main__':
    import platform

    print(platform.python_version())
    unittest.main()
    my_tree = AVLTree()
    my_tree[3] = 'red'
    my_tree[4] = 'blue'
    my_tree[6] = 'yellow'
    my_tree[2] = 'pink'
    my_tree[8] = "green"
    my_tree[7] = "black"
    my_tree[9] = "orange"
    print(3 in my_tree)
    print(my_tree[6])
    del my_tree[3]
    print(my_tree[2])
    for key in my_tree:
        print(key, my_tree[key])
