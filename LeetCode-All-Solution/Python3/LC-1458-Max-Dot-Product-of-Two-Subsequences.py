#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1458-Max-Dot-Product-of-Two-Subsequences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-10-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1458 - (Hard) Max Dot Product of Two Subsequences
https://leetcode.com/problems/max-dot-product-of-two-subsequences/

Description & Requirement:
    Given two arrays nums1 and nums2.

    Return the maximum dot product between non-empty subsequences 
    of nums1 and nums2 with the same length.

    A subsequence of a array is a new array which is formed from the original array 
    by deleting some (can be none) of the characters without disturbing the relative positions 
    of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

Example 1:
    Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
    Output: 18
    Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
        Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:
    Input: nums1 = [3,-2], nums2 = [2,-6,7]
    Output: 21
    Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
        Their dot product is (3*7) = 21.
Example 3:
    Input: nums1 = [-1,-1], nums2 = [1,1]
    Output: -1
    Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
        Their dot product is -1.

Constraints:
    1 <= nums1.length, nums2.length <= 500
    -1000 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        # main method: (Dynamic Programming)
        return self._maxDotProduct(nums1, nums2)

    def _maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1

        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                xij = nums1[i] * nums2[j]
                dp[i][j] = xij
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + xij)

        return dp[-1][-1]


def main():
    # Example 1: Output: 18
    nums1 = [2, 1, -2, 5]
    nums2 = [3, 0, -6]

    # Example 2: Output: 21
    # nums1 = [3, -2]
    # nums2 = [2, -6, 7]

    # Example 3: Output: -1
    # nums1 = [-1, -1]
    # nums2 = [1, 1]

    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxDotProduct(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
