#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0645-Set-Mismatch.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-23
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0645 - (Easy) - Set Mismatch
https://leetcode.com/problems/set-mismatch/

Description & Requirement:
    You have a set of integers s, which originally contains all the numbers from 1 to n. 
    Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
    which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
    Input: nums = [1,2,2,4]
    Output: [2,3]
Example 2:
    Input: nums = [1,1]
    Output: [1,2]

Constraints:
    2 <= nums.length <= 10^4
    1 <= nums[i] <= 10^4
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (hash dict counter)
        return self._findErrorNums(nums)

    def _findErrorNums(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 2
        n = len(nums)

        hash_dict = dict({})
        for num in range(1, n + 1):
            hash_dict[num] = 0

        for num in nums:
            hash_dict[num] += 1

        res = [-1, -1]
        for num, cnt in hash_dict.items():
            if cnt == 0:
                res[1] = num
            if cnt == 2:
                res[0] = num

        return res


def main():
    # Example 1: Output: [2,3]
    # nums = [1, 2, 2, 4]

    # Example 2: Output: [1,2]
    nums = [1, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findErrorNums(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
