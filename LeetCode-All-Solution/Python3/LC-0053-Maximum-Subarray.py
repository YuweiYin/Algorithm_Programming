#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0053-Maximum-Subarray.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0053 - (Easy) - Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Description & Requirement:
    Given an integer array nums, 
    find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:
    Input: nums = [1]
    Output: 1
Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

Follow up:
    If you have figured out the O(n) solution, 
    try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        # main method: (1. Dynamic Programming: 1-dim, compress state to one variable, store cur non-negative sum)
        return self._maxSubArrayDp(nums)
        # main method: (2. Divide & Conquer: similar to interval tree)
        #     divide an interval into two small intervals, calculate the necessary information about small intervals
        #     when combining two intervals, the max subarray of the combined intervals is either:
        #         1) the max subarray of the left small interval
        #         2) the max subarray of the right small interval
        #         3) contain the partitioning number, rightmost part of left small interval, and leftmost of right s i.
        #     the border case is when the interval length == 1
        #     calculate 4 necessary information about small intervals:
        #         1) interval_sum: the sum of all numbers in the interval
        #         2) leftmost_max: the max subarray that contains the leftmost number
        #         2) rightmost_max: the max subarray that contains the rightmost number
        #         2) interval_max: the max subarray of the whole interval
        #     when combining two intervals, say i_l and i_r
        #         1) new interval_sum: i_l.interval_sum + i_r.interval_sum
        #         2) new leftmost_max: max(i_l.leftmost_max, i_l.interval_sum + i_r.leftmost_max)
        #         3) new rightmost_max: max(i_r.rightmost_max, i_l.rightmost_max + i_r.interval_sum)
        #         4) new interval_max: max(i_l.interval_max, i_r.interval_max, i_l.rightmost_max + i_r.leftmost_max)
        #     aim: find the interval_max of interval nums[:]
        # return self._maxSubArrayDC(nums)

    def _maxSubArrayDp(self, nums: List[int]) -> int:
        """
        Kadane's algorithm
        """
        len_nums = len(nums)
        assert len_nums >= 3

        res = nums[0]
        accumulate_sum = 0  # during the process, accumulate_sum may change to another number, or keep accumulating

        for cur_num in nums:
            # accumulate_sum is either the current num or the former accumulate_sum + current num
            # idea: if accumulate_sum is positive, it is always helpful. Once it's negative, change it to cur_num
            accumulate_sum = max(cur_num, accumulate_sum + cur_num)
            # update res
            res = max(res, accumulate_sum)

        return res

    def _maxSubArrayDC(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        class Interval:
            def __init__(self, interval_sum, leftmost_max, rightmost_max, interval_max):
                self.interval_sum = interval_sum
                self.leftmost_max = leftmost_max
                self.rightmost_max = rightmost_max
                self.interval_max = interval_max

        def __combine_interval(i_l: Interval, i_r: Interval) -> Interval:
            new_interval_sum = i_l.interval_sum + i_r.interval_sum
            new_leftmost_max = max(i_l.leftmost_max, i_l.interval_sum + i_r.leftmost_max)
            new_rightmost_max = max(i_r.rightmost_max, i_l.rightmost_max + i_r.interval_sum)
            new_interval_max = max(i_l.interval_max, i_r.interval_max, i_l.rightmost_max + i_r.leftmost_max)
            return Interval(new_interval_sum, new_leftmost_max, new_rightmost_max, new_interval_max)

        def __calculate_max_subarray(left_index: int, right_index: int) -> Interval:
            # border case
            if left_index == right_index:
                return Interval(nums[left_index], nums[left_index], nums[left_index], nums[left_index])

            # divide
            mid_index = (left_index + right_index) >> 1
            left_interval = __calculate_max_subarray(left_index, mid_index)  # dfs left
            right_interval = __calculate_max_subarray(mid_index + 1, right_index)  # dfs right

            # conquer (combine interval)
            return __combine_interval(left_interval, right_interval)

        res = __calculate_max_subarray(0, len_nums - 1)
        return res.interval_max


def main():
    # Example 1: Output: 6
    #     Explanation: [4,-1,2,1] has the largest sum = 6.
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Example 2: Output: 1
    # nums = [1]

    # Example 3: Output: 23
    # nums = [5, 4, -1, 7, 8]

    # Example 4: Output: -1
    # nums = [-2, -3, -1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSubArray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
