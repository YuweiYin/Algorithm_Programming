#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1447-Simplified-Fractions.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-10
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1447 - (Medium) - Simplified Fractions
https://leetcode.com/problems/simplified-fractions/

Description & Requirement:
    Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) 
    such that the denominator is less-than-or-equal-to n. 
    You can return the answer in any order.

Example 1:
    Input: n = 2
    Output: ["1/2"]
    Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:
    Input: n = 3
    Output: ["1/2","1/3","2/3"]
Example 3:
    Input: n = 4
    Output: ["1/2","1/3","1/4","2/3","3/4"]
    Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".

Constraints:
    1 <= n <= 100
"""


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return []  # Error input type
        if n == 1:
            return []
        # main method: (Math: if the greatest common divisor of denominator and numerator is 1, then valid)
        return self._simplifiedFractions(n)

    def _simplifiedFractions(self, n: int) -> List[str]:
        assert n >= 2
        import math

        # res_set = set()
        res = []

        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if math.gcd(denominator, numerator) == 1:
                    cur_simplified_fraction = "%d/%d" % (numerator, denominator)
                    # if cur_simplified_fraction not in res_set:
                    #     res_set.add(cur_simplified_fraction)
                    res.append(cur_simplified_fraction)

        # return list(res_set)
        return res


def main():
    # Example 1: Output: ["1/2"]
    # n = 2

    # Example 2: Output: ["1/2","1/3","2/3"]
    # n = 3

    # Example 3: Output: ["1/2","1/3","1/4","2/3","3/4"]
    n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.simplifiedFractions(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
