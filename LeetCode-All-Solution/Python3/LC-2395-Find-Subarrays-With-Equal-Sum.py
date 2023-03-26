#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2395-Find-Subarrays-With-Equal-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-26
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2395 - (Easy) - Find Subarrays With Equal Sum
https://leetcode.com/problems/find-subarrays-with-equal-sum/

Description & Requirement:
    Given a 0-indexed integer array nums, determine whether there exist two subarrays 
    of length 2 with equal sum. Note that the two subarrays must begin at different indices.

    Return true if these subarrays exist, and false otherwise.

    A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [4,2,4]
    Output: true
    Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
Example 2:
    Input: nums = [1,2,3,4,5]
    Output: false
    Explanation: No two subarrays of size 2 have the same sum.
Example 3:
    Input: nums = [0,0,0]
    Output: true
    Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0. 
        Note that even though the subarrays have the same content, the two subarrays are considered different 
        because they are in different positions in the original array.

Constraints:
    2 <= nums.length <= 1000
    -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (hash set)
        return self._findSubarrays(nums)

    def _findSubarrays(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 2

        n = len(nums)
        visited = set()
        for idx in range(n - 1):
            total = nums[idx] + nums[idx + 1]
            if total in visited:
                return True
            visited.add(total)

        return False


def main():
    # Example 1: Output: true
    nums = [4, 2, 4]

    # Example 2: Output: false
    # nums = [1, 2, 3, 4, 5]

    # Example 3: Output: true
    # nums = [0, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findSubarrays(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
