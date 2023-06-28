#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1681-Minimum-Incompatibility.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-28
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1681 - (Hard) - Minimum Incompatibility
https://leetcode.com/problems/minimum-incompatibility/

Description & Requirement:
    You are given an integer array nums and an integer k. 
    You are asked to distribute this array into k subsets of equal size 
    such that there are no two equal elements in the same subset.

    A subset's incompatibility is the difference between 
    the maximum and minimum elements in that array.

    Return the minimum possible sum of incompatibilities of the k subsets 
    after distributing the array optimally, or return -1 if it is not possible.

    A subset is a group integers that appear in the array with no particular order.

Example 1:
    Input: nums = [1,2,1,4], k = 2
    Output: 4
    Explanation: The optimal distribution of subsets is [1,2] and [1,4].
        The incompatibility is (2-1) + (4-1) = 4.
        Note that [1,1] and [2,4] would result in a smaller sum, 
        but the first subset contains 2 equal elements.
Example 2:
    Input: nums = [6,3,8,1,3,1,2,2], k = 4
    Output: 6
    Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
        The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
Example 3:
    Input: nums = [5,3,3,6,3,3], k = 3
    Output: -1
    Explanation: It is impossible to distribute nums into 3 subsets 
        where no two elements are equal in the same subset.

Constraints:
    1 <= k <= nums.length <= 16
    nums.length is divisible by k
    1 <= nums[i] <= nums.length
"""


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(nums, list) and len(nums) >= k and len(nums) % k == 0
        # main method: (dynamic programming)
        return self._minimumIncompatibility(nums, k)

    def _minimumIncompatibility(self, nums: List[int], k: int) -> int:
        assert isinstance(k, int) and k >= 1
        assert isinstance(nums, list) and len(nums) >= k and len(nums) % k == 0

        INF = int(1e9+7)
        n = len(nums)
        dp = [INF] * (1 << n)
        dp[0] = 0
        group = n // k
        values = dict({})

        for mask in range(1 << n):
            if bin(mask).count("1") != group:
                continue
            mn = 20
            mx = 0
            cur = set()
            for i in range(n):
                if mask & (1 << i) > 0:
                    if nums[i] in cur:
                        break
                    cur.add(nums[i])
                    mn = min(mn, nums[i])
                    mx = max(mx, nums[i])
            if len(cur) == group:
                values[mask] = mx - mn

        for mask in range(1 << n):
            if dp[mask] == INF:
                continue

            seen = dict({})
            for i in range(n):
                if mask & (1 << i) == 0:
                    seen[nums[i]] = i
            if len(seen) < group:
                continue

            sub = 0
            for v in seen:
                sub |= 1 << seen[v]

            nxt = sub
            while nxt > 0:
                if nxt in values:
                    dp[mask | nxt] = min(dp[mask | nxt], dp[mask] + values[nxt])
                nxt = (nxt - 1) & sub

        return int(dp[-1]) if dp[-1] < INF else -1


def main():
    # Example 1: Output: 4
    # nums = [1, 2, 1, 4]
    # k = 2

    # Example 2: Output: 6
    nums = [6, 3, 8, 1, 3, 1, 2, 2]
    k = 4

    # Example 3: Output: -1
    # nums = [5, 3, 3, 6, 3, 3]
    # k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumIncompatibility(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
