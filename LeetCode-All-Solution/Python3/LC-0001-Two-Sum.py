#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0001-Two-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-26
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0001 - (Easy) - Two Sum
https://leetcode.com/problems/two-sum/

Description & Requirement:
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.

    You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

Follow-up:
    Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2 and isinstance(target, int)
        # main method: (hash dict)
        # return self._twoSum(nums, target)
        return self._twoSumBetter(nums, target)

    def _twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        assert len_nums >= 2

        hash_dict = dict({})  # key: the diff (target - num); value: num_idx
        for num_idx, num in enumerate(nums):  # store all diff information
            diff = target - num
            if diff not in hash_dict:
                hash_dict[diff] = [num_idx]
            else:
                hash_dict[diff].append(num_idx)

        for num_idx, num in enumerate(nums):  # scan to find a two_sum pair
            if num in hash_dict:
                for diff_idx in hash_dict[num]:
                    if num_idx != diff_idx:
                        return [num_idx, diff_idx]

        return []  # can't find two_sum pair

    def _twoSumBetter(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        assert len_nums >= 2

        hash_dict = dict({})  # key: num; value: num_idx
        for num_idx, num in enumerate(nums):  # one scan, once found, stop loop
            diff = target - num
            if diff in hash_dict:
                return [hash_dict[diff], num_idx]
            else:
                hash_dict[num] = num_idx  # store it, to be paired for later numbers

        return []  # can't find two_sum pair


def main():
    # Example 1: Output: [0,1]
    # nums = [2, 7, 11, 15]
    # target = 9

    # Example 2: Output: [1,2]
    # nums = [3, 2, 4]
    # target = 6

    # Example 3: Output: [0,1]
    nums = [3, 3]
    target = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.twoSum(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
