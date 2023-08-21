#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2235-Add-Two-Integers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-19
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2235 - (Easy) Add Two Integers
https://leetcode.com/problems/add-two-integers/description/

Description & Requirement:
    Given two integers num1 and num2, return the sum of the two integers.

Example 1:
    Input: num1 = 12, num2 = 5
    Output: 17
    Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
Example 2:
    Input: num1 = -10, num2 = 4
    Output: -6
    Explanation: num1 + num2 = -6, so -6 is returned.

Constraints:
    -100 <= num1, num2 <= 100
"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # exception case
        assert isinstance(num1, int) and isinstance(num2, int)
        return num1 + num2


def main():
    # Example 1: Output: 17
    num1 = 12
    num2 = 5

    # Example 2: Output: -6
    # num1 = -10
    # num2 = 4

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.sum(num1, num2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
