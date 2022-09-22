#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1640-Check-Array-Formation-Through-Concatenation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-22
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1640 - (Easy) - Check Array Formation Through Concatenation
https://leetcode.com/problems/check-array-formation-through-concatenation/

Description & Requirement:
    You are given an array of distinct integers arr and an array of integer arrays pieces, 
    where the integers in pieces are distinct. 
    Your goal is to form arr by concatenating the arrays in pieces in any order. 
    However, you are not allowed to reorder the integers in each array pieces[i].

    Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:
    Input: arr = [15,88], pieces = [[88],[15]]
    Output: true
    Explanation: Concatenate [15] then [88]
Example 2:
    Input: arr = [49,18,16], pieces = [[16,18,49]]
    Output: false
    Explanation: Even though the numbers match, we cannot reorder pieces[0].
Example 3:
    Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
    Output: true
    Explanation: Concatenate [91] then [4,64] then [78]

Constraints:
    1 <= pieces.length <= arr.length <= 100
    sum(pieces[i].length) == arr.length
    1 <= pieces[i].length <= arr.length
    1 <= arr[i], pieces[i][j] <= 100
    The integers in arr are distinct.
    The integers in pieces are distinct 
        (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # exception case
        assert isinstance(arr, list) and isinstance(pieces, list) and len(arr) >= len(pieces) >= 1
        len_arr = len(arr)
        for piece in pieces:
            assert isinstance(piece, list) and 1 <= len(piece) <= len_arr
        for num in arr:
            assert isinstance(num, int) and num >= 1
        # main method: (hash dict)
        return self._canFormArray(arr, pieces)

    def _canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        assert isinstance(arr, list) and isinstance(pieces, list) and len(arr) >= len(pieces) >= 1

        index_dict = dict({piece[0]: idx for idx, piece in enumerate(pieces)})
        idx = 0

        while idx < len(arr):
            if arr[idx] not in index_dict:
                return False
            p = pieces[index_dict[arr[idx]]]
            if arr[idx: idx + len(p)] != p:
                return False
            idx += len(p)

        return True


def main():
    # Example 1: Output: true
    # arr = [15, 88]
    # pieces = [[88], [15]]

    # Example 2: Output: false
    # arr = [49, 18, 16]
    # pieces = [[16, 18, 49]]

    # Example 3: Output: true
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canFormArray(arr, pieces)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
