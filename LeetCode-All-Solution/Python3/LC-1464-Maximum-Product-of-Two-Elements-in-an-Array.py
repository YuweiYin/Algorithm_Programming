#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1464-Maximum-Product-of-Two-Elements-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-26
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1464 - (Easy) - Maximum Product of Two Elements in an Array
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Description & Requirement:
    Given the array of integers nums, you will choose two different indices i and j of that array. 
    Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:
    Input: nums = [3,4,5,2]
    Output: 12 
    Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, 
        that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:
    Input: nums = [1,5,4,5]
    Output: 16
    Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
        you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:
    Input: nums = [3,7]
    Output: 12

Constraints:
    2 <= nums.length <= 500
    1 <= nums[i] <= 10^3
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (find the largest element and the second largest one)
        return self._maxProduct(nums)

    def _maxProduct(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 2

        max_num = max(nums)
        max_idx = nums.index(max_num)
        rest_list = nums[:max_idx] + nums[max_idx + 1:]
        sec_max_num = max(rest_list)

        return (max_num - 1) * (sec_max_num - 1)


def main():
    # Example 1: Output: 12
    # nums = [3, 4, 5, 2]

    # Example 2: Output: 16
    # nums = [1, 5, 4, 5]

    # Example 3: Output: 12
    nums = [3, 7]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxProduct(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
