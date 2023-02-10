#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1223-Dice-Roll-Simulation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-10
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1223 - (Hard) - Dice Roll Simulation
https://leetcode.com/problems/dice-roll-simulation/

Description & Requirement:
    A die simulator generates a random number from 1 to 6 for each roll. 
    You introduced a constraint to the generator such that 
    it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

    Given an array of integers rollMax and an integer n, return the number of distinct sequences that 
    can be obtained with exact n rolls. Since the answer may be too large, return it modulo 10^9 + 7.

    Two sequences are considered different if at least one element differs from each other.

Example 1:
    Input: n = 2, rollMax = [1,1,2,2,2,3]
    Output: 34
    Explanation: There will be 2 rolls of die, if there are no constraints on the die, 
        there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, 
        the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, 
        so the final answer is 36-2 = 34.
Example 2:
    Input: n = 2, rollMax = [1,1,1,1,1,1]
    Output: 30
Example 3:
    Input: n = 3, rollMax = [1,1,1,2,2,3]
    Output: 181

Constraints:
    1 <= n <= 5000
    rollMax.length == 6
    1 <= rollMax[i] <= 15
"""


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(rollMax, list) and len(rollMax) >= 1
        # main method: (dynamic programming)
        return self._dieSimulator(n, rollMax)

    def _dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        Time: beats 98.43%; Space: beats 88.98%
        """
        assert isinstance(n, int) and n >= 1
        assert isinstance(rollMax, list) and len(rollMax) >= 1

        MOD = int(1e9+7)
        m = len(rollMax)

        dp = [[0] * m for _ in range(n)]
        dp[0] = [1] * m

        s = [0] * n
        s[0] = m
        for i in range(1, n):
            for j, mx in enumerate(rollMax):
                res = s[i - 1]
                if i > mx:
                    res -= s[i - mx - 1] - dp[i - mx - 1][j]
                elif i == mx:
                    res -= 1
                dp[i][j] = res % MOD
            s[i] = sum(dp[i]) % MOD

        return s[-1]


def main():
    # Example 1: Output: 34
    # n = 2
    # rollMax = [1, 1, 2, 2, 2, 3]

    # Example 2: Output: 30
    # n = 2
    # rollMax = [1, 1, 1, 1, 1, 1]

    # Example 3: Output: 181
    n = 3
    rollMax = [1, 1, 1, 2, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.dieSimulator(n, rollMax)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
