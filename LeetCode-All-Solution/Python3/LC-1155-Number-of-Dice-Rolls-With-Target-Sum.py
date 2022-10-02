#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1155-Number-of-Dice-Rolls-With-Target-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-02
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1155 - (Medium) - Number of Dice Rolls With Target Sum
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

Description & Requirement:
    You have n dice and each die has k faces numbered from 1 to k.

    Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) 
    to roll the dice so the sum of the face-up numbers equals target. 
    Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: n = 1, k = 6, target = 3
    Output: 1
    Explanation: You throw one die with 6 faces.
        There is only one way to get a sum of 3.
Example 2:
    Input: n = 2, k = 6, target = 7
    Output: 6
    Explanation: You throw two dice, each with 6 faces.
        There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:
    Input: n = 30, k = 30, target = 500
    Output: 222616187
    Explanation: The answer must be returned modulo 10^9 + 7.

Constraints:
    1 <= n, k <= 30
    1 <= target <= 1000
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and k >= 1
        assert isinstance(target, int) and target >= 1
        # main method: (dynamic programming)
        return self._numRollsToTarget(n, k, target)

    def _numRollsToTarget(self, n: int, k: int, target: int) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and k >= 1
        assert isinstance(target, int) and target >= 1

        MOD = int(1e9+7)
        dp = [[0 for _ in range(1001)] for _ in range(31)]
        init_num = min(k, target)

        for i in range(1, init_num + 1):
            dp[1][i] = 1

        target_max = n * k
        for i in range(2, n + 1):
            for j in range(i, target_max + 1):
                index = 1
                while j >= index and k >= index:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - index]) % MOD
                    index += 1

        return dp[n][target]


def main():
    # Example 1: Output: 1
    # n = 1
    # k = 6
    # target = 3

    # Example 2: Output: 6
    # n = 2
    # k = 6
    # target = 7

    # Example 3: Output: 222616187
    n = 30
    k = 30
    target = 500

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numRollsToTarget(n, k, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
