#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0823-Binary-Trees-With-Factors.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0823 - (Medium) - Binary Trees With Factors
https://leetcode.com/problems/binary-trees-with-factors/

Description & Requirement:
    Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

    We make a binary tree using these integers, and each number may be used for any number of times. 
    Each non-leaf node's value should be equal to the product of the values of its children.

    Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7.

Example 1:
    Input: arr = [2,4]
    Output: 3
    Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:
    Input: arr = [2,4,5,10]
    Output: 7
    Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:
    1 <= arr.length <= 1000
    2 <= arr[i] <= 10^9
    All the values of arr are unique.
"""


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        for num in arr:
            assert isinstance(num, int) and num >= 2
        # main method: (dynamic programming)
        return self._numFactoredBinaryTrees(arr)

    def _numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Runtime: 454 ms, faster than 81.82% of Python3 online submissions for Binary Trees With Factors.
        Memory Usage: 14.3 MB, less than 30.81% of Python3 online submissions for Binary Trees With Factors.
        """
        assert isinstance(arr, list) and len(arr) >= 1
        n = len(arr)
        MOD = int(1e9+7)

        arr.sort()
        dp = [1 for _ in range(n)]
        num_to_idx = {num: i for i, num in enumerate(arr)}

        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0:
                    # now, arr[j] is the left child
                    right = num / arr[j]
                    if right in num_to_idx:
                        dp[i] += dp[j] * dp[num_to_idx[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD


def main():
    # Example 1: Output: 3
    # arr = [2, 4]

    # Example 2: Output: 7
    arr = [2, 4, 5, 10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numFactoredBinaryTrees(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
