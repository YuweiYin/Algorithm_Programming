#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1035-Uncrossed-Lines.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-11
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1035 - (Medium) - Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/

Description & Requirement:
    You are given two integer arrays nums1 and nums2. 
    We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

    We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
        nums1[i] == nums2[j], and
        the line we draw does not intersect any other connecting (non-horizontal) line.

    Note that a connecting line cannot intersect even at the endpoints 
    (i.e., each number can only belong to one connecting line).

    Return the maximum number of connecting lines we can draw in this way.

Example 1:
    Input: nums1 = [1,4,2], nums2 = [1,2,4]
    Output: 2
    Explanation: We can draw 2 uncrossed lines as in the diagram.
        We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 
        will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:
    Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
    Output: 3
Example 3:
    Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
    Output: 2

Constraints:
    1 <= nums1.length, nums2.length <= 500
    1 <= nums1[i], nums2[j] <= 2000
"""


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        # main method: (dynamic programming)
        return self._maxUncrossedLines(nums1, nums2)

    def _maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1

        len_1, len_2 = len(nums1), len(nums2)
        dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 == num2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]


def main():
    # Example 1: Output: 2
    # nums1 = [1, 4, 2]
    # nums2 = [1, 2, 4]

    # Example 2: Output: 3
    # nums1 = [2, 5, 1, 2, 5]
    # nums2 = [10, 5, 2, 1, 5, 2]

    # Example 3: Output: 2
    nums1 = [1, 3, 7, 1, 7, 5]
    nums2 = [1, 9, 2, 5, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxUncrossedLines(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
