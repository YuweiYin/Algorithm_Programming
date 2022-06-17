#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1089-Duplicate-Zeros.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-17
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1089 - (Easy) - Duplicate Zeros
https://leetcode.com/problems/duplicate-zeros/

Description & Requirement:
    Given a fixed-length integer array arr, duplicate each occurrence of zero, 
    shifting the remaining elements to the right.

    Note that elements beyond the length of the original array are not written. 
    Do the above modifications to the input array in place and do not return anything.

Example 1:
    Input: arr = [1,0,2,3,0,4,5,0]
    Output: [1,0,0,2,3,0,0,4]
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:
    Input: arr = [1,2,3]
    Output: [1,2,3]
    Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 9
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        for num in arr:
            assert isinstance(num, int) and 0 <= num <= 9
        # main method: (simulate stack & two pointers)
        self._duplicateZeros(arr)

    def _duplicateZeros(self, arr: List[int]) -> None:
        assert isinstance(arr, list) and len(arr) >= 1

        n = len(arr)
        stack_top = 0
        left = -1

        # simulate the stack pushing process, find the stack top index
        while stack_top < n:
            left += 1
            if arr[left] > 0:
                stack_top += 1
            else:
                stack_top += 2
        # adjust the last element
        right = n - 1
        if stack_top == n + 1:
            arr[right] = 0
            right -= 1
            left -= 1
        # modify the whole array
        while right >= 0:
            arr[right] = arr[left]
            right -= 1
            if arr[left] == 0:
                arr[right] = arr[left]
                right -= 1
            left -= 1


def main():
    # Example 1: Output: [1,0,0,2,3,0,0,4]
    arr = [1, 0, 2, 3, 0, 4, 5, 0]

    # Example 2: Output: [1,2,3]
    # arr = [1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.duplicateZeros(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(arr)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
