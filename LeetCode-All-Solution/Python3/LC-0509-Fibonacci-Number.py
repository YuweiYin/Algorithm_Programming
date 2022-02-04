#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0509-Fibonacci-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
import math

"""
LeetCode - 0509 - (Easy) - Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

Description & Requirement:
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
    such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).

Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
    0 <= n <= 30

Related Problem:
    LC-0070-Climbing-Stairs
"""


class Solution:
    def fib(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        # main method: (3 methods)
        return self._fib(n)

    def _fib(self, n: int) -> int:
        assert n >= 4

        def __fibo_simple(first: int, second: int, cur_n: int):
            """
            __fibo_simple can be accelerated by dynamic programming technique or matrix fast power technique
            """
            if cur_n == n:
                return second
            return __fibo_simple(second, first + second, cur_n + 1)

        def __fibo_matrix_fast_power():
            """
            F_{n} = F_{n-1} + F_{n-2}, it means
            [[F_1, F_2],  *  [[0, 1],  =  [[F_2, F_1 + F_2],  this is exactly the [[F_2, F_3]
             [0,    0]]      [1, 1]]       [0,          0]]                        [0,    0]]
            so start from [[F_1, F_2], [0, 0]], multiply [[0, 1], [1, 1]] each step
            plus, matrix multiplication m^n can be accelerated by matrix fast power technique
            """
            multiplier_matrix = [[0, 1], [1, 1]]

            def __matrix_multiply_2dim(mx1, mx2):
                res_mx = [[0, 0], [0, 0]]
                for row in range(2):
                    for col in range(2):
                        res_mx[row][col] = mx1[row][0] * mx2[0][col] + mx1[row][1] * mx2[1][col]
                return res_mx

            def __matrix_fast_power(mx, power_n: int):
                res_mx = [[1, 0], [0, 1]]  # identity matrix

                while power_n > 0:
                    if power_n & 0x01:  # lowest bit == 1 -> do multiplication
                        res_mx = __matrix_multiply_2dim(res_mx, mx)
                    power_n >>= 1  # consider next bit
                    if power_n <= 0:
                        break
                    mx = __matrix_multiply_2dim(mx, mx)  # self multiplication

                return res_mx

            fino_matrix = __matrix_fast_power(multiplier_matrix, n)
            return fino_matrix[0][1]

        def __fibo_binet():
            """
            [Binet's Formula](https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html)
            is an explicit formula used to find the $n$th term of the Fibonacci sequence.
            It is so named because it was derived by mathematician Jacques Philippe Marie Binet,
            though it was already known by Abraham de Moivre.
            Let $F_n$ be n-th Fibonacci number and s_5 means sqrt{5}, then
            $$F_n = 1/s_5 * (((1 + s_5) / 2)^n - ((1 - s_5) / 2)^n)$$
            However, when n is extremely large, there might be some accuracy error
            """
            SQRT5 = math.sqrt(5)
            _fibo = math.pow((1 + SQRT5) / 2, n) - math.pow((1 - SQRT5) / 2, n)
            return int(_fibo / SQRT5)

        # fibo_n = __fibo_simple(0, 1, 1)
        # fibo_n = __fibo_matrix_fast_power()
        fibo_n = __fibo_binet()
        return fibo_n


def main():
    # Example 1: Output: 1
    # n = 2

    # Example 2: Output: 2
    # n = 3

    # Example 3: Output: 3
    # n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    for n in range(31):
        ans = solution.fib(n)
        print(ans)
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
