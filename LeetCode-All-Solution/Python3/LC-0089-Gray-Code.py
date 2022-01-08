#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0089-Gray-Code.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-08
=================================================================="""
# import collections
import sys
import time
from typing import List
# import queue

"""
LeetCode - 0089 - (Medium) - Gray Code
https://leetcode.com/problems/gray-code/

Description:
    An n-bit gray code sequence is a sequence of 2n integers where:
        Every integer is in the inclusive range [0, 2n - 1],
        The first integer is 0,
        An integer appears no more than once in the sequence,
        The binary representation of every pair of adjacent integers differs by exactly one bit, and
        The binary representation of the first and last integers differs by exactly one bit.

Requirement:
    Given an integer n, return any valid n-bit gray code sequence.

Example 1:
    Input: n = 2
    Output: [0,1,3,2]
    Explanation:
        The binary representation of [0,1,3,2] is [00,01,11,10].
            - 00 and 01 differ by one bit
            - 01 and 11 differ by one bit
            - 11 and 10 differ by one bit
            - 10 and 00 differ by one bit
        [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
            - 00 and 10 differ by one bit
            - 10 and 11 differ by one bit
            - 11 and 01 differ by one bit
            - 01 and 00 differ by one bit
Example 2:
    Input: n = 1
    Output: [0,1]

Constraints:
    1 <= n <= 16
"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if not isinstance(n, int) or n <= 0:
            return []
        return self._grayCode(n)

    def _grayCode(self, n: int) -> List[int]:
        def __grayCodeSymmetricalGeneration() -> List[int]:
            """
            init: [b0], where b0 means binary 0, e.g., decimal integer 10 = b1010
            step 0: [b0, b1], where b1 is b0's (step+1)-th bit (count from the lowest bit) convert from 0 to 1
            step 1: [b00, b01, b11, b10], where b11 is b01's (step+1)-th bit 0->1, and b10 is b00's (step+1)-th bit 0->1
            step 2: [b000, b001, b011, b010, b110, b111, b101, b100], where b110 is b010's (step+1)-th bit 0->1,
                and b111 is b011's (step+1)-th bit 0->1, so does b101 and b100
            so on and so forth
            """
            gray_code = [0]  # init
            for step in range(n):  # perform n steps, step = 0, 1, 2, ...
                # each step, expand current gray_code twice large
                for rev_index in range(len(gray_code) - 1, -1, -1):  # backwards
                    gray_code.append(gray_code[rev_index] | (1 << step))  # (step+1)-th bit 0->1
                # print(gray_code)
                # Example: n = 4
                # step 0: [0, 1]
                # step 1: [0, 1, 3, 2]
                # step 2: [0, 1, 3, 2, 6, 7, 5, 4]
                # step 3: [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
            return gray_code

        def __grayCodeXor() -> List[int]:
            """
            init: [b0, b0, b0, ..., b0], all 2^n 0 in total. where b0 means binary 0, e.g., decimal integer 10 = b1010
            step b000: [b0], where b0 is (step)b000 ^ (b000 >> 1)
            step b001: [b00, b01], where b01 is (step)b001 ^ (b001 >> 1) = b001 ^ b000 = b001
            step b010: [b000, b001, b011], where b011 is (step)b010 ^ (b010 >> 1) = b010 ^ b001 = b011
            step b011: [b000, b001, b011, b010], where b011 is (step)b011 ^ (b011 >> 1) = b011 ^ b001 = b010
            so on and so forth
            """
            gray_code = [0 for _ in range(1 << n)]  # pre define the whole gray_code list
            for step in range(1 << n):  # generate 1 code in 1 loop, step = 0, 1, 2, ...
                gray_code[step] = step ^ (step >> 1)
                # print(gray_code)
                # Example: n = 3
                # step 0: [0, 0, 0, 0, 0, 0, 0, 0]
                # step 1: [0, 1, 0, 0, 0, 0, 0, 0]
                # step 2: [0, 1, 3, 0, 0, 0, 0, 0]
                # step 3: [0, 1, 3, 2, 0, 0, 0, 0]
                # step 4: [0, 1, 3, 2, 6, 0, 0, 0]
                # step 5: [0, 1, 3, 2, 6, 7, 0, 0]
                # step 6: [0, 1, 3, 2, 6, 7, 5, 0]
                # step 7: [0, 1, 3, 2, 6, 7, 5, 4]
            return gray_code

        # return __grayCodeSymmetricalGeneration()
        return __grayCodeXor()


def main():
    # Example 1: Output: [0, 1, 3, 2] or [0, 2, 3, 1]
    # n = 2

    # Example 2: Output: [0, 1]
    # n = 1

    # Example 3: Output: [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
    n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.grayCode(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
