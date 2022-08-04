#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1403-Minimum-Subsequence-in-Non-Increasing-Order.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1403 - (Easy) - Minimum Subsequence in Non-Increasing Order
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

Description & Requirement:
    Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than 
    the sum of the non included elements in such subsequence. 

    If there are multiple solutions, return the subsequence with minimum size and 
    if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. 
    A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

    Note that the solution with the given constraints is guaranteed to be unique. 
    Also return the answer sorted in non-increasing order.

Example 1:
    Input: nums = [4,3,10,9,8]
    Output: [10,9] 
    Explanation: The subsequences [10,9] and [10,8] are minimal such that 
        the sum of their elements is strictly greater than the sum of elements not included, 
        however, the subsequence [10,9] has the maximum total sum of its elements. 
Example 2:
    Input: nums = [4,4,7,6,7]
    Output: [7,7,6] 
    Explanation: The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater 
        than the sum of elements not included (14 = 4 + 4 + 6). 
        Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. 
        Note the subsequence has to returned in non-decreasing order.  
Example 3:
    Input: nums = [6]
    Output: [6]

Constraints:
    1 <= nums.length <= 500
    1 <= nums[i] <= 100
"""


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (sort, greedy)
        return self._minSubsequence(nums)

    def _minSubsequence(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1

        nums.sort(reverse=True)
        _sum, s = sum(nums), 0
        for i, num in enumerate(nums):
            s += num
            if s > _sum - s:
                return nums[:i + 1]


def main():
    # Example 1: Output: [10,9]
    nums = [4, 3, 10, 9, 8]

    # Example 2: Output: [7,7,6]
    # nums = [4, 4, 7, 6, 7]

    # Example 3: Output: [6]
    # nums = [6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minSubsequence(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
