#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0456-132-Pattern.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-07
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0456 - (Medium) - 132 Pattern
https://leetcode.com/problems/132-pattern/

Description & Requirement:
    Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
    such that i < j < k and nums[i] < nums[k] < nums[j].

    Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: There is no 132 pattern in the sequence.
Example 2:
    Input: nums = [3,1,4,2]
    Output: true
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
    Input: nums = [-1,3,2,0]
    Output: true
    Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Constraints:
    n == nums.length
    1 <= n <= 2 * 10^5
    -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (consider all possible "1" of "132"-pattern)
        return self._find132pattern(nums)

    def _find132pattern(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)
        if len_nums <= 2:
            return False

        mono_stack = [nums[-1]]  # monotonous stack
        number_2 = - int(1e9+7)  # -10^9 <= nums[i] <= 10^9

        for idx in range(len_nums - 2, -1, -1):  # reversely scan
            cur_num = nums[idx]
            if cur_num < number_2:  # cur_num can be the "1" of "132": cur_num, mono_stack[-1], number_2
                return True
            while len(mono_stack) > 0 and cur_num > mono_stack[-1]:
                number_2 = mono_stack.pop()
            if cur_num > number_2:
                mono_stack.append(cur_num)

        return False


def main():
    # Example 1: Output: false
    # nums = [1, 2, 3, 4]

    # Example 2: Output: true
    # nums = [3, 1, 4, 2]

    # Example 3: Output: true
    nums = [-1, 3, 2, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.find132pattern(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
