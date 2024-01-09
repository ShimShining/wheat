# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2024/1/9
Describe: 380. O(1) 时间插入、删除和获取随机元素
实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。
每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
输入
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出
[null, true, false, true, 2, true, false, 2]

解释
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
"""
import random


class RandomizedSet:

    def __init__(self):
        self.set_list = set()

    def insert(self, val: int) -> bool:
        if val in self.set_list:
            return False
        self.set_list.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set_list:
            self.set_list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(list(self.set_list), 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class RandomizedSet2:

    def __init__(self):
        self.nums = []
        self.indexs = dict()

    def insert(self, val: int) -> bool:
        if val in self.indexs:
            return False
        self.indexs[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.indexs:
            index = self.indexs[val]
            self.nums[index] = self.nums[-1]
            # 先更新indexs字典, 再进行pop, 不然val刚好是最后一位, 就会Index out of range
            self.indexs[self.nums[index]] = index
            self.nums.pop()
            del self.indexs[val]
            return True
        return False

    def get_random(self) -> int:
        return random.choice(self.nums)
