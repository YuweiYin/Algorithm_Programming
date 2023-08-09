#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2616-Minimize-the-Maximum-Difference-of-Pairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-09
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2616 - (Medium) - Minimize the Maximum Difference of Pairs
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

Description & Requirement:
    You are given a 0-indexed integer array nums and an integer p. 
    Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. 
    Also, ensure no index appears more than once amongst the p pairs.

    Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, 
    where |x| represents the absolute value of x.

    Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

Example 1:
    Input: nums = [10,1,2,7,1,3], p = 2
    Output: 1
    Explanation: The first pair is formed from the indices 1 and 4, 
        and the second pair is formed from the indices 2 and 5. 
        The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. 
        Therefore, we return 1.
Example 2:
    Input: nums = [4,2,1,2], p = 1
    Output: 0
    Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, 
        which is the minimum we can attain.

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    0 <= p <= (nums.length)/2
"""


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(p, int) and p >= 0
        # main method: (sorting and binary search)
        return self._minimizeMax(nums, p)

    def _minimizeMax(self, nums: List[int], p: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(p, int) and p >= 0

        nums.sort()

        def __check(mx: int) -> bool:
            cnt = i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mx:
                    i += 2
                    cnt += 1
                else:
                    i += 1
            return cnt >= p

        left = 0
        right = nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) >> 1
            if __check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 1
    # nums = [10, 1, 2, 7, 1, 3]
    # p = 2

    # Example 2: Output: 0
    # nums = [4, 2, 1, 2]
    # p = 1

    # Example 3: Output: 0
    nums = [4, 0, 2, 1, 2, 5, 5, 3]
    p = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimizeMax(nums, p)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
