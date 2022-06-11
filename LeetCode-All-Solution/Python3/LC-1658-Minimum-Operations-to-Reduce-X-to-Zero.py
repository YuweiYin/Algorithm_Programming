#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1658-Minimum-Operations-to-Reduce-X-to-Zero.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-11
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1658 - (Medium) - Minimum Operations to Reduce X to Zero
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

Description & Requirement:
    You are given an integer array nums and an integer x. 
    In one operation, you can either remove the leftmost or the rightmost element from the array nums and 
    subtract its value from x. Note that this modifies the array for future operations.

    Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:
    Input: nums = [1,1,4,2,3], x = 5
    Output: 2
    Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:
    Input: nums = [5,6,7,8,9], x = 4
    Output: -1
Example 3:
    Input: nums = [3,2,20,1,1,3], x = 10
    Output: 5
    Explanation: The optimal solution is to remove the last three elements and the first two elements 
        (5 operations in total) to reduce x to zero.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
    1 <= x <= 10^9
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(x, int) and x >= 1
        # main method: (find a subarray nums[i: j] of nums that sum(nums[i: j]) + x == sum(nums))
        return self._minOperations(nums, x)

    def _minOperations(self, nums: List[int], x: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(x, int) and x >= 1

        len_nums = len(nums)
        left, right = 0, 0
        res = -1  # max length

        nums_sum = sum(nums)
        if nums_sum == x:
            return len_nums
        target = nums_sum - x
        if target < 0:
            return -1

        cur_sum = 0
        while right < len_nums:  # sliding window
            cur_sum += nums[right]
            while cur_sum > target and left < right:  # shrink window
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                res = max(res, right - left + 1)
            right += 1

        return (len_nums - res) if res >= 0 else -1


def main():
    # Example 1: Output: 2
    # nums = [1, 1, 4, 2, 3]
    # x = 5

    # Example 2: Output: -1
    # nums = [5, 6, 7, 8, 9]
    # x = 4

    # Example 3: Output: 5
    nums = [3, 2, 20, 1, 1, 3]
    x = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minOperations(nums, x)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
