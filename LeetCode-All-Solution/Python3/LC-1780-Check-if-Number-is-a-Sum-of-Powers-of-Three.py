#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1780-Check-if-Number-is-a-Sum-of-Powers-of-Three.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-09
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1780 - (Medium) - Check if Number is a Sum of Powers of Three
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

Description & Requirement:
    Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. 
    Otherwise, return false.

    An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:
    Input: n = 12
    Output: true
    Explanation: 12 = 31 + 32
Example 2:
    Input: n = 91
    Output: true
    Explanation: 91 = 30 + 32 + 34
Example 3:
    Input: n = 21
    Output: false

Constraints:
    1 <= n <= 10^7
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (bit manipulation)
        return self._checkPowersOfThree(n)

    def _checkPowersOfThree(self, n: int) -> bool:
        assert isinstance(n, int) and n >= 1

        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3

        return True


def main():
    # Example 1: Output: true
    # n = 12

    # Example 2: Output: true
    # n = 91

    # Example 3: Output: false
    n = 21

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkPowersOfThree(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
