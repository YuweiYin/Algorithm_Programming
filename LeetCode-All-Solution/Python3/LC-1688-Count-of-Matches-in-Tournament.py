#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1688-Count-of-Matches-in-Tournament.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-25
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1688 - (Easy) - Count of Matches in Tournament
https://leetcode.com/problems/count-of-matches-in-tournament/

Description & Requirement:
    You are given an integer n, the number of teams in a tournament that has strange rules:

    If the current number of teams is even, each team gets paired with another team. 
        A total of n / 2 matches are played, and n / 2 teams advance to the next round.
    If the current number of teams is odd, one team randomly advances in the tournament, 
        and the rest gets paired. A total of (n - 1) / 2 matches are played, 
        and (n - 1) / 2 + 1 teams advance to the next round.
    Return the number of matches played in the tournament until a winner is decided.

Example 1:
    Input: n = 7
    Output: 6
    Explanation: Details of the tournament: 
        - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
        - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
        - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
        Total number of matches = 3 + 2 + 1 = 6.
Example 2:
    Input: n = 14
    Output: 13
    Explanation: Details of the tournament:
        - 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
        - 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
        - 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
        - 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
        Total number of matches = 7 + 3 + 2 + 1 = 13.

Constraints:
    1 <= n <= 200
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if n == 1:
            return 0
        # main method: (easy >> 1)
        # trick / pattern: just return n - 1
        return self._numberOfMatches(n)

    def _numberOfMatches(self, n: int) -> int:
        assert n > 1

        res = 0
        while n > 1:  # winner has not declared
            if n & 0x01 == 1:  # n is odd
                n >>= 1
                res += n
                n += 1  # one team randomly advances in the tournament
            else:  # n is even
                n >>= 1
                res += n

        return res


def main():
    # Example 1: Output: 6
    # n = 7

    # Example 2: Output: 13
    # n = 14

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    # ans = solution.numberOfMatches(n)
    ans = []
    for i in range(1, 201):
        ans.append(solution.numberOfMatches(i))
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)  # [0, 1, 2, ..., 199], so: ans = n - 1

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
