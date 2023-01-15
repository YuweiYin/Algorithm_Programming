#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2293-Min-Max-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2293 - (Easy) - Min Max Game
https://leetcode.com/problems/min-max-game/

Description & Requirement:
    You are given a 0-indexed integer array nums whose length is a power of 2.

    Apply the following algorithm on nums:
        Let n be the length of nums. If n == 1, end the process. 
            Otherwise, create a new 0-indexed integer array newNums of length n / 2
        For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1])
        For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1])

    Replace the array nums with newNums.
    Repeat the entire process starting from step 1.

    Return the last number that remains in nums after applying the algorithm.

Example 1:
    Input: nums = [1,3,5,2,4,8,2,2]
    Output: 1
    Explanation: The following arrays are the results of applying the algorithm repeatedly.
        First: nums = [1,5,4,2]
        Second: nums = [1,4]
        Third: nums = [1]
        1 is the last remaining number, so we return 1.
Example 2:
    Input: nums = [3]
    Output: 3
    Explanation: 3 is already the last remaining number, so we return 3.

Constraints:
    1 <= nums.length <= 1024
    1 <= nums[i] <= 10^9
    nums.length is a power of 2.
"""


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (recursion)
        return self._minMaxGame(nums)

    def _minMaxGame(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        n = len(nums)
        if n == 1:
            return nums[0]

        new_nums = [0] * (n >> 1)

        for i in range(n >> 1):
            i_2 = i << 1
            if i & 0x01 == 0:
                new_nums[i] = min(nums[i_2], nums[i_2 + 1])
            else:
                new_nums[i] = max(nums[i_2], nums[i_2 + 1])

        return self._minMaxGame(new_nums)


def main():
    # Example 1: Output: 1
    nums = [1, 3, 5, 2, 4, 8, 2, 2]

    # Example 2: Output: 3
    # nums = [3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minMaxGame(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
