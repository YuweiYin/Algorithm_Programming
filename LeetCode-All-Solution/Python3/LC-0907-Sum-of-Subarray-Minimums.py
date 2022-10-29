#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0907-Sum-of-Subarray-Minimums.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-28
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0907 - (Medium) - Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/

Description & Requirement:
    Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. 
    Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
    Input: arr = [3,1,2,4]
    Output: 17
    Explanation: 
        Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
        Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
        Sum is 17.
Example 2:
    Input: arr = [11,81,94,43,3]
    Output: 444

Constraints:
    1 <= arr.length <= 3 * 10^4
    1 <= arr[i] <= 3 * 10^4
"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        # main method: (monotonous stack)
        return self._sumSubarrayMins(arr)

    def _sumSubarrayMins(self, arr: List[int]) -> int:
        assert isinstance(arr, list) and len(arr) >= 1

        MOD = int(1e9+7)
        n = len(arr)

        mono_stack = []
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        for i, x in enumerate(arr):
            while len(mono_stack) > 0 and x <= arr[mono_stack[-1]]:
                mono_stack.pop()
            left[i] = i - (mono_stack[-1] if mono_stack else -1)
            mono_stack.append(i)

        mono_stack = []
        for i in range(n - 1, -1, -1):
            while len(mono_stack) > 0 and arr[i] < arr[mono_stack[-1]]:
                mono_stack.pop()
            right[i] = (mono_stack[-1] if mono_stack else n) - i
            mono_stack.append(i)

        res = 0
        for l, r, x in zip(left, right, arr):
            res = (res + l * r * x) % MOD

        return res


def main():
    # Example 1: Output: 17
    # arr = [3, 1, 2, 4]

    # Example 2: Output: 444
    arr = [11, 81, 94, 43, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sumSubarrayMins(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
