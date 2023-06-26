#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2485-Find-the-Pivot-Integer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-26
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2485 - (Easy) - Find the Pivot Integer
https://leetcode.com/problems/find-the-pivot-integer/

Description & Requirement:
    Given a positive integer n, find the pivot integer x such that:
        The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

    Return the pivot integer x. If no such integer exists, return -1. 
    It is guaranteed that there will be at most one pivot index for the given input.

Example 1:
    Input: n = 8
    Output: 6
    Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:
    Input: n = 1
    Output: 1
    Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:
    Input: n = 4
    Output: -1
    Explanation: It can be proved that no such integer exist.

Constraints:
    1 <= n <= 1000
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (mathematics)
        return self._pivotInteger(n)

    def _pivotInteger(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        t = (n * n + n) >> 1
        x = int(t ** 0.5)

        return x if x * x == t else -1


def main():
    # Example 1: Output: 6
    n = 8

    # Example 2: Output: 1
    # n = 1

    # Example 3: Output: -1
    # n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pivotInteger(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
