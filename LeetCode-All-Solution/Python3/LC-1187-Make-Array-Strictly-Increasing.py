#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1187-Make-Array-Strictly-Increasing.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-20
=================================================================="""

import sys
import time
from typing import List
import bisect
# import collections
# import functools

"""
LeetCode - 1187 - (Hard) - Make Array Strictly Increasing
https://leetcode.com/problems/make-array-strictly-increasing/

Description & Requirement:
    Given two integer arrays arr1 and arr2, return the minimum number of operations 
    (possibly zero) needed to make arr1 strictly increasing.

    In one operation, you can choose two indices 0 <= i < arr1.length and 
    0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

    If there is no way to make arr1 strictly increasing, return -1.

Example 1:
    Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
    Output: 1
    Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:
    Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
    Output: 2
    Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:
    Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
    Output: -1
    Explanation: You can't make arr1 strictly increasing.

Constraints:
    1 <= arr1.length, arr2.length <= 2000
    0 <= arr1[i], arr2[i] <= 10^9
"""


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # exception case
        assert isinstance(arr1, list) and len(arr1) >= 1
        assert isinstance(arr2, list) and len(arr2) >= 1
        # main method: (dynamic programming)
        return self._makeArrayIncreasing(arr1, arr2)

    def _makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        assert isinstance(arr1, list) and len(arr1) >= 1
        assert isinstance(arr2, list) and len(arr2) >= 1

        arr2 = list(set(arr2))
        arr2.sort()

        n = len(arr1)
        m = len(arr2)

        INF = int(1e9+7)
        dp = [[INF] *(min(m, n)+1) for _ in range(n + 1)]
        dp[0][0] = -1
        for i in range(1, n + 1):
            for j in range(min(i, m) + 1):
                if arr1[i - 1] > dp[i - 1][j]:
                    dp[i][j] = arr1[i - 1]
                if j and dp[i - 1][j - 1] != INF:
                    k = bisect.bisect_right(arr2, dp[i - 1][j - 1], j - 1)
                    if k < m:
                        dp[i][j] = min(dp[i][j], arr2[k])
                if i == n and dp[i][j] != INF:
                    return j

        return -1


def main():
    # Example 1: Output: 1
    # arr1 = [1, 5, 3, 6, 7]
    # arr2 = [1, 3, 2, 4]

    # Example 2: Output: 2
    # arr1 = [1, 5, 3, 6, 7]
    # arr2 = [4, 3, 1]

    # Example 3: Output: -1
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 6, 3, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.makeArrayIncreasing(arr1, arr2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
