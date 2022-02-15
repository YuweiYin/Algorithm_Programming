#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0118-Pascals-Triangle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-15
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0118 - (Easy) - Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Description & Requirement:
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # exception case
        assert isinstance(numRows, int) and numRows > 0
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        # main method: (from the ends to the center, 1-Dim Dynamic Programming)
        return self._generate(numRows)

    def _generate(self, numRows: int) -> List[List[int]]:
        """
        Runtime: 28 ms, faster than 92.48% of Python3 online submissions for Pascal's Triangle.
        Memory Usage: 13.9 MB, less than 91.64% of Python3 online submissions for Pascal's Triangle.
        """
        assert isinstance(numRows, int) and numRows > 2

        res = [[1], [1, 1]]
        while numRows > 2:
            last_layer = res[-1]
            new_layer = [1] + [0 for _ in range(len(last_layer) - 1)] + [1]  # construct new layer
            new_layer_len = len(new_layer)
            for index in range(1, (new_layer_len >> 1) + 1):  # deal with the left half
                new_layer[index] = last_layer[index - 1] + last_layer[index]  # get sum from the last layer
                new_layer[new_layer_len - 1 - index] = new_layer[index]  # copy the left one to its right counterpart
            res.append(new_layer)  # done new layer, push it in
            numRows -= 1

        return res


def main():
    # Example 1: Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    numRows = 5

    # Example 2: Output: [[1]]
    # numRows = 1

    # Example 3: Output:
    # numRows = 30

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.generate(numRows)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
