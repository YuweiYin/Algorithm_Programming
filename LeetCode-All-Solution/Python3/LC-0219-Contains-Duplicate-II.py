#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0219-Contains-Duplicate-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-19
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0219 - (Easy) - Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Description & Requirement:
    Given an integer array nums and an integer k, 
    return true if there are two distinct indices i and j in the array 
    such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true
Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true
Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    0 <= k <= 10^5
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 1:
            return False  # Error input type
        if k <= 0:
            return False  # Error input type
        if len(nums) == 2:
            return True if nums[0] == nums[1] else False
        # main method: (scan, hash dict, key: number, value: largest index of this number)
        return self._containsNearbyDuplicate(nums, k)

    def _containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Runtime: 653 ms, faster than 90.41% of Python3 online submissions for Contains Duplicate II.
        Memory Usage: 27.5 MB, less than 19.24% of Python3 online submissions for Contains Duplicate II.
        """
        len_nums = len(nums)
        assert len_nums > 2 and k >= 1

        n_i_dict = dict()  # key: number, value: largest index of this number
        for idx, num in enumerate(nums):
            if num not in n_i_dict:  # different number
                n_i_dict[num] = idx
            else:  # same number
                if (idx - n_i_dict[num]) <= k:
                    return True
                else:
                    n_i_dict[num] = idx  # update stored index in dict, store the larger one

        return False  # default, can't find a valid nearby duplicate number pair


def main():
    # Example 1: Output: true
    nums = [1, 2, 3, 1]
    k = 3

    # Example 2: Output: true
    # nums = [1, 0, 1, 1]
    # k = 1

    # Example 3: Output: false
    # nums = [1, 2, 3, 1, 2, 3]
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.containsNearbyDuplicate(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
