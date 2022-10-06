#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0927-Three-Equal-Parts.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-06
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0927 - (Hard) - Three Equal Parts
https://leetcode.com/problems/three-equal-parts/

Description & Requirement:
    You are given an array arr which consists of only zeros and ones, 
    divide the array into three non-empty parts such that all of these parts represent the same binary value.

    If it is possible, return any [i, j] with i + 1 < j, such that:
        arr[0], arr[1], ..., arr[i] is the first part,
        arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
        arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
        All three parts have equal binary values.

    If it is not possible, return [-1, -1].

    Note that the entire part is used when considering what binary value it represents. 
    For example, [1,1,0] represents 6 in decimal, not 3. 
    Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

Example 1:
    Input: arr = [1,0,1,0,1]
    Output: [0,3]
Example 2:
    Input: arr = [1,1,0,1,1]
    Output: [-1,-1]
Example 3:
    Input: arr = [1,1,0,0,1]
    Output: [0,2]

Constraints:
    3 <= arr.length <= 3 * 10^4
    arr[i] is 0 or 1
"""


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 3
        for num in arr:
            assert isinstance(num, int) and (num == 0 or num == 1)
        # main method: (sliding window)
        return self._threeEqualParts(arr)

    def _threeEqualParts(self, arr: List[int]) -> List[int]:
        assert isinstance(arr, list) and len(arr) >= 3

        len_arr = len(arr)
        sum_arr = sum(arr)

        if sum_arr % 3:
            return [-1, -1]
        if sum_arr == 0:
            return [0, 2]

        trilogy = sum_arr // 3
        first = second = third = cur_sum = 0
        for i, x in enumerate(arr):
            if x:
                if cur_sum == 0:
                    first = i
                elif cur_sum == trilogy:
                    second = i
                elif cur_sum == (trilogy << 1):
                    third = i
                cur_sum += 1

        length = len_arr - third
        if first + length <= second and second + length <= third:
            i = 0
            while third + i < len_arr:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1
            return [first + length - 1, second + length]

        return [-1, -1]


def main():
    # Example 1: Output: [0,3]
    arr = [1, 0, 1, 0, 1]

    # Example 2: Output: [-1,-1]
    # arr = [1, 1, 0, 1, 1]

    # Example 3: Output: [0,2]
    # arr = [1, 1, 0, 0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.threeEqualParts(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
