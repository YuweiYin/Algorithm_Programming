#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0357-Count-Numbers-with-Unique-Digits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-11
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0357 - (Medium) - Count Numbers with Unique Digits
https://leetcode.com/problems/count-numbers-with-unique-digits/

Description & Requirement:
    Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n.

Example 1:
    Input: n = 2
    Output: 91
    Explanation: 
        The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:
    Input: n = 0
    Output: 1

Constraints:
    0 <= n <= 8
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and 0 <= n <= 8
        # main method: (combinatorics: if a number has n digits, then the possible choices for each digit is n!)
        #     such that the number doesn't have duplicated digits
        # trick: construct result table
        return self._countNumbersWithUniqueDigits(n)

    def _countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        Runtime: 27 ms, faster than 94.65% of Python3 online submissions for Count Numbers with Unique Digits.
        Memory Usage: 13.8 MB, less than 61.76% of Python3 online submissions for Count Numbers with Unique Digits.
        """
        assert isinstance(n, int) and 0 <= n <= 8

        # res_list = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851]
        # return res_list[n]

        if n == 0:
            return 1
        if n == 1:
            return 10

        # get n!
        res = 10  # 0 ~ 9
        cur_choice = 9
        for cur_digit in range(n - 1):
            cur_choice *= 9 - cur_digit
            res += cur_choice
        return res


def main():
    # Example 1: Output: 91
    n = 2

    # Example 2: Output: 1
    # n = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countNumbersWithUniqueDigits(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
