#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0050-Pow(x,n).py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-24
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 0050 - (Medium) - Pow(x, n)
https://leetcode.com/problems/powx-n/

Description & Requirement:
    Implement pow(x, n), http://www.cplusplus.com/reference/valarray/pow/
    which calculates x raised to the power n (i.e., xn).

Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000
Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100
Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
    -100.0 < x < 100.0
    -2^31 <= n <= 2^31-1
    n is an integer.
    Either x is not zero or n > 0.
    -10^4 <= xn <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # exception case
        assert isinstance(x, float) and isinstance(n, int) and (x != 0 or n > 0)
        # main method: (quick multiply)
        return self._myPow(x, n)

    def _myPow(self, x: float, n: int) -> float:
        assert isinstance(x, float) and isinstance(n, int) and (x != 0 or n > 0)

        def __quick_mul(cur_n: int) -> float:
            if cur_n == 0:
                return 1.0
            y = __quick_mul(cur_n >> 1)
            return float(y * y) if cur_n % 2 == 0 else float(y * y * x)

        return __quick_mul(n) if n >= 0 else 1.0 / __quick_mul(-n)


def main():
    # Example 1: Output: 1024.00000
    # x = 2.00000
    # n = 10

    # Example 2: Output: 9.26100
    # x = 2.10000
    # n = 3

    # Example 3: Output: 0.25000
    x = 2.00000
    n = -2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.myPow(x, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
