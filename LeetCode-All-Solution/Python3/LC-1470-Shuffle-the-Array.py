#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1470-Shuffle-the-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-29
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1470 - (Easy) - Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/

Description & Requirement:
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7] 
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:
    Input: nums = [1,2,3,4,4,3,2,1], n = 4
    Output: [1,4,2,3,3,2,4,1]
Example 3:
    Input: nums = [1,1,2,2], n = 2
    Output: [1,2,1,2]

Constraints:
    1 <= n <= 500
    nums.length == 2n
    1 <= nums[i] <= 10^3
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (split the list and combine together)
        return self._shuffle(nums, n)

    def _shuffle(self, nums: List[int], n: int) -> List[int]:
        assert isinstance(n, int) and n >= 1
        assert isinstance(nums, list) and len(nums) >= 1

        x_part = nums[:n]
        y_part = nums[n:]

        for idx in range(n):
            nums[idx << 1] = x_part[idx]
            nums[(idx << 1) + 1] = y_part[idx]

        return nums


def main():
    # Example 1: Output: [2,3,5,4,1,7]
    # nums = [2, 5, 1, 3, 4, 7]
    # n = 3

    # Example 2: Output: [1,4,2,3,3,2,4,1]
    # nums = [1, 2, 3, 4, 4, 3, 2, 1]
    # n = 4

    # Example 3: Output: [1,2,1,2]
    nums = [1, 1, 2, 2]
    n = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shuffle(nums, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
