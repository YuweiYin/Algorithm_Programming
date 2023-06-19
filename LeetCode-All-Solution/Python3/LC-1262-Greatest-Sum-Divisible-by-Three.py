#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1262-Greatest-Sum-Divisible-by-Three.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-19
=================================================================="""

import sys
import time
from typing import List
# import collections
import functools

"""
LeetCode - 1262 - (Medium) - Greatest Sum Divisible by Three
https://leetcode.com/problems/greatest-sum-divisible-by-three/

Description & Requirement:
    Given an integer array nums, 
    return the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:
    Input: nums = [3,6,5,1,8]
    Output: 18
    Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:
    Input: nums = [4]
    Output: 0
    Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:
    Input: nums = [1,2,3,4,4]
    Output: 12
    Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

Constraints:
    1 <= nums.length <= 4 * 10^4
    1 <= nums[i] <= 10^4
"""


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (dynamic programming)
        return self._maxSumDivThree(nums)

    def _maxSumDivThree(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        dp = [0, -float("inf"), -float("inf")]
        for num in nums:
            dp_temp = dp[:]
            for i in range(3):
                dp_temp[(i + num % 3) % 3] = max(dp_temp[(i + num % 3) % 3], dp[i] + num)
            dp = dp_temp

        return int(dp[0])


def main():
    # Example 1: Output: 18
    nums = [3, 6, 5, 1, 8]

    # Example 2: Output: 0
    # nums = [4]

    # Example 3: Output: 12
    # nums = [1, 2, 3, 4, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSumDivThree(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
