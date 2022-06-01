#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0473-Matchsticks-to-Square.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-01
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0473 - (Medium) - Matchsticks to Square
https://leetcode.com/problems/matchsticks-to-square/

Description & Requirement:
    You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. 
    You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, 
    and each matchstick must be used exactly one time.

    Return true if you can make this square and false otherwise.

Example 1:
    Input: matchsticks = [1,1,2,2,2]
    Output: true
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
    Input: matchsticks = [3,3,3,3,4]
    Output: false
    Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:
    1 <= matchsticks.length <= 15
    1 <= matchsticks[i] <= 10^8
"""


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # exception case
        assert isinstance(matchsticks, list) and len(matchsticks) >= 1
        # main method: (DFS & backtrace)
        # return self._makesquare(matchsticks)  # Time: O(4^n)
        return self._makesquareDP(matchsticks)  # Time: O(n * 2^n)

    def _makesquare(self, matchsticks: List[int]) -> bool:
        assert isinstance(matchsticks, list) and len(matchsticks) >= 1
        n = len(matchsticks)
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        matchsticks.sort()
        edge_len = total_len >> 2
        if matchsticks[-1] > edge_len:
            return False

        edge = [0, 0, 0, 0]

        def __dfs(cur_idx: int) -> bool:
            if cur_idx == n:
                return True
            for edge_idx in range(4):  # try 4 directions
                edge[edge_idx] += matchsticks[cur_idx]
                if edge[edge_idx] <= edge_len and __dfs(cur_idx + 1):  # DFS
                    return True
                edge[edge_idx] -= matchsticks[cur_idx]  # backtrace
            return False

        return __dfs(0)

    def _makesquareDP(self, matchsticks: List[int]) -> bool:
        assert isinstance(matchsticks, list) and len(matchsticks) >= 1
        n = len(matchsticks)
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        matchsticks.sort()
        edge_len = total_len >> 2
        if matchsticks[-1] > edge_len:
            return False

        # state records the sticks that have been used, the i-bit of state == 1 means the i-th stick has been used
        # dp[s] means the current length of the unfilled edge of the square
        dp = [-1 for _ in range(1 << n)]
        dp[0] = 0
        for state in range(1, 1 << n):
            for i, stick in enumerate(matchsticks):
                if state & (1 << i) == 0:
                    continue
                new_state = state & ~(1 << i)  # get rid of the i-th bit: it means the i-th stick hasn't been used
                if dp[new_state] >= 0 and dp[new_state] + stick <= edge_len:
                    dp[state] = (dp[new_state] + stick) % edge_len
                    break

        return dp[-1] == 0


def main():
    # Example 1: Output: true
    # matchsticks = [1, 1, 2, 2, 2]

    # Example 2: Output: false
    # matchsticks = [3, 3, 3, 3, 4]

    # Example 3: Output: false
    matchsticks = [5969561, 8742425, 2513572, 3352059, 9084275, 2194427, 1017540, 2324577, 6810719, 8936380, 7868365,
                   2755770, 9954463, 9912280, 4713511]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.makesquare(matchsticks)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
