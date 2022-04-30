#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0908-Smallest-Range-I.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-30
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0908 - (Easy) - Smallest Range I
https://leetcode.com/problems/smallest-range-i/

Description & Requirement:
    You are given an integer array nums and an integer k.

    In one operation, you can choose any index i where 0 <= i < nums.length and 
    change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. 
    You can apply this operation at most once for each index i.

    The score of nums is the difference between the maximum and minimum elements in nums.

    Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Example 1:
    Input: nums = [1], k = 0
    Output: 0
    Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
Example 2:
    Input: nums = [0,10], k = 2
    Output: 6
    Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
Example 3:
    Input: nums = [1,3,6], k = 3
    Output: 0
    Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^4
    0 <= k <= 10^4
"""


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 0
        # main method: (just consider the gap between max(nums) and min(nums))
        return self._smallestRangeI(nums, k)

    def _smallestRangeI(self, nums: List[int], k: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 0

        len_nums = len(nums)
        if len_nums == 1:
            return 0

        max_n = max(nums)
        min_n = min(nums)
        remedy = k << 1

        return max(0, max_n - min_n - remedy)


def main():
    # Example 1: Output: 0
    # nums = [1]
    # k = 0

    # Example 2: Output: 6
    # nums = [0, 10]
    # k = 2

    # Example 3: Output: 0
    nums = [1, 3, 9]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestRangeI(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
