#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2367-Number-of-Arithmetic-Triplets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2367 - (Easy) - Number of Arithmetic Triplets
https://leetcode.com/problems/number-of-arithmetic-triplets/

Description & Requirement:
    You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
    A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
        i < j < k,
        nums[j] - nums[i] == diff, and
        nums[k] - nums[j] == diff.

    Return the number of unique arithmetic triplets.

Example 1:
    Input: nums = [0,1,4,6,7,10], diff = 3
    Output: 2
    Explanation:
        (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
        (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
Example 2:
    Input: nums = [4,5,6,7,8,9], diff = 2
    Output: 2
    Explanation:
        (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
        (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

Constraints:
    3 <= nums.length <= 200
    0 <= nums[i] <= 200
    1 <= diff <= 50
    nums is strictly increasing.
"""


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 3
        assert isinstance(diff, int) and diff >= 1
        # main method: (hash set)
        return self._arithmeticTriplets(nums, diff)

    def _arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 3
        assert isinstance(diff, int) and diff >= 1

        visited = set(nums)
        return sum((num + diff) in visited and (num + diff * 2) in visited for num in nums)


def main():
    # Example 1: Output: 2
    # nums = [0, 1, 4, 6, 7, 10]
    # diff = 3

    # Example 2: Output: 2
    nums = [4, 5, 6, 7, 8, 9]
    diff = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.arithmeticTriplets(nums, diff)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
