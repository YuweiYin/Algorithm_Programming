#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2215-Find-the-Difference-of-Two-Arrays.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2215 - (Easy) - Find the Difference of Two Arrays
https://leetcode.com/problems/find-the-difference-of-two-arrays/

Description & Requirement:
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

        answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
        answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

    Note that the integers in the lists may be returned in any order.

Example 1:
    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
    Explanation:
        For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 
        are not present in nums2. Therefore, answer[0] = [1,3].
        For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 
        are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:
    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation:
        For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], 
        their value is only included once and answer[0] = [3].
        Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    -1000 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        # main method: (hash set)
        return self._findDifference(nums1, nums2)

    def _findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1

        num_set1 = set(nums1)
        num_set2 = set(nums2)
        res = [[], []]
        for num in num_set1:
            if num not in num_set2:
                res[0].append(num)
        for num in num_set2:
            if num not in num_set1:
                res[1].append(num)

        return res


def main():
    # Example 1: Output: [[1,3],[4,6]]
    # nums1 = [1, 2, 3]
    # nums2 = [2, 4, 6]

    # Example 2: Output: [[3],[]]
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findDifference(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
