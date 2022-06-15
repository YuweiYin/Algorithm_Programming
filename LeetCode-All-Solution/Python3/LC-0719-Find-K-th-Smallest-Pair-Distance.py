#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0719-Find-K-th-Smallest-Pair-Distance.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-15
=================================================================="""

import sys
import time
from typing import List
# import bisect
# import functools

"""
LeetCode - 0719 - (Hard) - Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance/

Description & Requirement:
    The distance of a pair of integers a and b is defined as the absolute difference between a and b.

    Given an integer array nums and an integer k, 
    return the k-th smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
    Input: nums = [1,3,1], k = 1
    Output: 0
    Explanation: Here are all the pairs:
        (1,3) -> 2
        (1,1) -> 0
        (3,1) -> 2
        Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:
    Input: nums = [1,1,1], k = 2
    Output: 0
Example 3:
    Input: nums = [1,6,1], k = 3
    Output: 5

Constraints:
    n == nums.length
    2 <= n <= 10^4
    0 <= nums[i] <= 10^6
    1 <= k <= n * (n - 1) / 2
"""


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(nums, list) and len(nums) >= 2
        for num in nums:
            assert isinstance(num, int) and num >= 0
        # main method: (sort & binary search & two pointers)
        return self._smallestDistancePair(nums, k)

    def _smallestDistancePair(self, nums: List[int], k: int) -> int:
        assert isinstance(k, int) and k >= 1
        assert isinstance(nums, list) and len(nums) >= 2
        n = len(nums)

        nums.sort()
        left, right = 0, int(1e9+7)
        while left < right:
            mid = (left + right) >> 1
            counter, j = 0, 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                counter += j - i - 1
            if counter < k:
                left = mid + 1
            else:
                right = mid

        return left


def main():
    # Example 1: Output: 0
    nums = [1, 3, 1]
    k = 1

    # Example 2: Output: 0
    # nums = [1, 1, 1]
    # k = 2

    # Example 3: Output: 5
    # nums = [1, 6, 1]
    # k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestDistancePair(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
