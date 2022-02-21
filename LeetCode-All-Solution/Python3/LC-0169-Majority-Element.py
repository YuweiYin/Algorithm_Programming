#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0169-Majority-Element.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-21
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0169 - (Easy) - Majority Element
https://leetcode.com/problems/majority-element/

Description & Requirement:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3
Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) > 0
        if len(nums) <= 2:
            return nums[0]
        # main method: (hash dict, counter)
        return self._majorityElement(nums)

    def _majorityElement(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        hash_dict = dict({})
        for num in nums:
            if num not in hash_dict:
                hash_dict[num] = 1
            else:
                hash_dict[num] += 1

        if len_nums & 0x01 == 0:  # len_nums is even
            majority_limit = len_nums >> 1
        else:  # len_nums is odd
            majority_limit = (len_nums >> 1) + 1

        for num, counter in hash_dict.items():
            if counter >= majority_limit:
                return num

        return nums[0]  # default result, won't reach here if the test data is valid (has a majority element)


def main():
    # Example 1: Output: 3
    # nums = [3, 2, 3]

    # Example 2: Output: 2
    nums = [2, 2, 1, 1, 1, 2, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.majorityElement(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
