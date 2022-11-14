#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0805-Split-Array-With-Same-Average.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0805 - (Medium) - Split Array With Same Average
https://leetcode.com/problems/split-array-with-same-average/

Description & Requirement:
    You are given an integer array nums.

    You should move each element of nums into one of the two arrays A and B such that 
    A and B are non-empty, and average(A) == average(B).

    Return true if it is possible to achieve that and false otherwise.

    Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

Example 1:
    Input: nums = [1,2,3,4,5,6,7,8]
    Output: true
    Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
Example 2:
    Input: nums = [3,1]
    Output: false

Constraints:
    1 <= nums.length <= 30
    0 <= nums[i] <= 10^4
"""


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (dynamic programming)
        return self._splitArraySameAverage(nums)

    def _splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        Runtime: 740 ms, faster than 59.13% of Python3 online submissions for Split Array With Same Average.
        Memory Usage: 38.9 MB, less than 69.23% of Python3 online submissions for Split Array With Same Average.
        """
        assert isinstance(nums, list) and len(nums) >= 1

        n = len(nums)
        n_half = n >> 1
        sum_nums = sum(nums)
        if all(sum_nums * idx % n for idx in range(1, n_half + 1)):
            return False

        dp = [set() for _ in range(n_half + 1)]
        dp[0].add(0)

        for num in nums:
            for i in range(n_half, 0, -1):
                for x in dp[i - 1]:
                    cur_num = x + num
                    if cur_num * n == sum_nums * i:
                        return True
                    dp[i].add(cur_num)

        return False


def main():
    # Example 1: Output: true
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    # Example 2: Output: false
    # nums = [3, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.splitArraySameAverage(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
