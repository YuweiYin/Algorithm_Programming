#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0941-Valid-Mountain-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-25
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0941 - (Easy) - Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/

Description & Requirement:
    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:
        arr.length >= 3
        There exists some i with 0 < i < arr.length - 1 such that:
            arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
    Input: arr = [2,1]
    Output: false
Example 2:
    Input: arr = [3,5,5]
    Output: false
Example 3:
    Input: arr = [0,3,2,1]
    Output: true

Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^4
"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # exception case
        if not isinstance(arr, list) or len(arr) <= 0:
            return False  # Error input type
        if len(arr) < 3:
            return False
        # main method: (scan: from index 0, find num in ascending order till the max,
        #     then scan to end in descending order. If this process is all OK, then arr is a mountain array, else not)
        return self._validMountainArray(arr)

    def _validMountainArray(self, arr: List[int]) -> bool:
        len_arr = len(arr)
        assert len_arr >= 3

        cur_index = 0
        while cur_index < len_arr - 1:  # scan, in ascending order, find peak
            if arr[cur_index + 1] > arr[cur_index]:
                cur_index += 1
            else:
                break
        if cur_index == 0 or cur_index == len_arr - 1:  # peak is at the first or last index
            return False

        # now, arr[cur_index] is the mountain peak
        while cur_index < len_arr - 1:  # scan, in descending order, till the end
            if arr[cur_index + 1] < arr[cur_index]:
                cur_index += 1
            else:
                return False  # not in descending order

        return True


def main():
    # Example 1: Output: false
    # arr = [2, 1]

    # Example 2: Output: false
    # arr = [3, 5, 5]

    # Example 3: Output: true
    # arr = [0, 3, 2, 1]

    # Example 4: Output: false
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.validMountainArray(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
