#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0564-Find-the-Closest-Palindrome.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-02
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0564 - (Hard) - Find the Closest Palindrome
https://leetcode.com/problems/find-the-closest-palindrome/

Description & Requirement:
    Given a string n representing an integer, 
    return the closest integer (not including itself), which is a palindrome. 
    If there is a tie, return the smaller one.

    The closest is defined as the absolute difference minimized between two integers.

Example 1:
    Input: n = "123"
    Output: "121"
Example 2:
    Input: n = "1"
    Output: "0"
    Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

Constraints:
    1 <= n.length <= 18
    n consists of only digits.
    n does not have leading zeros.
    n is representing an integer in the range [1, 10^18 - 1].
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # exception case
        assert isinstance(n, str) and len(n) > 0 and n.isdigit() and n[0] != "0"
        if n == "0":
            return "1"
        if len(n) == 1:  # 0, 1, 2, ..., 9 are all palindromes
            return str(int(n) - 1)
        # main method: (simulation, modify the origin string to construct possible palindromes)
        #     after considering all possible and close palindromes, choose the closest one (if a tie -> smaller one)
        return self._nearestPalindromic(n)

    def _nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        assert len_n > 0
        number_n = int(n)
        assert number_n > 0

        # 999...999 and 100...001 will always be possible
        # element: (palindrome number, absolute distance from number_n)
        possible_palindrome = [
            [(10 ** (len_n - 1)) - 1, -1],
            [(10 ** (len_n - 1)) + 1, -1],
            [(10 ** len_n) - 1, -1],
            [(10 ** len_n) + 1, -1]
        ]

        # modify the origin string to construct possible palindromes
        left_str = n[: ((len_n + 1) >> 1)]
        left_number = int(left_str)

        # use 3 closest versions of left_num to construct the right_num
        for left_num in [left_number - 1, left_number, left_number + 1]:
            if len_n & 0x01 == 0:  # n has even numbers
                right_num = left_num
            else:  # n has odd numbers
                right_num = left_num // 10  # right_num remove the lowest decimal digit
            # construct palindrome (corporate right_num to left_num)
            while right_num > 0:
                # left_num reserve the lowest decimal digit for the lowest decimal digit of right_num (right_num % 10)
                left_num = (left_num * 10) + (right_num % 10)
                right_num //= 10
            # add the new possible palindrome to list
            possible_palindrome.append([left_num, -1])

        # choose the closest one (if a tie -> smaller one)
        # calculate the absolute distances
        for palin in possible_palindrome:
            palin[1] = abs(palin[0] - number_n)
        # sort (first by absolute distance, then by number)
        possible_palindrome.sort(key=lambda x: (x[1], x[0]))

        for palin in possible_palindrome:
            if palin[0] != number_n:
                return str(palin[0])

        return "0"


def main():
    # Example 1: Output: "121"
    # n = "123"

    # Example 2: Output: "0"
    # n = "1"

    # Example 3: Output: "77"
    n = "88"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nearestPalindromic(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
