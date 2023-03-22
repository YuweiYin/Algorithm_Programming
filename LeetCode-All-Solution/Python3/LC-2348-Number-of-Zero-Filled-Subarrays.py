#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2348-Number-of-Zero-Filled-Subarrays.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2348 - (Medium) - Number of Zero-Filled Subarrays
https://leetcode.com/problems/number-of-zero-filled-subarrays/

Description & Requirement:
    Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,3,0,0,2,0,0,4]
    Output: 6
    Explanation: 
        There are 4 occurrences of [0] as a subarray.
        There are 2 occurrences of [0,0] as a subarray.
        There is no occurrence of a subarray with a size more than 
            2 filled with 0. Therefore, we return 6.
Example 2:
    Input: nums = [0,0,0,2,0,0]
    Output: 9
    Explanation:
        There are 5 occurrences of [0] as a subarray.
        There are 3 occurrences of [0,0] as a subarray.
        There is 1 occurrence of [0,0,0] as a subarray.
        There is no occurrence of a subarray with a size more than 3 filled with 0. 
            Therefore, we return 9.
Example 3:
    Input: nums = [2,10,2019]
    Output: 0
    Explanation: There is no subarray filled with 0. Therefore, we return 0.

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (subarray summation and reset)
        return self._zeroFilledSubarray(nums)

    def _zeroFilledSubarray(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        res = accumulation = 0
        for num in nums:
            if num != 0:
                accumulation = 0
            else:
                accumulation += 1
                res += accumulation

        return res


def main():
    # Example 1: Output: 6
    nums = [1, 3, 0, 0, 2, 0, 0, 4]

    # Example 2: Output: 9
    # nums = [0, 0, 0, 2, 0, 0]

    # Example 3: Output: 0
    # nums = [2, 10, 2019]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.zeroFilledSubarray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
