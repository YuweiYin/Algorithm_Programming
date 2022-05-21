#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0961-N-Repeated-Element-in-Size-2N-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-21
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0961 - (Easy) - N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

Description & Requirement:
    You are given an integer array nums with the following properties:
        nums.length == 2 * n.
        nums contains n + 1 unique elements.
        Exactly one element of nums is repeated n times.

    Return the element that is repeated n times.

Example 1:
    Input: nums = [1,2,3,3]
    Output: 3
Example 2:
    Input: nums = [2,1,2,5,3,2]
    Output: 2
Example 3:
    Input: nums = [5,1,5,2,5,3,5,4]
    Output: 5

Constraints:
    2 <= n <= 5000
    nums.length == 2 * n
    0 <= nums[i] <= 10^4
    nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (only one number will repeat, use hash set to find it)
        return self._repeatedNTimes(nums)

    def _repeatedNTimes(self, nums: List[int]) -> int:
        """
        Runtime: 208 ms, faster than 93.83% of Python3 online submissions for N-Repeated Element in Size 2N Array.
        Memory Usage: 15.4 MB, less than 57.88% of Python3 online submissions for N-Repeated Element in Size 2N Array.
        """
        assert isinstance(nums, list) and len(nums) >= 2
        hash_set = set()

        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                return num

        return nums[0]


def main():
    # Example 1: Output: 3
    # nums = [1, 2, 3, 3]

    # Example 2: Output: 2
    # nums = [2, 1, 2, 5, 3, 2]

    # Example 3: Output: 5
    nums = [5, 1, 5, 2, 5, 3, 5, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.repeatedNTimes(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
