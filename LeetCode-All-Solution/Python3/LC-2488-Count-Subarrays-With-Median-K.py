#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2488-Count-Subarrays-With-Median-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-16
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2488 - (Hard) - Count Subarrays With Median K
https://leetcode.com/problems/count-subarrays-with-median-k/

Description & Requirement:
    You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.

    Return the number of non-empty subarrays in nums that have a median equal to k.

    Note:
        The median of an array is the middle element after sorting the array in ascending order. 
            If the array is of even length, the median is the left middle element.
        For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.

    A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [3,2,1,4,5], k = 4
    Output: 3
    Explanation: The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].
Example 2:
    Input: nums = [2,3,1], k = 3
    Output: 1
    Explanation: [3] is the only subarray that has a median equal to 3.

Constraints:
    n == nums.length
    1 <= n <= 10^5
    1 <= nums[i], k <= n
    The integers in nums are distinct.
"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 1 <= k <= len(nums)
        # main method: (prefix sum)
        return self._countSubarrays(nums, k)

    def _countSubarrays(self, nums: List[int], k: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 1 <= k <= len(nums)

        def __sign(num: int) -> int:
            return (num > 0) - (num < 0)

        res = 0

        k_index = nums.index(k)
        cur_sum = 0

        cnt = collections.Counter()
        cnt[0] = 1

        for idx, num in enumerate(nums):
            cur_sum += __sign(num - k)
            if idx < k_index:
                cnt[cur_sum] += 1
            else:
                res += cnt[cur_sum] + cnt[cur_sum - 1]

        return res


def main():
    # Example 1: Output: 3
    nums = [3, 2, 1, 4, 5]
    k = 4

    # Example 2: Output: 1
    # nums = [2, 3, 1]
    # k = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.countSubarrays(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
