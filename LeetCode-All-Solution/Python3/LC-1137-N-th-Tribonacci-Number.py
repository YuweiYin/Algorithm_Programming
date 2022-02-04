#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1137-N-th-Tribonacci-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-04
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1137 - (Easy) - N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/

Description & Requirement:
    The Tribonacci sequence Tn is defined as follows: 
        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    Given n, return the value of Tn.

Example 1:
    Input: n = 4
    Output: 4
    Explanation:
        T_3 = 0 + 1 + 1 = 2
        T_4 = 1 + 1 + 2 = 4
Example 2:
    Input: n = 25
    Output: 1389537

Constraints:
    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        # main method: (2 methods)
        return self._tribonacci(n)

    def _tribonacci(self, n: int) -> int:
        assert n >= 4

        def __tribo_simple(first: int, second: int, third: int, cur_n: int):
            """
            __tribo_simple can be accelerated by dynamic programming technique or matrix fast power technique
            """
            if cur_n == n:
                return second
            return __tribo_simple(second, third, first + second + third, cur_n + 1)

        def __tribo_matrix_fast_power():
            """
            T_{n} = T_{n-1} + T_{n-2} + T_{n-3}, it means
            [[T_1, T_2, T_3],  *  [[0, 0, 1],  =  [[T_1, T_2, T_1 + T_2 + T_3], this is exactly the [[T_2, T_3, T_4]
             [0,   0,   0]         [1, 0, 1]       [0,   0,   0]                                     [0,   0,   0]
             [0,   0,   0]]        [0, 1, 1]]      [0,   0,   0]]                                    [0,   0,   0]]
            so start from [[T_0, T_1, T_2], [0, 0, 0], [0, 0, 0]], multiply [[0, 0, 1], [1, 0, 1], [0, 1, 1]] each step
            plus, matrix multiplication m^n can be accelerated by matrix fast power technique
            """
            multiplier_matrix = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]

            def __matrix_multiply_3dim(mx1, mx2):
                res_mx = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                for row in range(3):
                    for col in range(3):
                        res_mx[row][col] = sum([mx1[row][index] * mx2[index][col] for index in range(3)])
                return res_mx

            def __matrix_fast_power(mx, power_n: int):
                res_mx = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # identity matrix

                while power_n > 0:
                    if power_n & 0x01:  # lowest bit == 1 -> do multiplication
                        res_mx = __matrix_multiply_3dim(res_mx, mx)
                    power_n >>= 1  # consider next bit
                    if power_n <= 0:
                        break
                    mx = __matrix_multiply_3dim(mx, mx)  # self multiplication

                return res_mx

            fino_matrix = __matrix_fast_power(multiplier_matrix, n)
            return fino_matrix[0][2]

        tribo_n = __tribo_simple(0, 1, 1, 1)
        # tribo_n = __tribo_matrix_fast_power()
        return tribo_n


def main():
    # Example 1: Output: 4
    # n = 4

    # Example 2: Output: 1389537
    n = 25

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.tribonacci(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
