#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0862-Shortest-Subarray-with-Sum-at-Least-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-26
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0862 - (Hard) - Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Description & Requirement:
    Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums 
    with a sum of at least k. If there is no such subarray, return -1.

    A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [1], k = 1
    Output: 1
Example 2:
    Input: nums = [1,2], k = 4
    Output: -1
Example 3:
    Input: nums = [2,-1,2], k = 3
    Output: 3

Constraints:
    1 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5
    1 <= k <= 10^9
"""


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 1 <= k
        # main method: (prefix sum)
        return self._shortestSubarray(nums, k)

    def _shortestSubarray(self, nums: List[int], k: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 1 <= k

        res = len(nums) + 1

        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        queue = collections.deque()
        for i, cur_sum in enumerate(pre_sum):
            while len(queue) > 0 and cur_sum - pre_sum[queue[0]] >= k:
                res = min(res, i - queue.popleft())
            while len(queue) > 0 and pre_sum[queue[-1]] >= cur_sum:
                queue.pop()
            queue.append(i)

        return res if res < len(nums) + 1 else -1


def main():
    # Example 1: Output: 1
    # nums = [1]
    # k = 1

    # Example 2: Output: -1
    # nums = [1, 2]
    # k = 4

    # Example 3: Output: 3
    nums = [2, -1, 2]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestSubarray(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
