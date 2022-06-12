#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1695-Maximum-Erasure-Value.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1695 - (Medium) - Maximum Erasure Value
https://leetcode.com/problems/maximum-erasure-value/

Description & Requirement:
    You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
    The score you get by erasing the subarray is equal to the sum of its elements.

    Return the maximum score you can get by erasing exactly one subarray.

    An array b is called to be a subarray of a if it forms a contiguous subsequence of a, 
    that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray here is [2,4,5,6].
Example 2:
    Input: nums = [5,2,1,2,5,2,1,2,5]
    Output: 8
    Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (sliding window)
        return self._maximumUniqueSubarray(nums)

    def _maximumUniqueSubarray(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)

        num_counter = dict({})  # key: number; value: counter of the number in the current window

        res = 0
        cur_sum = 0
        left = 0
        for right in range(0, len_nums):
            cur_num = nums[right]
            while cur_num in num_counter and num_counter[cur_num] > 0 and left < right:
                left_num = nums[left]
                assert left_num in num_counter and num_counter[left_num] > 0
                num_counter[left_num] -= 1
                cur_sum -= left_num
                left += 1
            cur_sum += cur_num
            if cur_num in num_counter:
                num_counter[cur_num] += 1
            else:
                num_counter[cur_num] = 1
            res = max(res, cur_sum)

        return res


def main():
    # Example 1: Output: 17
    nums = [4, 2, 4, 5, 6]

    # Example 2: Output: 8
    # nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumUniqueSubarray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
