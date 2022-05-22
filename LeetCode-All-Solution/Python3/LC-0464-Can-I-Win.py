#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0464-Can-I-Win.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-22
=================================================================="""

import sys
import time
import functools
# from typing import List

"""
LeetCode - 0464 - (Medium) - Can I Win
https://leetcode.com/problems/can-i-win/

Description & Requirement:
    In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. 
    The player who first causes the running total to reach or exceed 100 wins.

    What if we change the game so that players cannot re-use integers?

    For example, two players might take turns drawing from a common pool of numbers from 1 to 15 
    without replacement until they reach a total >= 100.

    Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, 
    otherwise, return false. Assume both players play optimally.

Example 1:
    Input: maxChoosableInteger = 10, desiredTotal = 11
    Output: false
    Explanation:
        No matter which integer the first player choose, the first player will lose.
        The first player can choose an integer from 1 up to 10.
        If the first player choose 1, the second player can only choose integers from 2 up to 10.
        The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
        Same with other integers chosen by the first player, the second player will always win.
Example 2:
    Input: maxChoosableInteger = 10, desiredTotal = 0
    Output: true
Example 3:
    Input: maxChoosableInteger = 10, desiredTotal = 1
    Output: true

Constraints:
    1 <= maxChoosableInteger <= 20
    0 <= desiredTotal <= 300
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # exception case
        assert isinstance(maxChoosableInteger, int) and maxChoosableInteger >= 1
        assert isinstance(desiredTotal, int) and desiredTotal >= 0
        # main method: (memorized DFS search - method of exhaustion)
        return self._canIWin(maxChoosableInteger, desiredTotal)

    def _canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        @functools.lru_cache(maxsize=None)
        def __dfs(num_used: int, cur_total: int) -> bool:
            # num_used has at most `maxChoosableInteger` bits
            for idx in range(maxChoosableInteger):
                if (num_used >> idx) & 0x01 == 0:
                    if (cur_total + idx + 1 >= desiredTotal) or not __dfs(num_used | (1 << idx), cur_total + idx + 1):
                        return True
            return False

        return (((maxChoosableInteger + 1) * maxChoosableInteger) >> 1) >= desiredTotal and __dfs(0, 0)


def main():
    # Example 1: Output: false
    maxChoosableInteger = 10
    desiredTotal = 11

    # Example 2: Output: true
    # maxChoosableInteger = 10
    # desiredTotal = 0

    # Example 3: Output: true
    # maxChoosableInteger = 10
    # desiredTotal = 1

    # Example 4: Output: true
    maxChoosableInteger = 19
    desiredTotal = 190

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canIWin(maxChoosableInteger, desiredTotal)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
