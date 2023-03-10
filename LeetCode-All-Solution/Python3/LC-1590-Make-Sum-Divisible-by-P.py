#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1590-Make-Sum-Divisible-by-P.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-10
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1590 - (Medium) - Make Sum Divisible by P
https://leetcode.com/problems/make-sum-divisible-by-p/

Description & Requirement:
    Given an array of positive integers nums, remove the smallest subarray (possibly empty) 
    such that the sum of the remaining elements is divisible by p. 
    It is not allowed to remove the whole array.

    Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

    A subarray is defined as a contiguous block of elements in the array.

Example 1:
    Input: nums = [3,1,4,2], p = 6
    Output: 1
    Explanation: The sum of the elements in nums is 10, which is not divisible by 6. 
        We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:
    Input: nums = [6,3,5,2], p = 9
    Output: 2
    Explanation: We cannot remove a single element to get a sum divisible by 9. 
        The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:
    Input: nums = [1,2,3], p = 3
    Output: 0
    Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= p <= 10^9
"""


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(p, int) and p >= 1
        # main method: (prefix sum)
        return self._minSubarray(nums, p)

    def _minSubarray(self, nums: List[int], p: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(p, int) and p >= 1

        x = sum(nums) % p
        if x == 0:
            return 0

        y = 0
        index_dict = {0: -1}
        res = len(nums)

        for idx, num in enumerate(nums):
            y = (y + num) % p
            if (y - x) % p in index_dict:
                res = min(res, idx - index_dict[(y - x) % p])
            index_dict[y] = idx

        return res if res < len(nums) else -1


def main():
    # Example 1: Output: 1
    nums = [3, 1, 4, 2]
    p = 6

    # Example 2: Output: 2
    # nums = [6, 3, 5, 2]
    # p = 9

    # Example 3: Output: 0
    # nums = [1, 2, 3]
    # p = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minSubarray(nums, p)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
