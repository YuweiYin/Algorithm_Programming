#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0525-Contiguous-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-04
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0525 - (Medium) - Contiguous Array
https://leetcode.com/problems/contiguous-array/

Description & Requirement:
    Given a binary array nums, return the maximum length of a contiguous subarray 
    with an equal number of 0 and 1.

Example 1:
    Input: nums = [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:
    Input: nums = [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 2 if nums[0] != nums[1] else 0
        # main method: (1. Prefix Array)
        #    idea: len(prefix_array) == 2 * len(nums) + 1, mid point prefix_array[len_nums] = -1, others init == -2.
        #        if encounter 0, prefix -= 1; if encounter 1, prefix += 1. (init prefix == 0)
        #        consider index (prefix + len_nums), if cur_num == last_num, then keep decreasing or increasing prefix,
        #            record prefix_array[prefix + len_nums] as the current index in nums cur_idx
        #        if cur_num != last_num, then prefix will "go back" for a step,
        #        if cur_num == 0 and last_num == 1, then prefix_array[prefix + len_nums] is last_idx
        #            so (cur_idx - last_idx) is paired 01 subarray length. (so does case cur_num == 1 and last_num == 0)
        #        if 0(aim), 0, 1, 1(cur), prefix_array[prefix + len_nums] is exactly the aim_idx
        #            so (cur_idx - last_idx) is still paired 01 subarray length. (so does case 1(aim), 1, 0, 0(cur))
        return self._findMaxLengthPrefixArray(nums)

    def _findMaxLengthPrefixArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        res = 0

        prefix_array = [-2 for _ in range((len_nums << 1) + 1)]  # start from mid, both arm length are len(nums)
        prefix_array[len_nums] = -1  # init == -1, because -(-1) == 1, means include nums[0]
        prefix = 0  # record the number gap of 1 and 0, i.e., (number of 1) - (number of 0)

        for cur_idx, cur_num in enumerate(nums):  # scan for once
            # update prefix
            if cur_num == 0:  # 0, decrease
                prefix -= 1
            elif cur_num == 1:  # 1, increase
                prefix += 1
            else:
                raise Exception  # Error Input
            # get the length of 01 subarray based on prefix
            if prefix_array[prefix + len_nums] >= -1:  # >= -1, not -2, have scanned, go back, 01 paired
                # (cur_idx - last_idx) is paired 01 subarray length
                # last_idx is prefix_array[prefix + len_nums]
                res = max(res, cur_idx - prefix_array[prefix + len_nums])
            else:
                # record the cur_idx to prefix_array[prefix + len_nums], when go back, calculate 01 subarray len
                prefix_array[prefix + len_nums] = cur_idx

        return res


def main():
    # Example 1: Output: 2
    # nums = [0, 1, 0]

    # Example 2: Output: 4
    nums = [1, 1, 1, 0, 1, 1, 0, 1]

    # Example 2: Output: 2
    # nums = [1, 1, 1, 0, 1, 1, 1, 0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMaxLength(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
