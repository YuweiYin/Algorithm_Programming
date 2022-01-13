#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0191-Number-of-1-Bits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-13
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 0191 - (Easy) - Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Description & Requirement:
    Write a function that takes an unsigned integer and returns the number of '1' bits it has 
    (also known as the [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight)).

    Note:
        Note that in some languages, such as Java, there is no unsigned integer type. 
        In this case, the input will be given as a signed integer type. 
        It should not affect your implementation, as the integer's internal binary representation is the same, 
        whether it is signed or unsigned.

        In Java, the compiler represents the signed integers using 
        [2's complement notation](https://en.wikipedia.org/wiki/Two%27s_complement). 
        Therefore, in Example 3, the input represents the signed integer. -3.

Example 1:
    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:
    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:
    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
    The input must be a binary string of length 32.

Follow up:
    If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        # main method: (Bit Manipulation)
        # return self._hammingWeight(n)
        return self._hammingWeightFast(n)

    def _hammingWeight(self, n: int) -> int:
        """
        consider each bit
        """
        MAX_BIT = 32
        counter = 0
        for _ in range(MAX_BIT):
            if n & 0x01 == 1:
                counter += 1
            n >>= 1

        return counter

    def _hammingWeightFast(self, n: int) -> int:
        """
        Faster: (n & (n-1)) will change the highest bit '1' of n into bit '0'
        """
        counter = 0
        while n:
            n &= (n - 1)
            counter += 1

        return counter


def main():
    # Example 1: Output: 3
    # n = 0b00000000000000000000000000001011

    # Example 2: Output: 1
    # n = 0b00000000000000000000000010000000

    # Example 3: Output: 31
    n = 0b11111111111111111111111111111101

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.hammingWeight(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
