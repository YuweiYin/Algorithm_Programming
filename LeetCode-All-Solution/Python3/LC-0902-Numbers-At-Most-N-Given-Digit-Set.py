#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0902-Numbers-At-Most-N-Given-Digit-Set.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0902 - (Hard) - Numbers At Most N Given Digit Set
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

Description & Requirement:
    Given an array of digits which is sorted in non-decreasing order. 
    You can write numbers using each digits[i] as many times as we want. 
    For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

    Return the number of positive integers that can be generated that are less than or equal to a given integer n.

Example 1:
    Input: digits = ["1","3","5","7"], n = 100
    Output: 20
    Explanation: 
        The 20 numbers that can be written are:
        1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:
    Input: digits = ["1","4","9"], n = 1000000000
    Output: 29523
    Explanation: 
        We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
        81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
        2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
        In total, this is 29523 integers that can be written using the digits array.
Example 3:
    Input: digits = ["7"], n = 8
    Output: 1

Constraints:
    1 <= digits.length <= 9
    digits[i].length == 1
    digits[i] is a digit from '1' to '9'.
    All the values in digits are unique.
    digits is sorted in non-decreasing order.
    1 <= n <= 10^9
"""


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # exception case
        assert isinstance(digits, list) and len(digits) >= 1
        assert isinstance(n, int) and n >= 1
        # main method: (dynamic programming)
        return self._atMostNGivenDigitSet(digits, n)

    def _atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        assert isinstance(digits, list) and len(digits) >= 1
        assert isinstance(n, int) and n >= 1

        len_d = len(digits)
        n_str = str(n)
        len_n = len(n_str)

        dp = [[0, 0] for _ in range(len_n + 1)]
        dp[0][1] = 1

        for i in range(1, len_n + 1):
            for d in digits:
                if d == n_str[i - 1]:
                    dp[i][1] = dp[i - 1][1]
                elif d < n_str[i - 1]:
                    dp[i][0] += dp[i - 1][1]
                else:
                    break
            if i > 1:
                dp[i][0] += len_d + dp[i - 1][0] * len_d

        return dp[-1][0] + dp[-1][1]


def main():
    # Example 1: Output: 20
    # digits = ["1", "3", "5", "7"]
    # n = 100

    # Example 2: Output: 29523
    digits = ["1", "4", "9"]
    n = 1000000000

    # Example 3: Output: 1
    # digits = ["7"]
    # n = 8

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.atMostNGivenDigitSet(digits, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
