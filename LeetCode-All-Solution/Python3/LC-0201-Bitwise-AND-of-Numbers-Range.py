#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0201-Bitwise-AND-of-Numbers-Range.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-01
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0201 - (Medium) - Bitwise AND of Numbers Range
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Description & Requirement:
    Given two integers left and right that represent the range [left, right], 
    return the bitwise AND of all numbers in this range, inclusive.

Example 1:
    Input: left = 5, right = 7
    Output: 4
Example 2:
    Input: left = 0, right = 0
    Output: 0
Example 3:
    Input: left = 1, right = 2147483647
    Output: 0

Constraints:
    0 <= left <= right <= 2^31 - 1
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # exception case
        if not isinstance(left, int) or left < 0:
            return 0  # Error input type
        if not isinstance(right, int) or right < left:
            return 0  # Error input type
        # main method 1: (Binary Manipulation)
        #     idea: bitwise AND, if one bit is 0, then this bit in AND result is also 0
        #     consider all num in [left, right] range, from a certain bit k, high bits (>= k) are all the same
        #     consider the bits < k, e.g., range [m, n], where n > m.
        #     m must do AND with m+1, if >= k bits of m and m+1 are the same, then m and m+1 must be:
        #     m: 0b???...??0  m+1: 0b???...??1   or   m: 0b???...?0111...111 and m+1: 0b???...?1000...000
        #     in either case, (m & m+1): 0b???...???000...000, only the common prefix bits (0b???...???) reserved
        #     therefore, just find the "0b???...???" of left and right, and then shift << to recover 0s
        # main method 2: Brian Kernighan's algorithm
        #    idea: when perform (n & n-1), the rightmost bit-1 will be removed from n,
        #    so follow the idea of method 1, perform n = n & (n-1) until m == n (only common prefix bits are remained)
        # return self._rangeBitwiseAnd(left, right)
        return self._rangeBitwiseAndBrianKernighan(left, right)

    def _rangeBitwiseAnd(self, left: int, right: int) -> int:
        assert 0 <= left <= right

        tobe_shift_bits = 0
        while left < right:  # loop until found the common prefix bits (0b???...???)
            left >>= 1
            right >>= 1
            tobe_shift_bits += 1  # record how many 0s need to be recovered

        return left << tobe_shift_bits

    def _rangeBitwiseAndBrianKernighan(self, left: int, right: int) -> int:
        """
        Runtime: 56 ms, faster than 82.70% of Python3 online submissions for Bitwise AND of Numbers Range.
        Memory Usage: 13.9 MB, less than 98.66% of Python3 online submissions for Bitwise AND of Numbers Range.
        """
        assert 0 <= left <= right

        while left < right:  # loop until found the common prefix bits (0b???...???)
            right = right & (right - 1)  # remove the rightmost bit-1 of right

        return right


def main():
    # Example 1: Output: 4
    left = 5
    right = 7

    # Example 2: Output: 0
    # left = 0
    # right = 0

    # Example 3: Output: 0
    # left = 1
    # right = 2147483647

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rangeBitwiseAnd(left, right)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
