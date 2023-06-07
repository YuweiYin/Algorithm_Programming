#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1318-Minimum-Flips-to-Make-a-OR-b-Equal-to-c.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-07
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1318 - (Medium) - Minimum Flips to Make a OR b Equal to c
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

Description & Requirement:
    Given 3 positives numbers a, b and c. Return the minimum flips required in some bits 
    of a and b to make ( a OR b == c ). (bitwise OR operation).

    Flip operation consists of change any single bit 1 to 0 or 
    change the bit 0 to 1 in their binary representation.

Example 1:
    Input: a = 2, b = 6, c = 5
    Output: 3
    Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:
    Input: a = 4, b = 2, c = 7
    Output: 1
Example 3:
    Input: a = 1, b = 2, c = 3
    Output: 0

Constraints:
    1 <= a <= 10^9
    1 <= b <= 10^9
    1 <= c <= 10^9
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # exception case
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and b >= 1
        assert isinstance(c, int) and c >= 1
        # main method: (bit manipulation)
        return self._minFlips(a, b, c)

    def _minFlips(self, a: int, b: int, c: int) -> int:
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and b >= 1
        assert isinstance(c, int) and c >= 1

        res = 0
        MAX_BIT = 32
        for i in range(MAX_BIT):
            bit_a, bit_b, bit_c = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            if bit_c == 0:
                res += bit_a + bit_b
            else:
                if (bit_a + bit_b) == 0:
                    res += 1

        return res


def main():
    # Example 1: Output: 3
    # a = 2
    # b = 6
    # c = 5

    # Example 2: Output: 1
    # a = 4
    # b = 2
    # c = 7

    # Example 3: Output: 0
    a = 1
    b = 2
    c = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minFlips(a, b, c)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
