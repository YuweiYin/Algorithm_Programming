#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0808-Soup-Servings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-22
=================================================================="""

import sys
import time
import math
# from typing import List
# import collections
# import functools

"""
LeetCode - 0808 - (Hard) - Soup Servings
https://leetcode.com/problems/soup-servings/

Description & Requirement:
    A positive integer is magical if it is divisible by either a or b.

    Given the three integers n, a, and b, return the nth magical number. 
    Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
    Input: n = 1, a = 2, b = 3
    Output: 2
Example 2:
    Input: n = 4, a = 2, b = 3
    Output: 6

Constraints:
    1 <= n <= 10^9
    2 <= a, b <= 4 * 10^4
"""


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(a, int) and a >= 2
        assert isinstance(b, int) and b >= 2
        # main method: (binary search)
        return self._nthMagicalNumber(n, a, b)

    def _nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """
        Runtime: 49 ms, faster than 80.60% of Python3 online submissions for Nth Magical Number.
        Memory Usage: 13.9 MB, less than 89.55% of Python3 online submissions for Nth Magical Number.
        """
        assert isinstance(n, int) and n >= 1
        assert isinstance(a, int) and a >= 2
        assert isinstance(b, int) and b >= 2

        MOD = int(1e9+7)

        left = min(a, b)
        right = n * min(a, b)
        lcm = a * b / math.gcd(a, b)
        while left <= right:
            mid = (left + right) >> 1
            cnt = mid // a + mid // b - mid // lcm
            if cnt >= n:
                right = mid - 1
            else:
                left = mid + 1

        return (right + 1) % MOD


def main():
    # Example 1: Output: 2
    # n = 1
    # a = 2
    # b = 3

    # Example 2: Output: 6
    n = 4
    a = 2
    b = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nthMagicalNumber(n, a, b)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
