#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1567-Maximum-Length-of-Subarray-With-Positive-Product.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-09
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 1567 - (Medium) - Maximum Length of Subarray With Positive Product
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Description & Requirement:
    Given an array of integers nums, 
    find the maximum length of a subarray where the product of all its elements is positive.

    A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

    Return the maximum length of a subarray with positive product.

Example 1:
    Input: nums = [1,-2,-3,4]
    Output: 4
    Explanation: The array nums already has a positive product of 24.
Example 2:
    Input: nums = [0,1,-2,-3,-4]
    Output: 3
    Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
        Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:
    Input: nums = [-1,-2,-3,0,1]
    Output: 2
    Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

Related Problem:
    LC-0152-Maximum-Product-Subarray
"""


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 1 if nums[0] > 0 else 0
        if len(nums) == 2:
            if nums[0] * nums[1] > 0:
                return 2
            if nums[0] > 0 or nums[1] > 0:
                return 1
            return 0
        # main method: (Dynamic Programming)
        #     dp_pos[i] is positive product len end with nums[i], dp_neg[i] is negative product len end with nums[i]
        #         note that: assert dp_pos[i] >= 0 and dp_neg[i] >= 0
        #     dp equation: (1 <= i < len(nums))
        #         if nums[i] > 0:
        #             dp_pos[i] = dp_pos[i-1] + 1
        #             dp_neg[i] = dp_neg[i-1] + 1 if dp_neg[i-1] > 0 else 0
        #         if nums[i] < 0:
        #             dp_pos[i] = dp_neg[i-1] + 1 if dp_neg[i-1] > 0 else 0
        #             dp_neg[i] = dp_pos[i-1] + 1
        #         if nums[i] == 0:
        #             dp_pos[i] = 0
        #             dp_neg[i] = 0
        #     dp init: dp_pos[0] = 1 if nums[0] > 0 else 0; dp_neg[0] = 1 if nums[0] < 0 else 0
        #     dp aim: get max(dp_pos)
        return self._getMaxLen(nums)

    def _getMaxLen(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        dp_pos = [0 for _ in range(len_nums)]
        dp_neg = [0 for _ in range(len_nums)]

        dp_pos[0] = 1 if nums[0] > 0 else 0
        dp_neg[0] = 1 if nums[0] < 0 else 0

        cur_index = 1
        while cur_index < len_nums:
            cur_num = nums[cur_index]
            if cur_num > 0:
                dp_pos[cur_index] = dp_pos[cur_index - 1] + 1
                dp_neg[cur_index] = dp_neg[cur_index - 1] + 1 if dp_neg[cur_index - 1] > 0 else 0
            elif cur_num < 0:
                dp_pos[cur_index] = dp_neg[cur_index - 1] + 1 if dp_neg[cur_index - 1] > 0 else 0
                dp_neg[cur_index] = dp_pos[cur_index - 1] + 1
            else:
                dp_pos[cur_index] = 0
                dp_neg[cur_index] = 0
            cur_index += 1

        return max(dp_pos)


def main():
    # Example 1: Output: 4
    # nums = [1, -2, -3, 4]

    # Example 2: Output: 3
    # nums = [0, 1, -2, -3, -4]

    # Example 3: Output: 2
    nums = [-1, -2, -3, 0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getMaxLen(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
