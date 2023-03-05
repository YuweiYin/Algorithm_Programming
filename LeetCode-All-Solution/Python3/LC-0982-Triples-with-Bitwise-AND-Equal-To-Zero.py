#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0982-Triples-with-Bitwise-AND-Equal-To-Zero.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-04
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0982 - (Hard) - Triples with Bitwise AND Equal To Zero
https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

Description & Requirement:
    Given an integer array nums, return the number of AND triples.

    An AND triple is a triple of indices (i, j, k) such that:
        0 <= i < nums.length
        0 <= j < nums.length
        0 <= k < nums.length
        nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.

Example 1:
    Input: nums = [2,1,3]
    Output: 12
    Explanation: We could choose the following i, j, k triples:
        (i=0, j=0, k=1) : 2 & 2 & 1
        (i=0, j=1, k=0) : 2 & 1 & 2
        (i=0, j=1, k=1) : 2 & 1 & 1
        (i=0, j=1, k=2) : 2 & 1 & 3
        (i=0, j=2, k=1) : 2 & 3 & 1
        (i=1, j=0, k=0) : 1 & 2 & 2
        (i=1, j=0, k=1) : 1 & 2 & 1
        (i=1, j=0, k=2) : 1 & 2 & 3
        (i=1, j=1, k=0) : 1 & 1 & 2
        (i=1, j=2, k=0) : 1 & 3 & 2
        (i=2, j=0, k=1) : 3 & 2 & 1
        (i=2, j=1, k=0) : 3 & 1 & 2
Example 2:
    Input: nums = [0,0,0]
    Output: 27

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] < 2^16
"""


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (enumerate)
        return self._countTriplets(nums)

    def _countTriplets(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        cnt = collections.Counter((x & y) for x in nums for y in nums)

        res = 0
        for num in nums:
            for mask, freq in cnt.items():
                if (num & mask) == 0:
                    res += freq

        return res


def main():
    # Example 1: Output: 12
    nums = [2, 1, 3]

    # Example 2: Output: 27
    # nums = [0, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.countTriplets(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
