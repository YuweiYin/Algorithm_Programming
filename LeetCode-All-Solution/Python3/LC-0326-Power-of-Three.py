#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0326-Power-of-Three.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-24
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0326 - (Easy) - Power of Three
https://leetcode.com/problems/power-of-three/

Description & Requirement:
    Given an integer n, return true if it is a power of three. Otherwise, return false.

    An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:
    Input: n = 27
    Output: true
Example 2:
    Input: n = 0
    Output: false
Example 3:
    Input: n = 9
    Output: true

Constraints:
    -2^31 <= n <= 2^31 - 1

Follow up:
    Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # exception case
        assert isinstance(n, int)
        # main method: (math trick: since -2^31 <= n <= 2^31 - 1, the biggest 3^x is 3^19 = 1162261467)
        #     so just check if n is a factor of 3^19
        return self._isPowerOfThree(n)

    def _isPowerOfThree(self, n: int) -> bool:
        """
        Runtime: 76 ms, faster than 96.63% of Python3 online submissions for Power of Three.
        Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions for Power of Three.
        """
        assert isinstance(n, int)

        return n > 0 and 1162261467 % n == 0


def main():
    # Example 1: Output: true
    n = 27

    # Example 2: Output: false
    # n = 0

    # Example 3: Output: true
    # n = 9

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPowerOfThree(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
