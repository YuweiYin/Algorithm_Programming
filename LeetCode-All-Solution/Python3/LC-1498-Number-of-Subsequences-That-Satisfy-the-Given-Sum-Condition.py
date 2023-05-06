#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1498-Number-of-Subsequences-That-Satisfy-the-Given-Sum-Condition.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-06
=================================================================="""

import sys
import time
from typing import List
import bisect
# import collections
# import functools

"""
LeetCode - 1498 - (Medium) - Number of Subsequences That Satisfy the Given Sum Condition
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

Description & Requirement:
    You are given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that 
    the sum of the minimum and maximum element on it is less or equal to target. 
    Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: nums = [3,5,6,7], target = 9
    Output: 4
    Explanation: There are 4 subsequences that satisfy the condition.
        [3] -> Min value + max value <= target (3 + 3 <= 9)
        [3,5] -> (3 + 5 <= 9)
        [3,5,6] -> (3 + 6 <= 9)
        [3,6] -> (3 + 6 <= 9)
Example 2:
    Input: nums = [3,3,6,8], target = 10
    Output: 6
    Explanation: There are 6 subsequences that satisfy the condition. 
        (nums can have repeated numbers).
        [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:
    Input: nums = [2,3,3,4,6,7], target = 12
    Output: 61
    Explanation: There are 63 non-empty subsequences, 
        two of them do not satisfy the condition ([6,7], [7]).
        Number of valid subsequences (63 - 2 = 61).

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
    1 <= target <= 10^6
"""


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(target, int) and target >= 1
        # main method: (sorting and binary search)
        return self._numSubseq(nums, target)

    def _numSubseq(self, nums: List[int], target: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(target, int) and target >= 1

        n = len(nums)
        MOD = int(1e9+7)

        dp = [1] + [0] * (n - 1)
        for i in range(1, n):
            dp[i] = (dp[i - 1] << 1) % MOD

        nums.sort()

        res = 0
        for i, num in enumerate(nums):
            if (nums[i] << 1) > target:
                break
            pos = bisect.bisect_right(nums, target - nums[i]) - 1
            res += dp[pos - i] if pos >= i else 0

        return res % MOD


def main():
    # Example 1: Output: 4
    # nums = [3, 5, 6, 7]
    # target = 9

    # Example 2: Output: 6
    # nums = [3, 3, 6, 8]
    # target = 10

    # Example 3: Output: 61
    nums = [2, 3, 3, 4, 6, 7]
    target = 12

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSubseq(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
