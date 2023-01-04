#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1802-Maximum-Value-at-a-Given-Index-in-a-Bounded-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1802 - (Medium) - Maximum Value at a Given Index in a Bounded Array
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

Description & Requirement:
    You are given three positive integers: n, index, and maxSum. 
    You want to construct an array nums (0-indexed) that satisfies the following conditions:
        nums.length == n
        nums[i] is a positive integer where 0 <= i < n.
        abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
        The sum of all the elements of nums does not exceed maxSum.
        nums[index] is maximized.

    Return nums[index] of the constructed array.

    Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:
    Input: n = 4, index = 2,  maxSum = 6
    Output: 2
    Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
        There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:
    Input: n = 6, index = 1,  maxSum = 10
    Output: 3

Constraints:
    1 <= n <= maxSum <= 10^9
    0 <= index < n
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # exception case
        assert isinstance(n, int) and isinstance(maxSum, int) and maxSum >= n >= 1
        assert isinstance(index, int) and n >= index >= 0
        # main method: (greedy & binary search)
        return self._maxValue(n, index, maxSum)

    def _maxValue(self, n: int, index: int, maxSum: int) -> int:
        assert isinstance(n, int) and isinstance(maxSum, int) and maxSum >= n >= 1
        assert isinstance(index, int) and n >= index >= 0

        def __valid(_mid: int, _n: int, _index: int, _maxSum: int) -> bool:
            _left = _index
            _right = _n - _index - 1
            return _mid + __cal(_mid, _left) + __cal(_mid, _right) <= _maxSum

        def __cal(large: int, length: int) -> int:
            if length + 1 < large:
                small = large - length
                return ((large - 1 + small) * length) >> 1
            else:
                ones = length - (large - 1)
                return ((large - 1 + 1) * (large - 1) >> 1) + ones

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if __valid(mid, n, index, maxSum):
                left = mid
            else:
                right = mid - 1

        return left


def main():
    # Example 1: Output: 2
    # n, index, maxSum = 4, 2, 6

    # Example 2: Output: 3
    n, index, maxSum = 6, 1, 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxValue(n, index, maxSum)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
