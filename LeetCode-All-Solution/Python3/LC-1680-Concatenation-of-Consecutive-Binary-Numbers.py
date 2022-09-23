#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1680-Concatenation-of-Consecutive-Binary-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-23
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1680 - (Medium) - Concatenation of Consecutive Binary Numbers
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

Description & Requirement:
    Given an integer n, return the decimal value of the binary string formed by 
    concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.

Example 1:
    Input: n = 1
    Output: 1
    Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:
    Input: n = 3
    Output: 27
    Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
        After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:
    Input: n = 12
    Output: 505379714
    Explanation: The concatenation results in "1101110010111011110001001101010111100".
        The decimal value of that is 118505380540.
        After modulo 10^9 + 7, the result is 505379714.

Constraints:
    1 <= n <= 10^5
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (simulation or math)
        return self._concatenatedBinary(n)

    def _concatenatedBinary(self, n: int) -> int:
        """
        Runtime: 3078 ms, faster than 38.58% of Python3 submissions for Concatenation of Consecutive Binary Numbers.
        Memory Usage: 13.8 MB, less than 97.64% of Python3 submissions for Concatenation of Consecutive Binary Numbers.
        """
        assert isinstance(n, int) and n >= 1

        MOD = int(1e9+7)

        res = 0
        shift = 0

        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                shift += 1
            res = ((res << shift) + i) % MOD

        return res


def main():
    # Example 1: Output: 1
    # n = 1

    # Example 2: Output: 27
    # n = 3

    # Example 3: Output: 505379714
    n = 12

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.concatenatedBinary(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
