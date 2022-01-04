#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1009-Complement-of-Base-10-Integer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 1009 - (Easy) - Complement of Base 10 Integer
https://leetcode.com/problems/complement-of-base-10-integer/

Description:
    The complement of an integer is the integer you get when you flip all the 0's to 1's 
    and all the 1's to 0's in its binary representation.

    For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

Requirement:
    Given an integer n, return its complement.

Example 1:
    Input: n = 5
    Output: 2
    Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:
    Input: n = 7
    Output: 0
    Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:
    Input: n = 10
    Output: 5
    Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

Constraints:
    0 <= n < 10^9

Note: This question is the same as 476: https://leetcode.com/problems/number-complement/
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # exception case
        if not isinstance(n, int):
            return -1  # Error input
        # special case
        if n == 0:
            return 1
        if not (n & (n + 1)):  # if n & (n + 1) == 0, then (n + 1) is a power of 2, so bin(n) = 111...111
            return 0
        # main method:
        # return self._bitwiseComplementString(n)
        return self._bitwiseComplementNumber(n)  # more time-efficient

    def _bitwiseComplementString(self, n: int) -> int:
        """ String method
        """
        n_bin_str = bin(n).replace("0b", "")  # get the binary string representation (remove the leftmost "0b")
        new_bin_str = ""  # construct new str
        len_bin_str = len(n_bin_str)
        cur_index = 0
        while cur_index < len_bin_str:
            new_bin_str += "0" if n_bin_str[cur_index] == "1" else "1"  # convert every "0" to "1" and "1" to "0"
            cur_index += 1  # deal with the next bit

        return int(new_bin_str, 2)  # convert string to binary number

    def _bitwiseComplementNumber(self, n: int) -> int:
        """ Number method
        """
        complement = 0
        cur_power = 1
        while n > 0:
            if not (n & 0x01):  # if True: the lowest bit of n is 0, so its complement bit is 1
                complement += cur_power
            cur_power <<= 1  # update power: 1 -> 2 -> 4 -> 8 -> ...
            n >>= 1  # check the next bit of n

        return complement


def main():
    # Example 1: Output: 2
    #     Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
    n = 5

    # Example 2: Output: 0
    #     Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
    # n = 7

    # Example 3: Output: 5
    #     Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
    # n = 10

    # Example 4: Output: 1
    # n = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.bitwiseComplement(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
