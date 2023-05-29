#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2455-Average-Value-of-Even-Numbers-That-Are-Divisible-by-Three.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-29
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2455 - (Easy) - Average Value of Even Numbers That Are Divisible by Three
https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

Description & Requirement:
    Given an integer array nums of positive integers, 
    return the average value of all even integers that are divisible by 3.

    Note that the average of n elements is the sum of the n elements 
    divided by n and rounded down to the nearest integer.

Example 1:
    Input: nums = [1,3,6,10,12,15]
    Output: 9
    Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:
    Input: nums = [1,2,4,7,10]
    Output: 0
    Explanation: There is no single number that satisfies the requirement, so return 0.

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
"""


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (scan the array)
        return self._averageValue(nums)

    def _averageValue(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        total = 0
        div = 0
        for num in nums:
            if num % 6 == 0:
                total += num
                div += 1

        return total // div if div > 0 else 0


def main():
    # Example 1: Output: 9
    nums = [1, 3, 6, 10, 12, 15]

    # Example 2: Output: 0
    # nums = [1, 2, 4, 7, 10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.averageValue(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
