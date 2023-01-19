#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0974-Subarray-Sums-Divisible-by-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0974 - (Medium) - Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/

Description & Requirement:
    Given an integer array nums and an integer k, 
    return the number of non-empty subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [4,5,0,-2,-3,1], k = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by k = 5:
        [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:
    Input: nums = [5], k = 9
    Output: 0

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    2 <= k <= 10^4
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 2
        # main method: (hash dict)
        return self._subarraysDivByK(nums, k)

    def _subarraysDivByK(self, nums: List[int], k: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 2

        record = dict({0: 1})
        total, res = 0, 0

        for num in nums:
            total += num
            modulus = total % k
            same = record.get(modulus, 0)
            res += same
            record[modulus] = same + 1

        return res


def main():
    # Example 1: Output: 7
    nums = [4, 5, 0, -2, -3, 1]
    k = 5

    # Example 2: Output: 0
    # nums = [5]
    # k = 9

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.subarraysDivByK(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
