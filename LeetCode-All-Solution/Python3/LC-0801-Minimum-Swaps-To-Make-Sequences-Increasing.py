#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0801-Minimum-Swaps-To-Make-Sequences-Increasing.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-10
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0801 - (Hard) - Minimum Swaps To Make Sequences Increasing
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

Description & Requirement:
    You are given two integer arrays of the same length nums1 and nums2. 
    In one operation, you are allowed to swap nums1[i] with nums2[i].

        For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], 
        you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].

    Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. 
    The test cases are generated so that the given input always makes it possible.

    An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

Example 1:
    Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
    Output: 1
    Explanation: 
        Swap nums1[3] and nums2[3]. Then the sequences are:
        nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
        which are both strictly increasing.
Example 2:
    Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
    Output: 1

Constraints:
    2 <= nums1.length <= 10^5
    nums2.length == nums1.length
    0 <= nums1[i], nums2[i] <= 2 * 10^5
"""


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 2
        assert isinstance(nums2, list) and len(nums2) == len(nums1)
        for num in (nums1 + nums2):
            assert isinstance(num, int) and num >= 0
        # main method: (dynamic programming)
        return self._minSwap(nums1, nums2)

    def _minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Runtime: 1233 ms, faster than 90.72% of Python3 submissions for Minimum Swaps To Make Sequences Increasing.
        Memory Usage: 31.9 MB, less than 68.56% of Python3 submissions for Minimum Swaps To Make Sequences Increasing.
        """
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) == len(nums1)

        n = len(nums1)

        # dp[i][0] is the minimal number of the operations of index i, where the number at index i has NOT bben swapped
        # dp[i][0] is the minimal number of the operations of index i, where the number at index i has been swapped
        # dp = []

        dp_1, dp_2 = 0, 1  # state compression
        for i in range(1, n):
            tmp_1, tmp_2 = dp_1, dp_2
            dp_1 = dp_2 = n
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp_1 = min(dp_1, tmp_1)
                dp_2 = min(dp_2, tmp_2 + 1)

            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp_1 = min(dp_1, tmp_2)
                dp_2 = min(dp_2, tmp_1 + 1)

        return min(dp_1, dp_2)


def main():
    # Example 1: Output: 1
    nums1, nums2 = [1, 3, 5, 4], [1, 2, 3, 7]

    # Example 2: Output: 1
    # nums1, nums2 = [0, 3, 5, 8, 9], [2, 1, 4, 6, 9]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minSwap(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
