#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0029-Divide-Two-Integers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-14
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0029 - (Medium) - Divide Two Integers
https://leetcode.com/problems/divide-two-integers/

Description & Requirement:
    Given two integers dividend and divisor, 
    divide two integers without using multiplication, division, and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part. 
    For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment 
        that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. 
        For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, 
        and if the quotient is strictly less than -2^31, then return -2^31.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
    -2^31 <= dividend, divisor <= 2^31 - 1
    divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # exception case
        assert isinstance(dividend, int) and isinstance(divisor, int)
        # main method: (greedily minus divisor * 2^k as large as possible)
        return self._divide(dividend, divisor)

    def _divide(self, dividend: int, divisor: int) -> int:
        """
        Runtime: 28 ms, faster than 97.98% of Python3 online submissions for Divide Two Integers.
        Memory Usage: 13.9 MB, less than 81.15% of Python3 online submissions for Divide Two Integers.
        """
        if divisor == 0:
            return 0
        if dividend == 0:
            return 0

        MAX_INT = (1 << 31) - 1
        MIN_INT = - (1 << 31)

        if dividend == MAX_INT:
            if divisor == 1:
                return MAX_INT
            elif divisor == -1:
                return - MAX_INT
            # else: the quotient won't overflow

        if dividend == MIN_INT:
            if divisor == 1:
                return MIN_INT
            elif divisor == -1:
                return MAX_INT  # rather than (- MIN_INT)
            # else: the quotient won't overflow

        if divisor == MAX_INT:
            if dividend == MAX_INT:
                return 1
            elif dividend == MIN_INT:
                return -1
            else:
                return 0  # truncate all fractional part

        if divisor == MIN_INT:
            if dividend == MIN_INT:
                return 1
            else:
                return 0  # truncate all fractional part

        # now, use addition and subtraction to simulate the division process
        # convert positive numbers into negative numbers
        flag = False
        if dividend > 0:
            dividend = - dividend
            flag = not flag
        if divisor > 0:
            divisor = - divisor
            flag = not flag

        # find the k such that (divisor * 2^k) < dividend
        divisor_list = [divisor]
        while divisor_list[-1] >= dividend - divisor_list[-1]:
            divisor_list.append(divisor_list[-1] + divisor_list[-1])  # put in (divisor * 2^k)

        # dividend minus (divisor * 2^k) for each step
        res = 0  # quotient
        for idx in range(len(divisor_list) - 1, -1, -1):
            if divisor_list[idx] >= dividend:
                res += (1 << idx)
                dividend -= divisor_list[idx]

        return res if not flag else - res


def main():
    # Example 1: Output: 3
    # dividend = 10
    # divisor = 3

    # Example 2: Output: -2
    # dividend = 7
    # divisor = -3

    # Example 3: Output: -1
    dividend = 2147483647
    divisor = -2147483648

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.divide(dividend, divisor)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
