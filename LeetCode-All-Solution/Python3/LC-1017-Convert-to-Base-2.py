#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1017-Convert-to-Base-2.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-06
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1017 - (Medium) - Convert to Base -2
https://leetcode.com/problems/convert-to-base-2/

Description & Requirement:
    Given an integer n, return a binary string representing its representation in base -2.

    Note that the returned string should not have leading zeros unless the string is "0".

Example 1:
    Input: n = 2
    Output: "110"
    Explantion: (-2)^2 + (-2)^1 = 2
Example 2:
    Input: n = 3
    Output: "111"
    Explantion: (-2)^2 + (-2)^1 + (-2)^0 = 3
Example 3:
    Input: n = 4
    Output: "100"
    Explantion: (-2)^2 = 4

Constraints:
    0 <= n <= 10^9
"""


class Solution:
    def baseNeg2(self, n: int) -> str:
        # exception case
        assert isinstance(n, int) and n >= 0
        # main method: (digits conversion)
        return self._baseNeg2(n)

    def _baseNeg2(self, n: int) -> str:
        assert isinstance(n, int) and n >= 0

        if n == 0 or n == 1:
            return str(n)

        res = []
        while n:
            remainder = n & 0x01
            res.append(str(remainder))
            n -= remainder
            n //= -2

        return "".join(res[::-1])


def main():
    # Example 1: Output: "110"
    # n = 2

    # Example 2: Output: "111"
    # n = 3

    # Example 3: Output: "100"
    n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.baseNeg2(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
