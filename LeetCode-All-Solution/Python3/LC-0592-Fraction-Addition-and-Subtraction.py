#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0592-Fraction-Addition-and-Subtraction.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-27
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0592 - (Medium) - Fraction Addition and Subtraction
https://leetcode.com/problems/fraction-addition-and-subtraction/

Description & Requirement:
    Given a string expression representing an expression of fraction addition and subtraction, 
    return the calculation result in string format.

    The final result should be an irreducible fraction. If your final result is an integer, 
    change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
    Input: expression = "-1/2+1/2"
    Output: "0/1"
Example 2:
    Input: expression = "-1/2+1/2+1/3"
    Output: "1/3"
Example 3:
    Input: expression = "1/3-1/2"
    Output: "-1/6"

Constraints:
    The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    Each fraction (input and output) has the format ±numerator/denominator. 
        If the first input fraction or the output is positive, then '+' will be omitted.
    The input only contains valid irreducible fractions, where the numerator and denominator of each fraction 
        will always be in the range [1, 10]. If the denominator is 1, 
        it means this fraction is actually an integer in a fraction format defined above.
    The number of given fractions will be in the range [1, 10].
    The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""


class Solution:
    def fractionAddition(self, expression: str) -> str:
        # exception case
        assert isinstance(expression, str) and len(expression) > 0
        # main method: (get GCD of denominators, then get LCM of denominators)
        return self._fractionAddition(expression)

    def _fractionAddition(self, expression: str) -> str:
        """
        Runtime: 34 ms, faster than 87.11% of Python3 online submissions for Fraction Addition and Subtraction.
        Memory Usage: 14 MB, less than 41.33% of Python3 online submissions for Fraction Addition and Subtraction.
        """
        assert isinstance(expression, str) and len(expression) > 0

        # prepend "+" to each "-", except the first "-"
        new_exp = expression[0]
        for ch in expression[1:]:
            if ch == "-":
                new_exp += "+" + ch
            else:
                new_exp += ch

        expression = new_exp

        if "+" not in expression:
            return expression

        nums = expression.split("+")

        def __gcd(num_1: int, num_2: int) -> int:
            if num_2 == 0:
                return num_1
            else:
                return __gcd(num_2, num_1 % num_2)

        # def __lcm(num_1: int, num_2: int) -> int:
        #     return int(num_1 * num_2 / __gcd(num_1, num_2))

        def __plus(num_1: str, num_2: str) -> str:
            if "/" not in num_1:
                num_1 += "/1"
            numerator_1, denominator_1 = num_1.split("/")
            numerator_1, denominator_1 = int(numerator_1), int(denominator_1)

            if "/" not in num_2:
                num_2 += "/1"
            numerator_2, denominator_2 = num_2.split("/")
            numerator_2, denominator_2 = int(numerator_2), int(denominator_2)

            if numerator_1 == 0:
                return num_2
            de_gcd = __gcd(denominator_1, denominator_2)
            de_lcm = int(denominator_1 * denominator_2 / de_gcd)  # new common denominator
            nu_1 = int(numerator_1 * denominator_2 / de_gcd)  # new numerator_1
            nu_2 = int(numerator_2 * denominator_1 / de_gcd)  # new numerator_2
            nu = nu_1 + nu_2  # sum of numerator_1 and numerator_2
            return str(nu) + "/" + str(de_lcm)

        res = nums[0]
        for idx in range(1, len(nums)):
            num = nums[idx]
            if len(num) > 0:
                res = __plus(res, num)

        if "/" not in res:
            return res + "/1"
        else:
            n, d = res.split("/")
            n, d = int(n), int(d)
            if n == 0:
                return "0/1"
            else:
                gcd = __gcd(abs(n), abs(d))
                return str(int(n / gcd)) + "/" + str(int(d / gcd))


def main():
    # Example 1: Output: "0/1"
    expression = "-1/2+1/2"

    # Example 2: Output: "1/3"
    # expression = "-1/2+1/2+1/3"

    # Example 3: Output: "-1/6"
    # expression = "1/3-1/2"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.fractionAddition(expression)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
