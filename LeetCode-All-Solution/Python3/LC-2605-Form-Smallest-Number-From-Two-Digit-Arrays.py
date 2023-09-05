#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2605-Form-Smallest-Number-From-Two-Digit-Arrays.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-05
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2605 - (Easy) Form Smallest Number From Two Digit Arrays
https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

Description & Requirement:
    Given two arrays of unique digits nums1 and nums2, 
    return the smallest number that contains at least one digit from each array.

Example 1:
    Input: nums1 = [4,1,3], nums2 = [5,7]
    Output: 15
    Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. 
        It can be proven that 15 is the smallest number we can have.
Example 2:
    Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
    Output: 3
    Explanation: The number 3 contains the digit 3 which exists in both arrays.

Constraints:
    1 <= nums1.length, nums2.length <= 9
    1 <= nums1[i], nums2[i] <= 9
    All digits in each array are unique.
"""


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        # main method: (hash set)
        return self._minNumber(nums1, nums2)

    def _minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1

        def same() -> int:
            s = set(nums1) & set(nums2)
            return -1 if not s else min(s)

        if (x := same()) != -1:
            return x

        x = min(nums1)
        y = min(nums2)

        return min(x * 10 + y, y * 10 + x)


def main():
    # Example 1: Output: 15
    # nums1 = [4, 1, 3]
    # nums2 = [5, 7]

    # Example 2: Output: 3
    nums1 = [3, 5, 2, 6]
    nums2 = [3, 1, 7]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minNumber(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
