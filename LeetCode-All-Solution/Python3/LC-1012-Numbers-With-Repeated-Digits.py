#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1012-Numbers-With-Repeated-Digits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-20
=================================================================="""

import sys
import time
# from typing import List
# import collections
import functools

"""
LeetCode - 1012 - (Hard) - Numbers With Repeated Digits
https://leetcode.com/problems/numbers-with-repeated-digits/

Description & Requirement:
    Given an integer n, return the number of positive integers in the range [1, n] 
    that have at least one repeated digit.

Example 1:
    Input: n = 20
    Output: 1
    Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:
    Input: n = 100
    Output: 10
    Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 
        11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:
    Input: n = 1000
    Output: 262

Constraints:
    1 <= n <= 10^9
"""


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (digit DP)
        return self._numDupDigitsAtMostN(n)

    def _numDupDigitsAtMostN(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        array = list(map(int, str(n)))
        len_a = len(array)

        @functools.lru_cache(maxsize=None)
        def dp(index, tight, mask, has_dup):
            if index >= len_a:
                return 1 if has_dup else 0

            res = 0
            upperbound = array[index] if tight else 9

            for ub in range(upperbound + 1):
                tight_new = tight and ub == upperbound
                mask_new = mask if (mask == 0 and ub == 0) else (mask | (1 << ub))
                has_dup_new = has_dup or (mask & (1 << ub))
                res += dp(index + 1, tight_new, mask_new, has_dup_new)

            return res

        return dp(0, True, 0, False)


def main():
    # Example 1: Output: 1
    # n = 20

    # Example 2: Output: 10
    # n = 100

    # Example 3: Output: 262
    n = 1000

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.numDupDigitsAtMostN(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
