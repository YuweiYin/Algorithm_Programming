#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0209-Minimum-Size-Subarray-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-18
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0209 - (Medium) - Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Description & Requirement:
    Given an array of positive integers nums and a positive integer target, 
    return the minimal length of a contiguous subarray [nums_{l}, nums_{l+1}, ..., nums_{r-1}, nums_{r}] 
    of which the sum is greater than or equal to target. 
    If there is no such subarray, return 0 instead.

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1
Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

Constraints:
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5

Follow up:
    If you have figured out the O(n) solution, 
    try coding another solution of which the time complexity is O(n log(n)).
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        # main method: (two pointer, slide window) O(n)
        #     idea: if cur_sum < target, then move window_end
        #           if cur_sum == target, then record max of len(window) and move window_end
        #           if cur_sum > target, then record max of len(window) and move window_start
        # other common method for contiguous subarray problems: prefix sum & binary search (import bisect), O(n lg n)
        return self._minSubArrayLen(target, nums)

    def _minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 1

        INF = sys.maxsize
        res = INF
        window_start = 0
        cur_sum = 0
        for window_end, end_num in enumerate(nums):  # consider interval [0:1], [0:2], ..., [0: max]
            cur_sum += end_num  # each for loop, window_end move right, so add number
            if cur_sum < target:
                # if cur_sum is less than target, expand window by moving window_end
                continue
            while cur_sum >= target:  # shrink the window as possible
                res = min(res, window_end - window_start + 1)  # before shrink, record len(window)
                cur_sum -= nums[window_start]  # release window_start
                window_start += 1  # move window_start, do shrink

        return res if res < INF else 0


def main():
    # Example 1: Output: 2
    #     Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    target = 7
    nums = [2, 3, 1, 2, 4, 3]

    # Example 2: Output: 1
    # target = 4
    # nums = [1, 4, 4]

    # Example 3: Output: 0
    # target = 11
    # nums = [1, 1, 1, 1, 1, 1, 1, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minSubArrayLen(target, nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
