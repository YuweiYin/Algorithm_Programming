#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1053-Previous-Permutation-With-One-Swap.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1053 - (Medium) - Previous Permutation With One Swap
https://leetcode.com/problems/previous-permutation-with-one-swap/

Description & Requirement:
    Given an array of positive integers arr (not necessarily distinct), 
    return the lexicographically largest permutation that is smaller than arr, 
    that can be made with exactly one swap. If it cannot be done, then return the same array.

    Lexicographically Smaller: An array a is lexicographically smaller than an array b 
        if in the first position where a and b differ, array a has an element that is less than 
        the corresponding element in b. If the first min(a.length, b.length) elements do not differ, 
        then the shorter array is the lexicographically smaller one.

    Note that a swap exchanges the positions of two numbers arr[i] and arr[j]

Example 1:
    Input: arr = [3,2,1]
    Output: [3,1,2]
    Explanation: Swapping 2 and 1.
Example 2:
    Input: arr = [1,1,5]
    Output: [1,1,5]
    Explanation: This is already the smallest permutation.
Example 3:
    Input: arr = [1,9,4,6,7]
    Output: [1,7,4,6,9]
    Explanation: Swapping 9 and 7.

Constraints:
    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^4
"""


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        # main method: (greedily scan)
        return self._prevPermOpt1(arr)

    def _prevPermOpt1(self, arr: List[int]) -> List[int]:
        assert isinstance(arr, list) and len(arr) >= 1

        len_arr = len(arr)
        for i in range(len_arr - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                j = len_arr - 1
                while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break

        return arr


def main():
    # Example 1: Output: [3,1,2]
    # arr = [3, 2, 1]

    # Example 2: Output: [1,1,5]
    # arr = [1, 1, 5]

    # Example 3: Output: [1,7,4,6,9]
    arr = [1, 9, 4, 6, 7]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.prevPermOpt1(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
