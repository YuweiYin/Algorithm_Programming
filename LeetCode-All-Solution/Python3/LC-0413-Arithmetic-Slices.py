#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0413-Arithmetic-Slices.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-27
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0413 - (Medium) - Arithmetic Slices
https://leetcode.com/problems/arithmetic-slices/

Description & Requirement:
    An integer array is called arithmetic if it consists of at least three elements 
    and if the difference between any two consecutive elements is the same.
        For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

    Given an integer array nums, return the number of arithmetic subarrays of nums.

    A subarray is a contiguous subsequence of the array.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 3
    Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:
    Input: nums = [1]
    Output: 0

Constraints:
    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) <= 2:
            return 0
        if len(nums) == 3:
            return 1 if nums[1] - nums[0] == nums[2] - nums[1] else 0
        # main method: (scan and find each longest valid subarray)
        #     for a valid array, all its subarrays are valid (len >= 3)
        return self._numberOfArithmeticSlices(nums)

    def _numberOfArithmeticSlices(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 4

        def __get_longest_arithmetic_array(start_index: int) -> int:
            """
            :return: how many valid numbers in this arithmetic array, nums[start_index: start_index + valid_num_counter]
            """
            if start_index >= len_nums - 2:
                return 0
            valid_num_counter = 2
            gap = nums[start_index + 1] - nums[start_index]
            cur_index = start_index + 2
            while cur_index < len_nums:
                if nums[cur_index] - nums[cur_index - 1] == gap:
                    valid_num_counter += 1
                    cur_index += 1
                else:
                    break
            return valid_num_counter if valid_num_counter >= 3 else 0

        res = 0
        start_idx = 0
        while start_idx < len_nums - 1:
            cur_longest_len = __get_longest_arithmetic_array(start_idx)
            if cur_longest_len >= 3:
                # if cur_longest_len == 3, then res += 1
                # if cur_longest_len == 4, then res += 1 + 2
                # if cur_longest_len == 5, then res += 1 + 2 + 3, so on and so forth
                _add = 1
                for _ in range(2, cur_longest_len):
                    res += _add
                    _add += 1
                start_idx += cur_longest_len - 1  # skip this span, resume from the end of this span
            else:
                start_idx += 1

        return res


def main():
    # Example 1: Output: 3
    #     Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
    # nums = [1, 2, 3, 4]

    # Example 2: Output: 0
    # nums = [1]

    # Example 3: Output: 5
    nums = [1, 2, 3, 4, 7, 10, 11, 12]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfArithmeticSlices(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
