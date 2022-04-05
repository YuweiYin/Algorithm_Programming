#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0762-Prime-Number-of-Set-Bits-in-Binary-Representation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-05
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0762 - (Easy) - Prime Number of Set Bits in Binary Representation
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

Description & Requirement:
    Given two integers left and right, return the count of numbers in the inclusive range [left, right] 
    having a prime number of set bits in their binary representation.

    Recall that the number of set bits an integer has is the number of 1's present when written in binary.

    For example, 21 written in binary is 10101, which has 3 set bits.

Example 1:
    Input: left = 6, right = 10
    Output: 4
    Explanation:
        6  -> 110 (2 set bits, 2 is prime)
        7  -> 111 (3 set bits, 3 is prime)
        8  -> 1000 (1 set bit, 1 is not prime)
        9  -> 1001 (2 set bits, 2 is prime)
        10 -> 1010 (2 set bits, 2 is prime)
        4 numbers have a prime number of set bits.
Example 2:
    Input: left = 10, right = 15
    Output: 5
    Explanation:
        10 -> 1010 (2 set bits, 2 is prime)
        11 -> 1011 (3 set bits, 3 is prime)
        12 -> 1100 (2 set bits, 2 is prime)
        13 -> 1101 (3 set bits, 3 is prime)
        14 -> 1110 (3 set bits, 3 is prime)
        15 -> 1111 (4 set bits, 4 is not prime)
        5 numbers have a prime number of set bits.

Constraints:
    1 <= left <= right <= 10^6
    0 <= right - left <= 10^4
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # exception case
        assert isinstance(left, int) and left >= 1
        assert isinstance(right, int) and left <= right
        # main method: (check every number in the range)
        return self._countPrimeSetBits(left, right)

    def _countPrimeSetBits(self, left: int, right: int) -> int:
        def __get_prime_sieve_of_Eratosthenes(max_size: int) -> list:
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

            return prime_number

        # get prime number
        MAX_SIZE = len(bin(int(1e6+1)))  # 1 <= left <= right <= 10^6
        prime_number_seq = __get_prime_sieve_of_Eratosthenes(max_size=MAX_SIZE)
        prime_number_set = set(prime_number_seq)
        if 0 in prime_number_set:
            prime_number_set.discard(0)
        del prime_number_seq

        def __check(num: int) -> bool:
            num_bi = bin(num)
            counter_1 = 0
            for ch in num_bi:
                if ch == "1":
                    counter_1 += 1
            return True if counter_1 in prime_number_set else False

        res = 0
        for number in range(left, right + 1):
            if __check(number):
                res += 1
        return res


def main():
    # Example 1: Output: 4
    left = 6
    right = 10

    # Example 2: Output: 5
    # left = 10
    # right = 15

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countPrimeSetBits(left, right)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
