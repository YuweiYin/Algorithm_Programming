#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1420-Build-Array-Where-You-Can-Find-The-Maximum-Exactly-K-Comparisons.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-10-07
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1420 - (Hard) Build Array Where You Can Find The Maximum Exactly K Comparisons
https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

Description & Requirement:
    You are given three integers n, m and k. Consider the following algorithm 
    to find the maximum element of an array of positive integers:

    You should build the array arr which has the following properties:
        arr has exactly n integers.
        1 <= arr[i] <= m where (0 <= i < n).
        After applying the mentioned algorithm to arr, the value search_cost is equal to k.

    Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

Example 1:
    Input: n = 2, m = 3, k = 1
    Output: 6
    Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:
    Input: n = 5, m = 2, k = 3
    Output: 0
    Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:
    Input: n = 9, m = 1, k = 1
    Output: 1
    Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

Constraints:
    1 <= n <= 50
    1 <= m <= 100
    0 <= k <= n
"""


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(m, int) and m >= 1
        assert isinstance(k, int) and 0 <= k <= n
        # main method: (Dynamic Programming)
        return self._numOfArrays(n, m, k)

    def _numOfArrays(self, n: int, m: int, k: int) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(m, int) and m >= 1
        assert isinstance(k, int) and 0 <= k <= n

        if k == 0:
            return 0

        dp = [[[0] * (m + 1) for _ in range(k + 1)] for __ in range(n + 1)]
        MOD = int(1e9+7)

        for j in range(1, m + 1):
            dp[1][1][j] = 1

        for i in range(2, n + 1):
            for s in range(1, min(k, i) + 1):
                for j in range(1, m + 1):
                    dp[i][s][j] = dp[i - 1][s][j] * j
                    for j0 in range(1, j):
                        dp[i][s][j] += dp[i - 1][s - 1][j0]
                    dp[i][s][j] %= MOD

        res = sum(dp[n][k][j] for j in range(1, m + 1)) % MOD

        return res


def main():
    # Example 1: Output: 6
    # n = 2
    # m = 3
    # k = 1

    # Example 2: Output: 0
    # n = 5
    # m = 2
    # k = 3

    # Example 3: Output: 1
    n = 9
    m = 1
    k = 1

    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.numOfArrays(n, m, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
