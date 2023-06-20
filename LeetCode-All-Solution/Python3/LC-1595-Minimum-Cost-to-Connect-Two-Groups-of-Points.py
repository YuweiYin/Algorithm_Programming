#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1595-Minimum-Cost-to-Connect-Two-Groups-of-Points.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-20
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1595 - (Hard) - Minimum Cost to Connect Two Groups of Points
https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

Description & Requirement:
    You are given two groups of points where the first group has size1 points, 
    the second group has size2 points, and size1 >= size2.

    The cost of the connection between any two points are given in an size1 x size2 matrix where 
    cost[i][j] is the cost of connecting point i of the first group and point j of the second group. 
    The groups are connected if each point in both groups is connected to one or more points in the opposite group. 
    In other words, each point in the first group must be connected to at least one point in the second group, 
    and each point in the second group must be connected to at least one point in the first group.

    Return the minimum cost it takes to connect the two groups.

Example 1:
    Input: cost = [[15, 96], [36, 2]]
    Output: 17
    Explanation: The optimal way of connecting the groups is:
        1--A
        2--B
        This results in a total cost of 17.
Example 2:
    Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
    Output: 4
    Explanation: The optimal way of connecting the groups is:
        1--A
        2--B
        2--C
        3--A
        This results in a total cost of 4.
        Note that there are multiple points connected to point 2 in the first group 
        and point A in the second group. This does not matter as there is no limit to 
        the number of points that can be connected. We only care about the minimum total cost.
Example 3:
    Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
    Output: 10

Constraints:
    size1 == cost.length
    size2 == cost[i].length
    1 <= size1, size2 <= 12
    size1 >= size2
    0 <= cost[i][j] <= 100
"""


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # exception case
        assert isinstance(cost, list) and len(cost) >= 1
        # main method: (dynamic programming)
        return self._connectTwoGroups(cost)

    def _connectTwoGroups(self, cost: List[List[int]]) -> int:
        assert isinstance(cost, list) and len(cost) >= 1

        size1, size2 = len(cost), len(cost[0])
        m = 1 << size2
        dp1 = [int(1e9+7)] * m
        dp1[0] = 0
        dp2 = [0] * m

        for i in range(1, size1 + 1):
            for s in range(m):
                dp2[s] = int(1e9+7)
                for k in range(size2):
                    if (s & (1 << k)) == 0:
                        continue
                    dp2[s] = min(dp2[s], dp2[s ^ (1 << k)] + cost[i - 1][k])
                    dp2[s] = min(dp2[s], dp1[s] + cost[i - 1][k])
                    dp2[s] = min(dp2[s], dp1[s ^ (1 << k)] + cost[i - 1][k])
            dp1 = dp2[:]

        return int(dp1[m - 1])


def main():
    # Example 1: Output: 17
    # cost = [[15, 96], [36, 2]]

    # Example 2: Output: 4
    # cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]

    # Example 3: Output: 10
    cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.connectTwoGroups(cost)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
