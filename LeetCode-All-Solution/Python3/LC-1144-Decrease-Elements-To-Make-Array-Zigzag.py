#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1144-Decrease-Elements-To-Make-Array-Zigzag.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1144 - (Medium) - Decrease Elements To Make Array Zigzag
https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

Description & Requirement:
    Given an array nums of integers, 
    a move consists of choosing any element and decreasing it by 1.

    An array A is a zigzag array if either:
        Every even-indexed element is greater than adjacent elements, 
            ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
        OR, every odd-indexed element is greater than adjacent elements, 
            ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...

    Return the minimum number of moves to transform the given array nums into a zigzag array.

Example 1:
    Input: nums = [1,2,3]
    Output: 2
    Explanation: We can decrease 2 to 0 or 3 to 1.
Example 2:
    Input: nums = [9,6,1,6,2]
    Output: 4

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
"""


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (greedily decrease either odd index or even index)
        return self._movesToMakeZigzag(nums)

    def _movesToMakeZigzag(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        def _decrease(pos: int) -> int:
            res = 0

            for idx in range(pos, len(nums), 2):
                n_ops = 0
                if idx - 1 >= 0:
                    n_ops = max(n_ops, nums[idx] - nums[idx - 1] + 1)
                if idx + 1 < len(nums):
                    n_ops = max(n_ops, nums[idx] - nums[idx + 1] + 1)
                res += n_ops

            return res

        return min(_decrease(0), _decrease(1))


def main():
    # Example 1: Output: 2
    # nums = [1, 2, 3]

    # Example 2: Output: 4
    nums = [9, 6, 1, 6, 2]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.movesToMakeZigzag(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
