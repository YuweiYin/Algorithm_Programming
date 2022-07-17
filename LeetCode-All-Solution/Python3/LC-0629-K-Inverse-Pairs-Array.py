#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0629-K-Inverse-Pairs-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-17
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0629 - (Hard) - K Inverse Pairs Array
https://leetcode.com/problems/k-inverse-pairs-array/

Description & Requirement:
    For an integer array nums, an inverse pair is a pair of integers [i, j] 
    where 0 <= i < j < nums.length and nums[i] > nums[j].

    Given two integers n and k, return the number of different arrays consist of numbers from 1 to n 
    such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 10^9 + 7.

Example 1:
    Input: n = 3, k = 0
    Output: 1
    Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:
    Input: n = 3, k = 1
    Output: 2
    Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Constraints:
    1 <= n <= 1000
    0 <= k <= 1000
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and k >= 0
        # main method: (dynamic programming)
        return self._kInversePairs(n, k)

    def _kInversePairs(self, n: int, k: int) -> int:
        """
        Runtime: 692 ms, faster than 57.50% of Python3 online submissions for K Inverse Pairs Array.
        Memory Usage: 13.9 MB, less than 86.25% of Python3 online submissions for K Inverse Pairs Array.
        """
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and k >= 0

        MOD = int(1e9+7)
        dp = [0 for _ in range(k + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            _dp = [0 for _ in range(k + 1)]
            for j in range(k + 1):
                _dp[j] = ((_dp[j - 1] if j >= 1 else 0) - (dp[j - i] if j >= i else 0) + dp[j]) % MOD
            dp = _dp

        return dp[-1]


def main():
    # Example 1: Output: 1
    # n, k = 3, 0

    # Example 2: Output: 2
    n, k = 3, 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kInversePairs(n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
