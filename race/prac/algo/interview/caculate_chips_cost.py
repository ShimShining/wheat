# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/27
Describe: shopee面试题出自leetcode 1217. Play with Chips
There are some chips, and the i-th chip is at position chips[i].

You can perform any of the two following types of moves any number of times (possibly zero) on any chip:

Move the i-th chip by 2 units to the left or to the right with a cost of 0.
Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
There can be two or more chips at the same position initially.

Return the minimum cost needed to move all the chips to the same position (any position).


Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.


Input: chips = [2,2,2,3,3]
Output: 2
Explanation: Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
这道题的意思就是我们要将所有的署条移动到同一个位置，移动两步不需要cost，移动一步要1cost
"""


class MySolution:
    """
    执行用时：76 ms, 在所有 Python3 提交中击败了6.02%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了77.37%的用户
    """

    def min_cost_to_move_chips(self, chips):

        length = len(chips)
        min_cost_list = []

        if length == 0:
            return 0
        if length == 1 or len(set(chips)) == 1:
            return 0
        for i in range(length):
            total_cost = 0
            for j in range(length):
                if i == j:
                    continue
                dis = abs(chips[i] - chips[j])
                if dis % 2 == 0:
                    continue
                else:
                    total_cost += 1
            min_cost_list.append(total_cost)
        return min(min_cost_list)


class Solution:
    """
    优化后求解,合并奇数无需代价,合并偶数也无需代价,寻找奇数个数和偶数个数,其中的最小值就是cost
    执行用时：40 ms, 在所有 Python3 提交中击败了68.25%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了34.67%的用户
    """

    def min_cost_to_move_chips(self, chips):
        num_even = 0
        for chip_pos in chips:
            if chip_pos % 2 == 0:
                num_even += 1
        return min(len(chips) - num_even, num_even)


if __name__ == "__main__":

    temps = [[1, 2, 3], [2, 2, 2, 3, 3]]
    my_solution = MySolution()
    sol = Solution()
    for temp in temps:
        print(f"my_solution={my_solution.min_cost_to_move_chips(temp)}")
        print(f"solution={sol.min_cost_to_move_chips(temp)}")
