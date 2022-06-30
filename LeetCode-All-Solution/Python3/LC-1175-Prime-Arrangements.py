#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1175-Prime-Arrangements.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-30
=================================================================="""

import sys
import time
import math
# from typing import List
# import functools

"""
LeetCode - 1175 - (Easy) - Prime Arrangements
https://leetcode.com/problems/prime-arrangements/

Description & Requirement:
    Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

    (Recall that an integer is prime if and only if it is greater than 1, 
    and cannot be written as a product of two positive integers both smaller than it.)

    Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
    Input: n = 5
    Output: 12
    Explanation:
        For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:
    Input: n = 100
    Output: 682289015

Constraints:
    1 <= n <= 100
"""


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (combinatorics)
        return self._numPrimeArrangements(n)

    def _numPrimeArrangements(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1
        MOD = int(1e9+7)

        def __is_prime(num: int) -> int:
            if num == 1:
                return 0
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return 0
            return 1

        def __factorial(num: int) -> int:
            res = 1
            for i in range(1, num + 1):
                res *= i
                res %= MOD
            return res

        primes = sum(__is_prime(i) for i in range(1, n + 1))
        return __factorial(primes) * __factorial(n - primes) % MOD


def main():
    # Example 1: Output: 12
    # n = 5

    # Example 2: Output: 682289015
    n = 100

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numPrimeArrangements(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
