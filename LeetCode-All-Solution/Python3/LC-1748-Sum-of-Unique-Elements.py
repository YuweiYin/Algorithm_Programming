#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1748-Sum-of-Unique-Elements.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-06
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1748 - (Easy) - Sum of Unique Elements
https://leetcode.com/problems/sum-of-unique-elements/

Description & Requirement:
    You are given an integer array nums. 
    The unique elements of an array are the elements that appear exactly once in the array.

    Return the sum of all the unique elements of nums.

Example 1:
    Input: nums = [1,2,3,2]
    Output: 4
    Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:
    Input: nums = [1,1,1,1,1]
    Output: 0
    Explanation: There are no unique elements, and the sum is 0.
Example 3:
    Input: nums = [1,2,3,4,5]
    Output: 15
    Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return 0 if nums[0] == nums[1] else (nums[0] + nums[1])
        # main method: (hash dict, count the occurrence of each number)
        return self._sumOfUnique(nums)

    def _sumOfUnique(self, nums: List[int]) -> int:
        """
        Runtime: 28 ms, faster than 96.71% of Python3 online submissions for Sum of Unique Elements.
        Memory Usage: 14 MB, less than 83.21% of Python3 online submissions for Sum of Unique Elements.
        """
        len_nums = len(nums)
        assert len_nums >= 3

        hash_dict = dict({})  # key: number; value: the occurrence of the number
        for num in nums:
            if num not in hash_dict:
                hash_dict[num] = 1
            else:
                hash_dict[num] += 1

        res = 0
        for k, v in hash_dict.items():
            if v == 1:
                res += k

        return res


def main():
    # Example 1: Output: 4
    # nums = [1, 2, 3, 2]

    # Example 2: Output: 0
    # nums = [1, 1, 1, 1, 1]

    # Example 3: Output: 15
    nums = [1, 2, 3, 4, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sumOfUnique(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
