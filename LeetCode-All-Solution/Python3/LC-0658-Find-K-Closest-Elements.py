#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0658-Find-K-Closest-Elements.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-25
=================================================================="""

import sys
import time
from typing import List
import bisect
# import collections
# import functools

"""
LeetCode - 0658 - (Medium) - Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

Description & Requirement:
    Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
    The result should also be sorted in ascending order.

    An integer a is closer to x than an integer b if:
        |a - x| < |b - x|, or
        |a - x| == |b - x| and a < b

Example 1:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
Example 2:
    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]

Constraints:
    1 <= k <= arr.length
    1 <= arr.length <= 10^4
    arr is sorted in ascending order.
    -10^4 <= arr[i], x <= 10^4
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # exception case
        assert isinstance(x, int)
        assert isinstance(k, int) and k >= 1
        assert isinstance(arr, list) and len(arr) >= k
        # main method: (binary search + double pointers)
        return self._findClosestElements(arr, k, x)

    def _findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        assert isinstance(x, int)
        assert isinstance(k, int) and k >= 1
        assert isinstance(arr, list) and len(arr) >= k

        len_arr = len(arr)
        right_idx = bisect.bisect_left(arr, x)
        left_idx = right_idx - 1

        for _ in range(k):
            if left_idx < 0:
                right_idx += 1
            elif right_idx >= len(arr) or x - arr[left_idx] <= arr[right_idx] - x:
                left_idx -= 1
            else:
                right_idx += 1

        return arr[left_idx + 1: right_idx]


def main():
    # Example 1: Output: [1,2,3,4]
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3

    # Example 2: Output: [1,2,3,4]
    # arr = [1, 2, 3, 4, 5]
    # k = 4
    # x = -1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findClosestElements(arr, k, x)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
