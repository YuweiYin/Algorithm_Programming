#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0905-Sort-Array-By-Parity.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-28
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0905 - (Easy) - Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Description & Requirement:
    Given an integer array nums, move all the even integers 
    at the beginning of the array followed by all the odd integers.

    Return any array that satisfies this condition.

Example 1:
    Input: nums = [3,1,2,4]
    Output: [2,4,3,1]
    Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (just move it)
        return self._sortArrayByParity(nums)

    def _sortArrayByParity(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)
        if len_nums == 1:
            return nums

        res = []
        odd = []
        for num in nums:
            if num & 0x01 == 0:  # even integer
                res.append(num)
            else:  # odd integer
                odd.append(num)

        res.extend(odd)
        return res


def main():
    # Example 1: Output: [2,4,3,1]
    nums = [3, 1, 2, 4]

    # Example 2: Output: [0]
    # nums = [0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sortArrayByParity(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
