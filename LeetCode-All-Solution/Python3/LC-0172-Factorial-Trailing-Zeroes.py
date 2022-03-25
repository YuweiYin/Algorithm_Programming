#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0172-Factorial-Trailing-Zeroes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-25
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0172 - (Medium) - Factorial Trailing Zeroes
https://leetcode.com/problems/factorial-trailing-zeroes/

Description & Requirement:
    Given an integer n, return the number of trailing zeroes in n!.

    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
    Input: n = 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.
Example 2:
    Input: n = 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.
Example 3:
    Input: n = 0
    Output: 0

Constraints:
    0 <= n <= 10^4
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return 0
        # main method: (1. simulate the process, record and remove every trailing 0)
        #     apparently, a num ends with 1/3/7/9 won't gain any trailing 0
        # 2. Math: to get trailing 10, 5^x and 2^y are needed, and 2 is far more abundant than 5, so only consider 5
        #     5^1 contributes one 5, 5^2 contributes one 5s, and so on
        #     e.g., n = 101, there are int(101/(5^1)) numbers have at least one 5 factor
        #         and there are int(101/(5^2)) numbers have at least two 5 factors
        # return self._trailingZeroes(n)  # Time: O(n)
        return self._trailingZeroesMath(n)  # Time: O(log_5 n)

    def _trailingZeroes(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1
        res = 0
        product = 1
        ignore_set = {1, 3, 7, 9}
        while n > 1:
            k = n
            while k % 10 == 0:
                res += 1
                k //= 10
            if (k % 10) in ignore_set:
                n -= 1
                continue
            product *= k
            while product % 10 == 0:
                res += 1
                product //= 10
            n -= 1

        return res

    def _trailingZeroesMath(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        if n < 5:
            return 0

        res = 0
        while n > 0:
            n //= 5
            res += n

        return res


def main():
    # Example 1: Output: 0
    # n = 3

    # Example 2: Output: 1
    n = 5

    # Example 3: Output: 0
    # n = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.trailingZeroes(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
