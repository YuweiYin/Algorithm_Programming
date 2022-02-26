#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2016-Maximum-Difference-Between-Increasing-Elements.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-26
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2016 - (Easy) - Maximum Difference Between Increasing Elements
https://leetcode.com/problems/maximum-difference-between-increasing-elements/

Description & Requirement:
    Given a 0-indexed integer array nums of size n, 
    find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), 
    such that 0 <= i < j < n and nums[i] < nums[j].

    Return the maximum difference. If no such i and j exists, return -1.

Example 1:
    Input: nums = [7,1,5,4]
    Output: 4
    Explanation:
    The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
    Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
Example 2:
    Input: nums = [9,4,3,2]
    Output: -1
    Explanation:
    There is no i and j such that i < j and nums[i] < nums[j].
Example 3:
    Input: nums = [1,5,2,10]
    Output: 9
    Explanation:
    The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

Constraints:
    n == nums.length
    2 <= n <= 1000
    1 <= nums[i] <= 10^9

Related Problem:
    LC-0121-Best-Time-to-Buy-and-Sell-Stock
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (scan, consider diff between numbers)
        #     idea: record the current smallest number, then consider the largest diff between another number
        return self._maximumDifference(nums)

    def _maximumDifference(self, nums: List[int]) -> int:
        """
        Runtime: 44 ms, faster than 92.52% of Python3 online submissions for Maximum Diff Between Increasing Elements
        Memory Usage: 14 MB, less than 92.04% of Python3 online submissions for Maximum Diff Between Increasing Elements
        """
        len_nums = len(nums)
        assert len_nums >= 2

        res = 0  # default diff is 0
        min_num = nums[0]  # the current smallest number

        for num in nums:
            res = max(res, num - min_num)  # update the max diff
            min_num = min(min_num, num)  # update the min number

        return res if res > 0 else -1


def main():
    # Example 1: Output: 4
    # nums = [7, 1, 5, 4]

    # Example 2: Output: -1
    # nums = [9, 4, 3, 2]

    # Example 3: Output: 9
    nums = [1, 5, 2, 10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumDifference(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
