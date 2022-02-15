#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0119-Pascals-Triangle-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-15
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0119 - (Easy) - Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Description & Requirement:
    Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
    Input: rowIndex = 3
    Output: [1,3,3,1]
Example 2:
    Input: rowIndex = 0
    Output: [1]
Example 3:
    Input: rowIndex = 1
    Output: [1,1]

Constraints:
    0 <= rowIndex <= 33

Follow up:
    Could you optimize your algorithm to use only O(rowIndex) extra space?
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # exception case
        assert isinstance(rowIndex, int) and rowIndex >= 0
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        # main method: (from the ends to the center, 1-Dim Dynamic Programming)
        return self._getRow(rowIndex)

    def _getRow(self, rowIndex: int) -> List[int]:
        assert isinstance(rowIndex, int) and rowIndex > 1

        res = [1, 1]
        while rowIndex > 1:
            new_layer = [1] + [0 for _ in range(len(res) - 1)] + [1]  # construct new layer
            new_layer_len = len(new_layer)
            for index in range(1, (new_layer_len >> 1) + 1):  # deal with the left half
                new_layer[index] = res[index - 1] + res[index]  # get sum from the last layer
                new_layer[new_layer_len - 1 - index] = new_layer[index]  # copy the left one to its right counterpart
            res= new_layer  # done new layer, push it in
            rowIndex -= 1

        return res


def main():
    # Example 1: Output: [1,3,3,1]
    rowIndex = 3

    # Example 2: Output: [1]
    # rowIndex = 0

    # Example 3: Output: [1,1]
    # rowIndex = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getRow(rowIndex)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
