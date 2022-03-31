#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0410-Split-Array-Largest-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0410 - (Hard) - Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/

Description & Requirement:
    Given an array nums which consists of non-negative integers and an integer m, 
    you can split the array into m non-empty continuous subarrays.

    Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
    Input: nums = [7,2,5,10,8], m = 2
    Output: 18
    Explanation:
        There are four ways to split nums into two subarrays.
        The best way is to split it into [7,2,5] and [10,8],
        where the largest sum among the two subarrays is only 18.
Example 2:
    Input: nums = [1,2,3,4,5], m = 2
    Output: 9
Example 3:
    Input: nums = [1,4,4], m = 3
    Output: 4

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 10^6
    1 <= m <= min(50, nums.length)
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(m, int) and 1 <= m <= min(50, len(nums))
        # main method: (Dynamic Programming)
        #    dp[i][j] means the minimum of the largest sum among these j subarrays, using first i numbers in nums
        #    dp equation: dp[i][j] = min(dp[i][j], max(dp[k][j - 1], subarray_prefix[i] - subarray_prefix[k]))
        #        where k is the split point, range from 0 to i
        #        subarray_split[i] is the prefix sum, i.e., sum(nums[0: i+1])
        #        so (subarray_prefix[i] - subarray_prefix[k]) is the interval sum
        #    dp init: dp[0][0] = 0
        #    dp aim: get dp[-1][-1]
        # return self._splitArray(nums, m)
        return self._splitArrayBinarySearch(nums, m)

    def _splitArray(self, nums: List[int], m: int) -> int:
        """
        TLE, passed 29 of 30
        """
        len_nums = len(nums)
        assert len_nums >= 1

        # optimize: compress consecutive 0s
        new_nums = []
        idx = 0
        while idx < len_nums:
            if nums[idx] != 0:
                new_nums.append(nums[idx])
                idx += 1
            else:
                new_nums.append(0)
                while idx < len_nums and nums[idx] == 0:
                    idx += 1

        len_nums = len(new_nums)
        m = min(m, len_nums)
        # dp[i][j] means the minimum of the largest sum among these j subarrays, using first i numbers in nums
        dp = [[int(1e9+7) for _ in range(m + 1)] for _ in range(len_nums + 1)]  # 1e9+7 as INF

        # calculate the prefix sum
        subarray_prefix = [0]
        # for num in nums:
        for num in new_nums:
            subarray_prefix.append(subarray_prefix[-1] + num)

        dp[0][0] = 0
        for i in range(1, len_nums + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], subarray_prefix[i] - subarray_prefix[k]))

        return dp[-1][-1]

    def _splitArrayBinarySearch(self, nums: List[int], m: int) -> int:
        """
        TODO
        Runtime: 43 ms, faster than 78.62% of Python3 online submissions for Split Array Largest Sum.
        Memory Usage: 14 MB, less than 37.77% of Python3 online submissions for Split Array Largest Sum.
        """
        def __check(target_sum: int) -> bool:
            cur_sum = 0
            split_counter = 1
            for num in nums:
                if cur_sum + num > target_sum:
                    split_counter += 1
                    cur_sum = num  # recover
                else:
                    cur_sum += num
            return split_counter <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) >> 1
            if __check(mid):
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 18
    nums = [7, 2, 5, 10, 8]
    m = 2

    # Example 2: Output: 9
    # nums = [1, 2, 3, 4, 5]
    # m = 2

    # Example 3: Output: 4
    # nums = [1, 4, 4]
    # m = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.splitArray(nums, m)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
