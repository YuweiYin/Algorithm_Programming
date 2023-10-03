#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1512-Number-of-Good-Pairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-10-03
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1512 - (Easy) Number of Good Pairs
https://leetcode.com/problems/number-of-good-pairs/

Description & Requirement:
    Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:
    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.
Example 3:
    Input: nums = [1,2,3]
    Output: 0

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (hash counter)
        return self._numIdenticalPairs(nums)

    def _numIdenticalPairs(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        m = collections.Counter(nums)
        return sum(v * (v - 1) // 2 for k, v in m.items())


def main():
    # Example 1: Output: 4
    nums = [1, 2, 3, 1, 1, 3]

    # Example 2: Output: 6
    # nums = [1, 1, 1, 1]

    # Example 3: Output: 0
    # nums = [1, 2, 3]

    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.numIdenticalPairs(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
