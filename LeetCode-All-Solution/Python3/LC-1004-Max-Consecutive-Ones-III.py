#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1004-Max-Consecutive-Ones-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-29
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1004 - (Medium) - Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Description & Requirement:
    Given a binary array nums and an integer k, 
    return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
        Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
        Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
    0 <= k <= nums.length

Related Problem:
    LC-2024-Maximize-the-Confusion-of-an-Exam
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 0 <= k <= len(nums)
        # main method: (slide window)
        return self._longestOnes(nums, k)

    def _longestOnes(self, nums: List[int], k: int) -> int:
        def __max_consecutive(target: int) -> int:
            res = 0
            window_start = 0  # guarantee all answers in the window is the target (if not, use operation to change)
            k_counter = 0  # how many operations have used
            for window_end in range(len(nums)):
                if nums[window_end] != target:  # new window end is not the target answer, so use an operation
                    k_counter += 1
                while k_counter > k:  # out of limit of k operations
                    if nums[window_start] != target:
                        # this means to convert answerKey[window_start] to target, one operation was used
                        k_counter -= 1  # recover it
                    window_start += 1
                res = max(res, window_end - window_start + 1)
            return res

        return __max_consecutive(1)


def main():
    # Example 1: Output: 6
    # nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    # k = 2

    # Example 2: Output: 10
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestOnes(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
