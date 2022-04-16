#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0479-Largest-Palindrome-Product.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-16
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0479 - (Hard) - Largest Palindrome Product
https://leetcode.com/problems/largest-palindrome-product/

Description & Requirement:
    Given an integer n, return the largest palindromic integer that can be represented as 
    the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

Example 1:
    Input: n = 2
    Output: 987
    Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
Example 2:
    Input: n = 1
    Output: 9

Constraints:
    1 <= n <= 8
"""


class Solution:
    def largestPalindrome(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n > 0
        # main method: (trick: result table)
        #     construct and enumerate palindromes by flipping the left side
        return self._largestPalindrome(n)

    def _largestPalindrome(self, n: int) -> int:
        """
        Runtime: 31 ms, faster than 99.13% of Python3 online submissions for Largest Palindrome Product.
        Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Largest Palindrome Product.
        """
        assert isinstance(n, int) and 1 <= n <= 8
        # res = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
        # return res[n]

        if n == 1:
            return 9
        MOD = 1337
        upper_bound = 10 ** n - 1

        for palin_left in range(upper_bound, upper_bound // 10, -1):
            palin, p_left = palin_left, palin_left
            while p_left:  # construct p_right by p_left
                palin = palin * 10 + p_left % 10  # append each digit of p_right to the end of palin
                p_left //= 10
            p_left = upper_bound
            while p_left * p_left >= palin:
                if palin % p_left == 0:  # p_left is a factor of palin
                    return palin % MOD
                p_left -= 1


def main():
    # Example 1: Output: 987
    n = 2

    # Example 2: Output: 9
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestPalindrome(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
