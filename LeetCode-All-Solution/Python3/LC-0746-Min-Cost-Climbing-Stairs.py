#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0746-Min-Cost-Climbing-Stairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-05
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0746 - (Easy) - Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

Description & Requirement:
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
    Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.

Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
        - Pay 15 and climb two steps to reach the top.
        The total cost is 15.
Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: You will start at index 0.
        - Pay 1 and climb two steps to reach index 2.
        - Pay 1 and climb two steps to reach index 4.
        - Pay 1 and climb two steps to reach index 6.
        - Pay 1 and climb one step to reach index 7.
        - Pay 1 and climb two steps to reach index 9.
        - Pay 1 and climb one step to reach the top.
        The total cost is 6.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999

Related Problem:
    LC-0070-Climbing-Stairs
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # exception case
        if not isinstance(cost, list) or len(cost) <= 0:
            return 0  # Error input type
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        # main method: (Dynamic Programming: dp[i] is the min cost to get to i-index staircase, i = 0, 1, 2, ...)
        #     dp equation: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        #     dp init: dp[0] == 0, dp[1] == 0
        #     dp aim: get dp[-1]
        return self._minCostClimbingStairs(cost)

    def _minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Runtime: 52 ms, faster than 96.29% of Python3 online submissions for Min Cost Climbing Stairs.
        Memory Usage: 14 MB, less than 94.07% of Python3 online submissions for Min Cost Climbing Stairs.
        """
        len_cost = len(cost)
        assert len_cost >= 3

        INF = int(1e9+7)
        dp = [INF for _ in range(len_cost + 1)]  # note that the aim is jump over all stairs, reach index == len_cost
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len_cost + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]


def main():
    # Example 1: Output: 15
    # cost = [10, 15, 20]

    # Example 2: Output: 6
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCostClimbingStairs(cost)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
