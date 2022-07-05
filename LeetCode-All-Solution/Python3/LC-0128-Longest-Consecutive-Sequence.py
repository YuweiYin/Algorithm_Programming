#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0128-Longest-Consecutive-Sequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-05
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0128 - (Medium) - Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Description & Requirement:
    Given an unsorted array of integers nums, 
    return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list)
        # main method: (sort and scan O(n log n); hash set O(n))
        return self._longestConsecutive(nums)

    def _longestConsecutive(self, nums: List[int]) -> int:
        assert isinstance(nums, list)
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums

        nums = list(set(nums))  # get rid of duplication
        nums.sort()

        len_nums = len(nums)

        res = 1
        i = 0
        while i < len_nums:
            j = i + 1
            cur_len = 1
            while j < len_nums and nums[j] == nums[i] + 1:
                i += 1
                j += 1
                cur_len += 1
            i = j
            res = max(res, cur_len)

        return res


def main():
    # Example 1: Output: 4
    nums = [100, 4, 200, 1, 3, 2, 1]

    # Example 2: Output: 9
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestConsecutive(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
