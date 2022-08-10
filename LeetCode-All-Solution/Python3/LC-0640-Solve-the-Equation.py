#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0640-Solve-the-Equation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-10
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0640 - (Medium) - Solve the Equation
https://leetcode.com/problems/solve-the-equation/

Description & Requirement:
    Solve a given equation and return the value of 'x' in the form of a string "x=#value". 
    The equation contains only '+', '-' operation, the variable 'x' and its coefficient. 
    You should return "No solution" if there is no solution for the equation, 
    or "Infinite solutions" if there are infinite solutions for the equation.

    If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

Example 1:
    Input: equation = "x+5-3+x=6+x-2"
    Output: "x=2"
Example 2:
    Input: equation = "x=x"
    Output: "Infinite solutions"
Example 3:
    Input: equation = "2x=x"
    Output: "x=0"

Constraints:
    3 <= equation.length <= 1000
    equation has exactly one '='.
    equation consists of integers with an absolute value in the range [0, 100] 
        without any leading zeros, and the variable 'x'.
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        # exception case
        assert isinstance(equation, str) and len(equation) >= 3
        # main method: (combine all numbers and all variables, and then apply division)
        return self._solveEquation(equation)

    def _solveEquation(self, equation: str) -> str:
        assert isinstance(equation, str) and len(equation) >= 3

        factor = val = 0
        idx, len_equ, sign = 0, len(equation), 1

        while idx < len_equ:
            if equation[idx] == '=':
                sign = -1  # sing == -1 if considering the right part
                idx += 1
                continue

            s = sign
            if equation[idx] == '+':  # ignore the "+" sign
                idx += 1
            elif equation[idx] == '-':
                s = -s
                idx += 1

            # extract the current number
            num, valid = 0, False
            while idx < len_equ and equation[idx].isdigit():
                valid = True
                num = num * 10 + int(equation[idx])
                idx += 1

            if idx < len_equ and equation[idx] == 'x':  # variable x
                factor += s * num if valid else s
                idx += 1
            else:  # pure number
                val += s * num

        if factor == 0:
            return "No solution" if val else "Infinite solutions"

        return "No solution" if val % factor else f"x={-val // factor}"


def main():
    # Example 1: Output: "x=2"
    equation = "x+5-3+x=6+x-2"

    # Example 2: Output: "Infinite solutions"
    # equation = "x=x"

    # Example 3: Output: "x=0"
    # equation = "2x=x"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.solveEquation(equation)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
