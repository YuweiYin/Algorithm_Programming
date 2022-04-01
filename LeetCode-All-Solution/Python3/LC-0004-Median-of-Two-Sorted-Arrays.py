#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0004-Median-of-Two-Sorted-Arrays.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-01
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0004 - (Easy) - Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Description & Requirement:
    Given two sorted arrays nums1 and nums2 of size m and n respectively, 
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 10^6
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # exception case
        assert isinstance(nums1, list) and isinstance(nums2, list) and len(nums1) + len(nums2) >= 1
        # main method: (1. merge and then find, O(m+n); 2. binary search, O(log(m+n)))
        return self._findMedianSortedArrays(nums1, nums2)

    def _findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Runtime: 104 ms, faster than 79.48% of Python3 online submissions for Median of Two Sorted Arrays.
        Memory Usage: 14.2 MB, less than 71.83% of Python3 online submissions for Median of Two Sorted Arrays.
        """
        m, n = len(nums1), len(nums2)

        def __get_item_by_order(target_order: int):
            idx_nums1, idx_nums2 = 0, 0
            while True:
                # border case
                if idx_nums1 == m:  # no nums1, return the target_order-th number in nums2
                    return nums2[idx_nums2 + target_order - 1]
                if idx_nums2 == n:  # no nums2, return the target_order-th number in nums1
                    return nums1[idx_nums1 + target_order - 1]
                if target_order == 1:  # get the first (smallest) number
                    return min(nums1[idx_nums1], nums2[idx_nums2])

                # binary search
                mid_idx1 = min(idx_nums1 + (target_order >> 1) - 1, m - 1)
                mid_idx2 = min(idx_nums2 + (target_order >> 1) - 1, n - 1)
                mid_num1, mid_num2 = nums1[mid_idx1], nums2[mid_idx2]
                if mid_num1 <= mid_num2:  # the middle number of nums1 is smaller, so its left numbers are smaller too
                    target_order -= mid_idx1 - idx_nums1 + 1  # skip these small numbers
                    idx_nums1 = mid_idx1 + 1
                else:  # the middle number of nums2 is smaller, so its left numbers are smaller too
                    target_order -= mid_idx2 - idx_nums2 + 1  # skip these small numbers
                    idx_nums2 = mid_idx2 + 1

        length = m + n
        if length & 0x01 == 1:  # odd: get the ((m+n+1)/2)-th number
            return float(__get_item_by_order((length + 1) >> 1))
        else:  # even: get the average of the ((m+n)/2)-th number and the ((m+n)/2 + 1)-th number
            return float(__get_item_by_order(length >> 1) + __get_item_by_order((length >> 1) + 1)) / 2


def main():
    # Example 1: Output: 2.00000
    # nums1 = [1, 3]
    # nums2 = [2]

    # Example 2: Output: 2.50000
    nums1 = [1, 2]
    nums2 = [3, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMedianSortedArrays(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
