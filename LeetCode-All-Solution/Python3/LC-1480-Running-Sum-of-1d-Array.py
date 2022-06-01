#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1480-Running-Sum-of-1d-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-01
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1480 - (Easy) - Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/

Description & Requirement:
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i]).

    Return the running sum of nums.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]

Constraints:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (1-Dim DP)
        return self._runningSum(nums)

    def _runningSum(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1
        dp = [nums[0]]
        for idx in range(1, len(nums)):
            dp.append(nums[idx] + dp[-1])

        return dp


def main():
    # Example 1: Output: [1,3,6,10]
    nums = [1, 2, 3, 4]

    # Example 2: Output: [1,2,3,4,5]
    # nums = [1, 1, 1, 1, 1]

    # Example 3: Output: [3,4,6,16,17]
    # nums = [3, 1, 2, 10, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.runningSum(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
