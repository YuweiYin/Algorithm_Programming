#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0204-Count-Primes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-05
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0204 - (Medium) - Count Primes
https://leetcode.com/problems/count-primes/

Description & Requirement:
    Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:
    Input: n = 0
    Output: 0
Example 3:
    Input: n = 1
    Output: 0

Constraints:
    0 <= n <= 5 * 10^6
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 0
        if n <= 1:
            return 0
        # main method: (prime sieve of Eratosthenes)
        return self._countPrimes(n)

    def _countPrimes(self, n: int) -> int:
        def __get_prime_sieve_of_Eratosthenes(max_size: int) -> int:
            prime_number = [0 for _ in range(max_size)]  # prime number sequence: 2, 3, 5, 7, ... (1-indexed)
            prime_counter = 0
            used_prime = [False for _ in range(max_size)]  # record the used prime numbers, for sieve
            used_prime[0] = used_prime[1] = True  # 0 and 1 are not prime number

            cur_prime = 2
            while cur_prime < max_size:
                if not used_prime[cur_prime]:  # add cur_prime into prime_number sequence
                    prime_counter += 1
                    prime_number[prime_counter] = cur_prime
                # sieve all composite numbers based on cur_prime (also, limited by max_size)
                sieve_index = 1
                while sieve_index <= prime_counter and cur_prime * prime_number[sieve_index] < max_size:
                    used_prime[cur_prime * prime_number[sieve_index]] = True  # do sieve
                    if prime_number[sieve_index] == 0:  # already 0, stop sieve
                        break
                    sieve_index += 1
                cur_prime += 1

            # return prime_number
            return prime_counter

        def __get_prime_counter(max_size: int) -> int:
            prime_flag = [True for _ in range(max_size)]
            counter = 0
            for cur_prime in range(2, max_size):
                if prime_flag[cur_prime]:
                    counter += 1
                    if cur_prime * cur_prime < max_size:
                        sieve_num = cur_prime * cur_prime
                        while sieve_num < max_size:
                            prime_flag[sieve_num] = False
                            sieve_num += cur_prime
            return counter

        # get prime number
        # prime_number_seq = __get_prime_sieve_of_Eratosthenes(max_size=n)
        # prime_number_set = set(prime_number_seq)
        # if 0 in prime_number_set:
        #     prime_number_set.discard(0)

        # return len(prime_number_set)
        # return __get_prime_sieve_of_Eratosthenes(max_size=n)
        return __get_prime_counter(max_size=n)


def main():
    # Example 1: Output: 4
    n = 10

    # Example 2: Output: 0
    # n = 0

    # Example 3: Output: 0
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countPrimes(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
