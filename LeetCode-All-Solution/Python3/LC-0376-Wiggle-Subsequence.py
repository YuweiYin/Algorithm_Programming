#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0376-Wiggle-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-21
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0376 - (Medium) - Wiggle Subsequence
https://leetcode.com/problems/wiggle-subsequence/

Description & Requirement:
    A wiggle sequence is a sequence where the differences between successive numbers 
    strictly alternate between positive and negative. The first difference (if one exists) 
    may be either positive or negative. A sequence with one element and 
    a sequence with two non-equal elements are trivially wiggle sequences.

    For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence 
        because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
    In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. 
        The first is not because its first two differences are positive, 
        and the second is not because its last difference is zero.

    A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, 
    leaving the remaining elements in their original order.

    Given an integer array nums, return the length of the longest wiggle subsequence of nums.

Example 1:
    Input: nums = [1,7,4,9,2,5]
    Output: 6
    Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
Example 2:
    Input: nums = [1,17,5,10,13,15,10,5,16,8]
    Output: 7
    Explanation: There are several subsequences that achieve this length.
        One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
Example 3:
    Input: nums = [1,2,3,4,5,6,7,8,9]
    Output: 2

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000

Follow up:
    Could you solve this in O(n) time?
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 1  # trivially wiggle sequence
        if len(nums) == 2:
            return 2 if nums[0] != nums[1] else 1  # trivially wiggle sequence
        # main method: (greedily scan)
        return self._wiggleMaxLength(nums)

    def _wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Runtime: 24 ms, faster than 99.81% of Python3 online submissions for Wiggle Subsequence.
        Memory Usage: 13.9 MB, less than 77.55% of Python3 online submissions for Wiggle Subsequence.
        """
        len_nums = len(nums)
        assert len_nums >= 3

        second_num_idx = 1  # first_num_idx == 0
        # find the different one as the second element of wiggle sequence
        while second_num_idx < len_nums and nums[second_num_idx] == nums[0]:
            second_num_idx += 1
        if second_num_idx == len_nums:
            return 1  # all numbers are the same

        res = 2  # two elements, trivially wiggle sequence
        if nums[second_num_idx] > nums[0]:
            is_ascending = True
        else:
            is_ascending = False

        # scan the rest part  (second_num_idx will change)
        for cur_num_idx in range(second_num_idx + 1, len_nums):
            cur_num = nums[cur_num_idx]
            cur_diff = cur_num - nums[second_num_idx]
            if cur_diff > 0:
                if is_ascending:  # consecutive ascend, res stays still, update second_num_idx (to a bigger number)
                    second_num_idx = cur_num_idx
                else:  # a wiggle, res increase, update second_num_idx and is_ascending bool indicator
                    res += 1
                    second_num_idx = cur_num_idx
                    is_ascending = not is_ascending
            elif cur_diff < 0:
                if is_ascending:  # a wiggle, res increase, update second_num_idx and is_ascending bool indicator
                    res += 1
                    second_num_idx = cur_num_idx
                    is_ascending = not is_ascending
                else:  # consecutive descend, res stays still, update second_num_idx (to a smaller number)
                    second_num_idx = cur_num_idx
            else:  # no diff, keep moving
                continue

        return res


def main():
    # Example 1: Output: 6
    # nums = [1, 7, 4, 9, 2, 5]

    # Example 2: Output: 7
    #     Explanation: There are several subsequences that achieve this length.
    #         One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
    nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]

    # Example 3: Output: 2
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.wiggleMaxLength(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
