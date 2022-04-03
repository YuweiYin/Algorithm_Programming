#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0007-Reverse-Integer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-02
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0007 - (Medium) - Reverse Integer
https://leetcode.com/problems/reverse-integer/

Description & Requirement:
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321
Example 2:
    Input: x = -123
    Output: -321
Example 3:
    Input: x = 120
    Output: 21

Constraints:
    -2^31 <= x <= 2^31 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        # exception case
        assert isinstance(x, int)
        # main method: (convert x to str, then reverse, remove heading 0s. consider the sign symbol and int boundary)
        return self._reverse(x)

    def _reverse(self, x: int) -> int:
        """
        Runtime: 28 ms, faster than 97.47% of Python3 online submissions for Reverse Integer.
        Memory Usage: 13.9 MB, less than 18.22% of Python3 online submissions for Reverse Integer.
        """
        if x == 0:
            return 0
        sign = False
        if x > 0:
            x_str = str(x)
        else:
            sign = True
            x_str = str(-x)

        x_str = x_str[::-1] # reverse string
        idx = 0
        while idx < len(x_str) and x_str[idx] == "0":  # remove heading 0s
            idx += 1
        if idx == len(x_str):
            return 0
        x_str = x_str[idx:]

        MIN = -(1 << 31)
        MAX = (1 << 31) - 1

        min_str = str(-MIN)
        max_str = str(MAX)

        if sign:  # x is a negative number
            if len(x_str) < len(min_str):
                return - int(x_str)
            elif len(x_str) == len(min_str):
                if x_str > min_str:
                    return 0
                else:
                    return - int(x_str)
            else:
                return 0
        else:  # x is a positive number
            if len(x_str) < len(max_str):
                return int(x_str)
            elif len(x_str) == len(max_str):
                if x_str > max_str:
                    return 0
                else:
                    return int(x_str)
            else:
                return 0


def main():
    # Example 1: Output: 321
    x = 123

    # Example 2: Output: -321
    # x = -123

    # Example 3: Output: 21
    # x = 120

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverse(x)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
