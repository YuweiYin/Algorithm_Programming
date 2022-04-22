#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0396-Rotate-Function.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-22
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0396 - (Medium) - Rotate Function
https://leetcode.com/problems/rotate-function/

Description & Requirement:
    You are given an integer array nums of length n.

    Assume arr_k to be an array obtained by rotating nums by k positions clock-wise. 
    We define the rotation function F on nums as follow:
        F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1].

    Return the maximum value of F(0), F(1), ..., F(n-1).

    The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
    Input: nums = [4,3,2,6]
    Output: 26
    Explanation:
        F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
        F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
        F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
        F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
        So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
Example 2:
    Input: nums = [100]
    Output: 0

Constraints:
    n == nums.length
    1 <= n <= 10^5
    -100 <= nums[i] <= 100
"""


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (consider F(k) - F(k-1), where 1 <= k <= n-1)
        #     F(0) = 0 * nums[0] + 1 * nums[1] + 2 * nums[2] + ... + (n-2) * nums[n-2] + (n-1) * nums[n-1]
        #     F(1) = 0 * nums[n-1] + 1 * nums[0] + 2 * nums[1] + ... + (n-2) * nums[n-3] + (n-1) * nums[n-2]
        #     F(1) - F(0) = sum(nums) - n * nums[n-1]
        #     generally, F(k) - F(k-1) = sum(nums) - n * nums[n - k], where 1 <= k <= n-1
        return self._maxRotateFunction(nums)

    def _maxRotateFunction(self, nums: List[int]) -> int:
        """
        Runtime: 1830 ms, faster than 41.22% of Python3 online submissions for Rotate Function.
        Memory Usage: 22 MB, less than 93.03% of Python3 online submissions for Rotate Function.
        """
        assert isinstance(nums, list) and len(nums) >= 1
        n = len(nums)

        sum_nums = sum(nums)
        last_f = 0  # F(0)
        for idx, num in enumerate(nums):
            last_f += idx * num

        res = last_f
        for k in range(1, n):
            # F(k) - F(k-1) = sum(nums) - n * nums[n - k], where 1 <= k <= n-1
            next_f = last_f + sum_nums - n * nums[n - k]
            res = max(res, next_f)
            last_f = next_f

        return res


def main():
    # Example 1: Output: 26
    nums = [4, 3, 2, 6]

    # Example 2: Output: 0
    # nums = [100]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxRotateFunction(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
