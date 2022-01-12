#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0070-Climbing-Stairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-12
=================================================================="""
import math
import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0070 - (Easy) - Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

Description & Requirement:
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        # main method: (Dynamic Programming: DP equation: dp[i] = dp[i-1] + dp[i-2] -> Mathematics: Fibonacci sequence)
        #     Explanation: When jumping to i-th staircase, it can either from (i-1)-th staircase (by jump 1 step);
        #     or from (i-2)-th staircase (by jump 2 steps at a time), so the total jumping way to get i-th staircase
        #     dp[i] is the sum of dp[i-1] and dp[i-2]  (i >= 2).
        #     The dp equation dp[i] = dp[i-1] + dp[i-2] forms exactly the Fibonacci sequence: 1, 1, 2, 3, 5, ...
        #     In this problem, the fibo seq is: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
        #     1597, 2584, 4181, 6765, 10946, ... [Fibonacci_number](https://en.wikipedia.org/wiki/Fibonacci_number)
        return self._climbStairsFibonacci(n)

    def _climbStairsFibonacci(self, n: int) -> int:
        assert isinstance(n, int) and n > 2

        def __fibo_simple(first: int, second: int, cur_staircase: int):
            """
            __fibo_simple can be accelerated by dynamic programming technique or matrix fast power technique
            """
            if cur_staircase == n:
                return second
            return __fibo_simple(second, first + second, cur_staircase + 1)

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

            # note that in this problem, the actual target Fibonacci number is F_{n+1} rather than F_n
            fino_matrix = __matrix_fast_power(multiplier_matrix, n + 1)
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
            # note that in this problem, the actual target Fibonacci number is F_{n+1} rather than F_n
            _fibo = math.pow((1 + SQRT5) / 2, n + 1) - math.pow((1 - SQRT5) / 2, n + 1)
            return int(_fibo / SQRT5)

        # fibo_n = __fibo_simple(1, 2, 2)
        # fibo_n = __fibo_matrix_fast_power()
        fibo_n = __fibo_binet()
        return fibo_n


def main():
    # Example 1: Output: 2
    # n = 2

    # Example 2: Output: 3
    # n = 3

    # Example 3: Output: 89
    # n = 10

    # Example 4: Output: 10946
    # n = 20

    # Example 5: Output: 1346269
    # n = 30

    # Example 6: Output: 165580141
    # n = 40

    # Example 7: Output: 1836311903
    n = 45

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.climbStairs(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
