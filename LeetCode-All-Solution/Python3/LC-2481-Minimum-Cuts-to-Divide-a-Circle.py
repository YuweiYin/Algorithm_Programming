#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2481-Minimum-Cuts-to-Divide-a-Circle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-17
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2481 - (Hard) - Minimum Cuts to Divide a Circle
https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

Description & Requirement:
    A valid cut in a circle can be:
        A cut that is represented by a straight line that touches two points 
            on the edge of the circle and passes through its center, or
        A cut that is represented by a straight line that touches one point 
            on the edge of the circle and its center.

    Some valid and invalid cuts are shown in the figures below.

    Given the integer n, return the minimum number of cuts needed to divide a circle into n equal slices.

Example 1:
    Input: n = 4
    Output: 2
    Explanation:
        The above figure shows how cutting the circle twice 
        through the middle divides it into 4 equal slices.
Example 2:
    Input: n = 3
    Output: 3
    Explanation:
        At least 3 cuts are needed to divide the circle into 3 equal slices. 
        It can be shown that less than 3 cuts cannot result in 3 slices of equal size and shape.
        Also note that the first cut will not divide the circle into distinct parts.

Constraints:
    1 <= n <= 100
"""


class Solution:
    def numberOfCuts(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (different cases)
        return self._numberOfCuts(n)

    def _numberOfCuts(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        if n == 1:
            return 0
        if n % 2 == 0:
            return n >> 1

        return n


def main():
    # Example 1: Output: 2
    n = 4

    # Example 2: Output: 3
    # n = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfCuts(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
