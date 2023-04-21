#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2413-Smallest-Even-Multiple.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-21
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2413 - (Easy) - Smallest Even Multiple
https://leetcode.com/problems/smallest-even-multiple/

Description & Requirement:
    Given a positive integer n, return the smallest positive integer 
    that is a multiple of both 2 and n.

Example 1:
    Input: n = 5
    Output: 10
    Explanation: The smallest multiple of both 5 and 2 is 10.
Example 2:
    Input: n = 6
    Output: 6
    Explanation: The smallest multiple of both 6 and 2 is 6. 
        Note that a number is a multiple of itself.

Constraints:
    1 <= n <= 150
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (odd / even)
        return self._smallestEvenMultiple(n)

    def _smallestEvenMultiple(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        return n if (n & 0x01 == 0) else (n << 1)


def main():
    # Example 1: Output: 10
    n = 5

    # Example 2: Output: 6
    # n = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestEvenMultiple(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
