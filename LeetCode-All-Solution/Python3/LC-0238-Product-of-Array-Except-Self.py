#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0238-Product-of-Array-Except-Self.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-15
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0238 - (Medium) - Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Description & Requirement:
    Given an integer array nums, return an array answer 
    such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up:
    Can you solve the problem in O(1) extra space complexity?
    (The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (res[i] is the product of all left numbers and all right numbers, use prefix and suffix product)
        return self._productExceptSelf(nums)

    def _productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        assert len_nums >= 2

        # prefix_product = 1
        res = [1]
        for idx in range(1, len_nums):
            res.append(res[idx - 1] * nums[idx - 1])

        suffix_product = 1
        for idx in reversed(range(len_nums)):
            res[idx] *= suffix_product
            suffix_product *= nums[idx]

        return res


def main():
    # Example 1: Output: [24,12,8,6]
    nums = [1, 2, 3, 4]

    # Example 2: Output: [0,0,9,0,0]
    # nums = [-1, 1, 0, -3, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.productExceptSelf(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
