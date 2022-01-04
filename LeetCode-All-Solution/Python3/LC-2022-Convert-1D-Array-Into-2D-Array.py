#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2022-Convert-1D-Array-Into-2D-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 2022 - (Easy) - Convert 1D Array Into 2D Array
https://leetcode.com/problems/convert-1d-array-into-2d-array/

Description:
    You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. 
    You are tasked with creating a 2-dimensional (2D) array with m rows and n columns 
    using all the elements from original.

    The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, 
    the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

    Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

Requirement:
    You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: original = [1,2,3,4], m = 2, n = 2
    Output: [[1,2],[3,4]]
    Explanation: The constructed 2D array should contain 2 rows and 2 columns.
        The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
        The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
Example 2:
    Input: original = [1,2,3], m = 1, n = 3
    Output: [[1,2,3]]
    Explanation: The constructed 2D array should contain 1 row and 3 columns.
        Put all three elements in original into the first row of the constructed 2D array.
Example 3:
    Input: original = [1,2], m = 1, n = 1
    Output: []
    Explanation: There are 2 elements in original.
        It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.

Constraints:
    1 <= original.length <= 5 * 10^4
    1 <= original[i] <= 10^5
    1 <= m, n <= 4 * 10^4
"""


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # exception case
        if not isinstance(original, list) or len(original) <= 0 or m <= 0 or n <= 0 or (len(original) != m * n):
            return []
        # main method: (reverse list in place)
        return self._construct2DArray(original, m, n)

    def _construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res_2d_list = []
        cur_start_index = 0
        cur_row = 1
        len_ori = len(original)
        while cur_start_index < len_ori and cur_row <= m:
            cur_end_index = min(len_ori, cur_row * n)
            res_2d_list.append(original[cur_start_index: cur_end_index])
            cur_start_index = cur_end_index
            cur_row += 1
        return res_2d_list


def main():
    # Example 1: Output: [[1,2],[3,4]]
    original = [1, 2, 3, 4]
    m = 2
    n = 2

    # Example 2: Output: [[1,2,3]]
    # original = [1, 2, 3]
    # m = 1
    # n = 3

    # Example 3: Output: []
    # original = [1, 2]
    # m = 1
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.construct2DArray(original, m, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
