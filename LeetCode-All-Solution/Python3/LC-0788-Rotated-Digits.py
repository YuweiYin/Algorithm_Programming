#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0788-Rotated-Digits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-25
=================================================================="""

import sys
import time
# from typing import List
# import collections
import functools

"""
LeetCode - 0788 - (Medium) - Rotated Digits
https://leetcode.com/problems/rotated-digits/

Description & Requirement:
    An integer x is a good if after rotating each digit individually by 180 degrees, 
    we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

    A number is valid if each digit remains a digit after rotation. For example:
        0, 1, and 8 rotate to themselves,
        2 and 5 rotate to each other 
            (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
        6 and 9 rotate to each other, and
        the rest of the numbers do not rotate to any other number and become invalid.

    Given an integer n, return the number of good integers in the range [1, n].

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
        Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Example 2:
    Input: n = 1
    Output: 0
Example 3:
    Input: n = 2
    Output: 1

Constraints:
    1 <= n <= 10^4
"""


class Solution:
    def rotatedDigits(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (dynamic programming on digits)
        return self._rotatedDigits(n)

    def _rotatedDigits(self, n: int) -> int:
        """
        Runtime: 35 ms, faster than 99.05% of Python3 online submissions for Rotated Digits.
        Memory Usage: 14 MB, less than 28.79% of Python3 online submissions for Rotated Digits.
        """
        assert isinstance(n, int) and n >= 1

        # rotate[i] == 0 -> 0, 1, 8
        # rotate[i] == 1 -> 2, 5, 6, 9
        # rotate[i] == -1 -> 3, 4, 7
        rotate = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        digits = [int(digit) for digit in str(n)]

        @functools.lru_cache(maxsize=None)
        def __dfs(idx: int, bound: bool, diff: bool) -> int:
            """
            :param idx: the current position
            :param bound: if digits[:idx] == str(n)[:idx]
            :param diff: if 2 or 5 or 6 or 9 appears at least once in digits[:idx]
            :return: the number of good integers
            """
            if idx == len(digits):
                return int(diff)

            ans = 0
            for i in range(0, (digits[idx] if bound else 9) + 1):
                if rotate[i] != -1:
                    ans += __dfs(idx + 1, bound and i == digits[idx], diff or rotate[i] == 1)

            return ans

        res = __dfs(0, True, False)
        __dfs.cache_clear()

        return res


def main():
    # Example 1: Output: 4
    # n = 10

    # Example 2: Output: 0
    # n = 1

    # Example 3: Output: 1
    # n = 2

    # Example 1: Output: 2320
    n = 10000

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rotatedDigits(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
