#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0350-Intersection-of-Two-Arrays-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-27
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0350 - (Easy) - Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Description & Requirement:
    Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must appear as many times as it shows in both arrays 
    and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]
Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]
    Explanation: [9,4] is also accepted.

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums1, list) and len(nums1) > 0
        assert isinstance(nums2, list) and len(nums2) > 0
        # main method: (hash dict, count the occurrence of each number in nums1, then scan nums2 to see intersection.)
        return self._intersect(nums1, nums2)

    def _intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # count the shorter list
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 > len_nums2:
            nums1, nums2 = nums2, nums1

        counter = dict({})
        for num in nums1:  # count the occurrence of each number in nums1
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        res = []
        for num in nums2:  # scan nums2 to see intersection
            if num in counter and counter[num] > 0:
                counter[num] -= 1
                res.append(num)
                # at most len_nums1 elements in the intersection list
                if len(res) == len_nums1:
                    break

        return res


def main():
    # Example 1: Output: [2,2]
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    # Example 2: Output: [4,9]
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.intersect(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
