#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1473-Paint-House-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1473 - (Hard) - Paint House III
https://leetcode.com/problems/paint-house-iii/

Description & Requirement:
    There is a row of m houses in a small city, each house must be painted with one of the n colors 
    (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

    A neighborhood is a maximal group of continuous houses that are painted with the same color.
    For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].

    Given an array houses, an m x n matrix cost and an integer target where:
        houses[i]: is the color of the house i, and 0 if the house is not painted yet.
        cost[i][j]: is the cost of paint the house i with the color j + 1.

    Return the minimum cost of painting all the remaining houses in such a way that 
    there are exactly target neighborhoods. If it is not possible, return -1.

Example 1:
    Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
    Output: 9
    Explanation: Paint houses of this way [1,2,2,1,1]
        This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
        Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:
    Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
    Output: 11
    Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
        This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
        Cost of paint the first and last house (10 + 1) = 11.
Example 3:
    Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
    Output: -1
    Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.

Constraints:
    m == houses.length == cost.length
    n == cost[i].length
    1 <= m <= 100
    1 <= n <= 20
    1 <= target <= m
    0 <= houses[i] <= n
    1 <= cost[i][j] <= 10^4
"""


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # exception case
        assert isinstance(houses, list) and isinstance(cost, list)
        assert isinstance(m, int) and m == len(houses) == len(cost) >= 1
        assert isinstance(n, int) and n >= 1 and isinstance(target, int) and target >= 1
        for house in houses:
            assert isinstance(house, int) and house >= 0
        for row in cost:
            assert isinstance(row, list) and len(row) == n
            for item in row:
                assert isinstance(item, int) and item >= 1
        # main method: (dynamic programming)
        return self._minCost(houses, cost, m, n, target)

    def _minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        assert isinstance(houses, list) and isinstance(cost, list)
        assert isinstance(m, int) and m == len(houses) == len(cost) >= 1
        assert isinstance(n, int) and n >= 1 and isinstance(target, int) and target >= 1

        # color range from 0 to n-1, uncolored house is -1
        houses = [house - 1 for house in houses]

        # dp[i][j][k] means that houses[:i] are all colored, and
        # the color of the i-th house is j and it belongs to the k-th neighborhood
        dp = [[[int(1e9+7) for _ in range(target)] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:  # now, we don't need to paint color j for house i
                    continue

                for k in range(target):
                    for cur_j in range(n):
                        if cur_j == j:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][cur_j][k - 1])

                    if dp[i][j][k] != int(1e9+7) and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]

        res = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if res == int(1e9+7) else res


def main():
    # Example 1: Output: 9
    # houses = [0, 0, 0, 0, 0]
    # cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    # m = 5
    # n = 2
    # target = 3

    # Example 2: Output: 11
    houses = [0, 2, 1, 2, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3

    # Example 3: Output: -1
    # houses = [3, 1, 2, 3]
    # cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # m = 4
    # n = 3
    # target = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCost(houses, cost, m, n, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
