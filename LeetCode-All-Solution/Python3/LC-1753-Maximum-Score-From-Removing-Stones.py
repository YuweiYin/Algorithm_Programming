#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1753-Maximum-Score-From-Removing-Stones.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-21
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1753 - (Medium) - Maximum Score From Removing Stones
https://leetcode.com/problems/maximum-score-from-removing-stones/

Description & Requirement:
    You are playing a solitaire game with three piles of stones of sizes a, b, and c respectively. 
    Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. 
    The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

    Given three integers a, b, and c, return the maximum score you can get.

Example 1:
    Input: a = 2, b = 4, c = 6
    Output: 6
    Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
        - Take from 1st and 3rd piles, state is now (1, 4, 5)
        - Take from 1st and 3rd piles, state is now (0, 4, 4)
        - Take from 2nd and 3rd piles, state is now (0, 3, 3)
        - Take from 2nd and 3rd piles, state is now (0, 2, 2)
        - Take from 2nd and 3rd piles, state is now (0, 1, 1)
        - Take from 2nd and 3rd piles, state is now (0, 0, 0)
        There are fewer than two non-empty piles, so the game ends. Total: 6 points.
Example 2:
    Input: a = 4, b = 4, c = 6
    Output: 7
    Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
        - Take from 1st and 2nd piles, state is now (3, 3, 6)
        - Take from 1st and 3rd piles, state is now (2, 3, 5)
        - Take from 1st and 3rd piles, state is now (1, 3, 4)
        - Take from 1st and 3rd piles, state is now (0, 3, 3)
        - Take from 2nd and 3rd piles, state is now (0, 2, 2)
        - Take from 2nd and 3rd piles, state is now (0, 1, 1)
        - Take from 2nd and 3rd piles, state is now (0, 0, 0)
        There are fewer than two non-empty piles, so the game ends. Total: 7 points.
Example 3:
    Input: a = 1, b = 8, c = 8
    Output: 8
    Explanation: One optimal set of moves is to take from the 2nd and 3rd piles for 8 turns until they are empty.
        After that, there are fewer than two non-empty piles, so the game ends.

Constraints:
    1 <= a, b, c <= 10^5
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # exception case
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and b >= 1
        assert isinstance(c, int) and c >= 1
        # main method: (greedy)
        return self._maximumScore(a, b, c)

    def _maximumScore(self, a: int, b: int, c: int) -> int:
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and b >= 1
        assert isinstance(c, int) and c >= 1

        _sum = a + b + c
        max_val = max(a, b, c)

        return _sum - max_val if _sum < (max_val << 1) else (_sum >> 1)


def main():
    # Example 1: Output: 6
    a, b, c = 2, 4, 6

    # Example 2: Output: 7
    # a, b, c = 4, 4, 6

    # Example 3: Output: 8
    # a, b, c = 1, 8, 8

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumScore(a, b, c)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
