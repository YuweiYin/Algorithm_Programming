#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1822-Sign-of-the-Product-of-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1822 - (Easy) - Sign of the Product of an Array
https://leetcode.com/problems/sign-of-the-product-of-an-array/

Description & Requirement:
    There is a function signFunc(x) that returns:
        1 if x is positive.
        -1 if x is negative.
        0 if x is equal to 0.

    You are given an integer array nums. Let product be the product of all values in the array nums.

    Return signFunc(product).

Example 1:
    Input: nums = [-1,-2,-3,-4,3,2,1]
    Output: 1
    Explanation: The product of all values in the array is 144, and signFunc(144) = 1
Example 2:
    Input: nums = [1,5,0,2,-3]
    Output: 0
    Explanation: The product of all values in the array is 0, and signFunc(0) = 0
Example 3:
    Input: nums = [-1,1,-1,1,-1]
    Output: -1
    Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

Constraints:
    1 <= nums.length <= 1000
    -100 <= nums[i] <= 100
"""


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (count the number of negative numbers or zero)
        return self._arraySign(nums)

    def _arraySign(self, nums: List[int]) -> int:
        """
        Runtime: 62 ms, faster than 94.48% of Python3 online submissions for Sign of the Product of an Array.
        Memory Usage: 14.1 MB, less than 37.43% of Python3 online submissions for Sign of the Product of an Array.
        """
        assert isinstance(nums, list) and len(nums) >= 1

        neg_cnt = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                neg_cnt += 1

        return -1 if neg_cnt & 0x01 == 1 else 1


def main():
    # Example 1: Output: 1
    # nums = [-1, -2, -3, -4, 3, 2, 1]

    # Example 2: Output: 0
    # nums = [1, 5, 0, 2, -3]

    # Example 3: Output: -1
    nums = [-1, 1, -1, 1, -1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.arraySign(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
