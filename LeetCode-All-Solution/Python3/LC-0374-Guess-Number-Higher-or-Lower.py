#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0374-Guess-Number-Higher-or-Lower.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-16
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0374 - (Easy) - Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/

Description & Requirement:
    We are playing the Guess Game. The game is as follows:

    I pick a number from 1 to n. You have to guess which number I picked.

    Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

    You call a pre-defined API int guess(int num), which returns three possible results:
        -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).

    Return the number that I picked.

Example 1:
    Input: n = 10, pick = 6
    Output: 6
Example 2:
    Input: n = 1, pick = 1
    Output: 1
Example 3:
    Input: n = 2, pick = 1
    Output: 1

Constraints:
    1 <= n <= 2^31 - 1
    1 <= pick <= n
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (binary search)
        return self._guessNumber(n)

    def _guessNumber(self, n: int) -> int:
        """
        Runtime: 66 ms, faster than 10.28% of Python3 online submissions for Guess Number Higher or Lower.
        Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower.
        """
        assert isinstance(n, int) and n >= 1

        left, right = 1, n
        while left < right:
            mid = (left + right) >> 1
            if guess(mid) <= 0:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 6
    n = 10
    pick = 6

    # Example 2: Output: 1
    # n = 1
    # pick = 1

    # Example 3: Output: 1
    # n = 2
    # pick = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.guessNumber(n, pick)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
