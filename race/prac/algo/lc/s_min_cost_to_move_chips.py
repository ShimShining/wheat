# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/29
Describe: 1271 玩筹码
有 n 个筹码。第 i 个筹码的位置是 position[i] 。

我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:

position[i] + 2 或 position[i] - 2 ，此时 cost = 0
position[i] + 1 或 position[i] - 1 ，此时 cost = 1
返回将所有筹码移动到同一位置上所需要的 最小代价 。

输入：position = [1,2,3]
输出：1
解释：第一步:将位置3的筹码移动到位置1，成本为0。
第二步:将位置2的筹码移动到位置1，成本= 1。
总成本是1。

输入：position = [2,2,2,3,3]
输出：2
解释：我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。

输入：position = [1,1000000000]
输出：1
"""


def min_cost_to_move_chips(position):
    """
    暴力解法 遍历每个移动到每个位置下的最小cost,最后返回最小
    :param position:
    :return:
    时间 44ms 击败 6.82%使用 Python 的用户
    13.10MB 击败 11.36%使用 Python 的用户
    """
    if len(position) < 2 or len(set(position)) == 1:
        return 0
    min_cost = len(position) - 1
    for i in range(len(position)):
        step = 0
        for j in range(len(position)):
            if i == j:
                continue
            dis = abs(position[i] - position[j])
            if dis % 2 != 0:
                step += 1  # 奇数 +1
            else:
                continue
        min_cost = min(step, min_cost)
    return min_cost


def min_cost_to_move_chips_opt(position):
    """
    奇数到奇数位置, 偶数到偶数位置一定是偶数步骤,cost=0
    所以找出其中奇数或者偶数的最小值就行 cost = 1
    :param position:
    :return:
    16ms 击败 70.45%使用 Python 的用户
    13.04MB 击败 25.00%使用 Python 的用户
    """
    # cnt = Counter(p % 2 for p in position)  # 根据模 2 后的余数来统计奇偶个数
    # return min(cnt[0], cnt[1]

    pos_odd = 0
    for pos in position:
        if pos % 2 != 0:
            pos_odd += 1
    return min(len(position) - pos_odd, pos_odd)


if __name__ == '__main__':
    pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30]

    print(min_cost_to_move_chips(pos))
    print(min_cost_to_move_chips_opt(pos))

