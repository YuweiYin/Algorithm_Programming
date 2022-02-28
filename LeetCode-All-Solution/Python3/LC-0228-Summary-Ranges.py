#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0228-Summary-Ranges.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-28
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0228 - (Easy) - Summary Ranges
https://leetcode.com/problems/summary-ranges/

Description & Requirement:
    You are given a sorted unique integer array nums.

    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
    That is, each element of nums is covered by exactly one of the ranges, 
    and there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:
        "a->b" if a != b
        "a" if a == b

Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
        [0,2] --> "0->2"
        [4,5] --> "4->5"
        [7,7] --> "7"
Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
        [0,0] --> "0"
        [2,4] --> "2->4"
        [6,6] --> "6"
        [8,9] --> "8->9"

Constraints:
    0 <= nums.length <= 20
    -2^31 <= nums[i] <= 2^31 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # exception case
        assert isinstance(nums, list)
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        # main method: (scan, compass all consecutive numbers)
        return self._summaryRanges(nums)

    def _summaryRanges(self, nums: List[int]) -> List[str]:
        # count the shorter list
        len_nums = len(nums)
        assert len_nums >= 2

        res = []
        cursor = 0
        while cursor < len_nums:
            range_cursor = cursor
            while range_cursor + 1 < len_nums and nums[range_cursor] + 1 == nums[range_cursor + 1]:
                range_cursor += 1
            if range_cursor == cursor:  # only one element, put "m" in res
                res.append(str(nums[cursor]))
                cursor += 1
            else:  # consecutive numbers, put "m->n" in res
                res.append(str(nums[cursor]) + "->" + str(nums[range_cursor]))
                cursor = range_cursor + 1

        return res


def main():
    # Example 1: Output: ["0->2","4->5","7"]
    # nums = [0, 1, 2, 4, 5, 7]

    # Example 2: Output: ["0","2->4","6","8->9"]
    nums = [0, 2, 3, 4, 6, 8, 9]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.summaryRanges(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
