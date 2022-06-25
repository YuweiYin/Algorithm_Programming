#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-OFFER-II-0091-Paint-House.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-25
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - OFFER-II-0091 - (Medium) - Paint House
https://leetcode.com/problems/paint-house/
https://leetcode.cn/problems/JEj789/

Description & Requirement:
    假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，
    你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

    当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。
    每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。

    例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。

    请计算出粉刷完所有房子最少的花费成本。

Example 1:
    Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
    Output: 10
    Explanation: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。最少花费: 2 + 5 + 3 = 10。
Example 2:
    Input: costs = [[7,6,2]]
    Output: 2

Constraints:
    costs.length == n
    costs[i].length == 3
    1 <= n <= 100
    1 <= costs[i][j] <= 20
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # exception case
        assert isinstance(costs, list) and len(costs) >= 1
        for cost in costs:
            assert isinstance(cost, list) and len(cost) == 3 and all([c >= 1 for c in cost])
        # main method: (dynamic programming)
        #     dp[i][j] = costs[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
        return self._minCost(costs)

    def _minCost(self, costs: List[List[int]]) -> int:
        assert isinstance(costs, list) and len(costs) >= 1

        dp = [[int(1e9+7) for _ in range(3)] for _ in range(len(costs))]
        dp[0] = costs[0]

        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

        return min(dp[-1])


def main():
    # Example 1: Output: 10
    #     Explanation: min cost: 2 + 5 + 3 = 10。
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]

    # Example 2: Output: 2
    # costs = [[7, 6, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCost(costs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
