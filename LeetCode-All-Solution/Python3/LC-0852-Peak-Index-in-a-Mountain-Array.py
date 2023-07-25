#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0852-Peak-Index-in-a-Mountain-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-25
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 0852 - (Medium) - Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Description & Requirement:
    An array arr a mountain if the following properties hold:
        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            - arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
            - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Given a mountain array arr, return the index i such that 
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

    You must solve it in O(log(arr.length)) time complexity.

Example 1:
    Input: arr = [0,1,0]
    Output: 1
Example 2:
    Input: arr = [0,2,1,0]
    Output: 1
Example 3:
    Input: arr = [0,10,5,2]
    Output: 1

Constraints:
    3 <= arr.length <= 10^5
    0 <= arr[i] <= 10^6
    arr is guaranteed to be a mountain array.
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 3
        # main method: (binary search)
        return self._peakIndexInMountainArray(arr)

    def _peakIndexInMountainArray(self, arr: List[int]) -> int:
        assert isinstance(arr, list) and len(arr) >= 3

        n = len(arr)
        left, right, res = 1, n - 2, 0

        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] > arr[mid + 1]:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


def main():
    # Example 1: Output: 1
    # arr = [0, 1, 0]

    # Example 2: Output: 1
    # arr = [0, 2, 1, 0]

    # Example 3: Output: 1
    arr = [0, 10, 5, 2]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.peakIndexInMountainArray(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
