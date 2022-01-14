#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0136-Single-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-14
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0136 - (Easy) - Single Number
https://leetcode.com/problems/single-number/

Description & Requirement:
    Given a non-empty array of integers nums, 
    every element appears twice except for one. 
    Find that single one.

    You must implement a solution with a linear runtime complexity 
    and use only constant extra space.

Example 1:
    Input: nums = [2,2,1]
    Output: 1
Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4
Example 3:
    Input: nums = [1]
    Output: 1

Constraints:
    1 <= nums.length <= 3 * 10^4
    -3 * 10^4 <= nums[i] <= 3 * 10^4
    Each element in the array appears twice except for one element which appears only once.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return -1  # Error input type
        if len(nums) == 1:
            return nums[0]
        # main method: (Bit Manipulation: bit-xor)
        #     idea: apply bit-xor operation to all num in nums, A bit-xor A == 0, 0 bit-xor A == A
        #         plus, bit-xor is commutative and both left-associative and right-associative
        return self._singleNumber(nums)

    def _singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


def main():
    # Example 1: Output: 1
    # nums = [2, 2, 1]

    # Example 2: Output: 4
    # nums = [4, 1, 2, 1, 2]

    # Example 3: Output: 1
    nums = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.singleNumber(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
