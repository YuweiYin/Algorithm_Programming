#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2475-Number-of-Unequal-Triplets-in-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-13
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2475 - (Easy) - Number of Unequal Triplets in Array
https://leetcode.com/problems/number-of-unequal-triplets-in-array/

Description & Requirement:
    You are given a 0-indexed array of positive integers nums. 
    Find the number of triplets (i, j, k) that meet the following conditions:

    - 0 <= i < j < k < nums.length
    - nums[i], nums[j], and nums[k] are pairwise distinct.
        - In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].

    Return the number of triplets that meet the conditions.

Example 1:
    Input: nums = [4,4,2,4,3]
    Output: 3
    Explanation: The following triplets meet the conditions:
        - (0, 2, 4) because 4 != 2 != 3
        - (1, 2, 4) because 4 != 2 != 3
        - (2, 3, 4) because 2 != 4 != 3
        Since there are 3 triplets, we return 3.
        Note that (2, 0, 4) is not a valid triplet because 2 > 0.
Example 2:
    Input: nums = [1,1,1,1,1]
    Output: 0
    Explanation: No triplets meet the conditions so we return 0.

Constraints:
    3 <= nums.length <= 100
    1 <= nums[i] <= 1000
"""


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 3 and all([num >= 1 for num in nums])
        # main method: (hash counter)
        return self._unequalTriplets(nums)

    def _unequalTriplets(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 3 and all([num >= 1 for num in nums])

        cnt = collections.Counter(nums)

        n = len(nums)
        res = 0
        pre_sum = 0
        for _, cur_num in cnt.items():
            res += pre_sum * cur_num * (n - pre_sum - cur_num)
            pre_sum += cur_num

        return res


def main():
    # Example 1: Output: 3
    nums = [4, 4, 2, 4, 3]

    # Example 2: Output: 0
    # nums = [1, 1, 1, 1, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.unequalTriplets(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
