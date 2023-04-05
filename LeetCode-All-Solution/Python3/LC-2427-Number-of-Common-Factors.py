#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2427-Number-of-Common-Factors.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-05
=================================================================="""

import sys
import time
import math
# from typing import List
# import collections
# import functools

"""
LeetCode - 2427 - (Easy) - Number of Common Factors
https://leetcode.com/problems/number-of-common-factors/

Description & Requirement:
    Given two positive integers a and b, return the number of common factors of a and b.

    An integer x is a common factor of a and b if x divides both a and b.

Example 1:
    Input: a = 12, b = 6
    Output: 4
    Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:
    Input: a = 25, b = 30
    Output: 2
    Explanation: The common factors of 25 and 30 are 1, 5.

Constraints:
    1 <= a, b <= 1000
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # exception case
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and b >= 1
        # main method: (enumerate til the root square of gcd(a, b))
        return self._commonFactors(a, b)

    def _commonFactors(self, a: int, b: int) -> int:
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and b >= 1

        cf, res = math.gcd(a, b), 0

        number = 1
        while number * number <= cf:
            if cf % number == 0:
                res += 1
                if number * number != cf:
                    res += 1
            number += 1

        return res


def main():
    # Example 1: Output: 4
    a = 12
    b = 6

    # Example 2: Output: 2
    # a = 25
    # b = 30

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.commonFactors(a, b)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
