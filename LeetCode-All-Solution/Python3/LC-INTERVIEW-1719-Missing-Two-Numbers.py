#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-1719-Missing-Two-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - INTERVIEW-1719 - (Hard) - Missing Two Numbers
https://leetcode.cn/problems/missing-two-lcci/

Description & Requirement:
    You are given an array with all the numbers from 1 to N appearing exactly once, 
    except for two number that is missing. 
    How can you find the missing number in O(N) time and 0(1) space?

    You can return the missing numbers in any order.

Example 1:
    Input: [1]
    Output: [2,3]
Example 2:
    Input: [2,3]
    Output: [1,4]

Constraints:
    nums.length <= 30000
"""


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list)
        # main method: (bit manipulation)
        return self._missingTwo(nums)

    def _missingTwo(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list)

        xor_sum = 0
        n = len(nums) + 2
        for num in nums:
            xor_sum ^= num
        for i in range(1, n + 1):
            xor_sum ^= i

        lsb = xor_sum & (-xor_sum)  # lowest bit 1
        class_1, class_2 = 0, 0
        for num in nums:
            if num & lsb:
                class_1 ^= num
            else:
                class_2 ^= num

        for i in range(1, n + 1):
            if i & lsb:
                class_1 ^= i
            else:
                class_2 ^= i

        return [class_1, class_2]


def main():
    # Example 1: Output: [2,3]
    # nums = [1]

    # Example 2: Output: [1,4]
    nums = [2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.missingTwo(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
