#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0088-Merge-Sorted-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-26
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0088 - (Easy) - Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Description & Requirement:
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, 
    but instead be stored inside the array nums1. To accommodate this, 
    nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
        The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
        The result of the merge is [1].
Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
        The result of the merge is [1].
        Note that because m = 0, there are no elements in nums1. 
        The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # exception case
        assert isinstance(m, int) and m >= 0 and isinstance(n, int) and n >= 0 and m + n >= 1
        assert isinstance(nums1, list) and len(nums1) == m + n
        assert isinstance(nums2, list) and len(nums2) == n
        # main method: (just merge, in-place modify nums1)
        #     note that: array is not like linked list, insert in the middle is not fast
        #     space optimize: rather than create nums1_valid, scan from the end and put bigger num to the end of nums1
        return self._merge(nums1, m, nums2, n)

    def _merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_valid = nums1[:m]
        cursor_1, cursor_2 = 0, 0
        while cursor_1 < m and cursor_2 < n:  # scan and put in the smaller number at a time
            if nums1_valid[cursor_1] <= nums2[cursor_2]:
                nums1[cursor_1 + cursor_2] = nums1_valid[cursor_1]
                cursor_1 += 1
            else:
                nums1[cursor_1 + cursor_2] = nums2[cursor_2]
                cursor_2 += 1
        while cursor_1 < m:  # the rest part in nums1_valid
            nums1[cursor_1 + cursor_2] = nums1_valid[cursor_1]
            cursor_1 += 1
        while cursor_2 < n:  # the rest part in nums2
            nums1[cursor_1 + cursor_2] = nums2[cursor_2]
            cursor_2 += 1


def main():
    # Example 1: Output: [1,2,2,3,5,6]
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # Example 2: Output: [1]
    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # Example 3: Output: [1]
    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    # ans = solution.merge(nums1, m, nums2, n)
    solution.merge(nums1, m, nums2, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(nums1)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
