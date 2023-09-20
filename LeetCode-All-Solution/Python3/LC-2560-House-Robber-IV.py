#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2560-House-Robber-IV.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2560 - (Medium) House Robber IV
https://leetcode.com/problems/house-robber-iv/

Description & Requirement:
    There are several consecutive houses along a street, each of which has some money inside. 
    There is also a robber, who wants to steal money from the homes, 
    but he refuses to steal from adjacent homes.

    The capability of the robber is the maximum amount of money he steals 
    from one house of all the houses he robbed.

    You are given an integer array nums representing how much money is stashed in each house. 
    More formally, the ith house from the left has nums[i] dollars.

    You are also given an integer k, representing the minimum number of houses 
    the robber will steal from. It is always possible to steal at least k houses.

    Return the minimum capability of the robber out of all the possible ways 
    to steal at least k houses.

Example 1:
    Input: nums = [2,3,5,9], k = 2
    Output: 5
    Explanation: 
        There are three ways to rob at least 2 houses:
        - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
        - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
        - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
        Therefore, we return min(5, 9, 9) = 5.
Example 2:
    Input: nums = [2,7,9,3,1], k = 2
    Output: 2
    Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability 
        is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= (nums.length + 1)/2
"""


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (Binary Search - Dynamic Programming)
        return self._minCapability(nums, k)

    def _minCapability(self, nums: List[int], k: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1

        def __check(target: int) -> bool:
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= target:
                    count += 1
                    i += 1
                i += 1
            return count >= k

        left = min(nums)
        right = max(nums)
        res = 0
        while left <= right:
            # mid = left + ((right - left) >> 1)
            mid = (left + right) >> 1
            if __check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


def main():
    # Example 1: Output: 5
    # nums = [2, 3, 5, 9]
    # k = 2

    # Example 2: Output: 2
    nums = [2, 7, 9, 3, 1]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minCapability(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
