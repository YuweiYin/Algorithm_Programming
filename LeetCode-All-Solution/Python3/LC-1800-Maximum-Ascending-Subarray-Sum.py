#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1800-Maximum-Ascending-Subarray-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-07
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1800 - (Easy) - Maximum Ascending Subarray Sum
https://leetcode.com/problems/maximum-ascending-subarray-sum/

Description & Requirement:
    Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

    A subarray is defined as a contiguous sequence of numbers in an array.

    A subarray [nums_l, nums_{l+1}, ..., nums_{r-1}, nums_r] is ascending if for all i 
    where l <= i < r, nums_i < nums_{i+1}. Note that a subarray of size 1 is ascending.

Example 1:
    Input: nums = [10,20,30,5,10,50]
    Output: 65
    Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:
    Input: nums = [10,20,30,40,50]
    Output: 150
    Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:
    Input: nums = [12,17,15,13,10,11,12]
    Output: 33
    Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (scan the array once, get the sum of every ascending subarray)
        return self._maxAscendingSum(nums)

    def _maxAscendingSum(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        res = cur_sum = last_num = nums[0]
        for num in nums[1:]:
            if num > last_num:
                cur_sum += num
                res = max(res, cur_sum)
            else:  # reset the current sum
                cur_sum = num
            last_num = num

        return res


def main():
    # Example 1: Output: 65
    nums = [10, 20, 30, 5, 10, 50]

    # Example 2: Output: 150
    # nums = [10, 20, 30, 40, 50]

    # Example 3: Output: 33
    # nums = [12, 17, 15, 13, 10, 11, 12]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxAscendingSum(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
