#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1510-Stone-Game-IV.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-22
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1510 - (Hard) - Stone Game IV
https://leetcode.com/problems/stone-game-iv/

Description & Requirement:
    Alice and Bob take turns playing a game, with Alice starting first.

    Initially, there are n stones in a pile. On each player's turn, 
    that player makes a move consisting of removing any non-zero square number of stones in the pile.

    Also, if a player cannot make a move, he/she loses the game.

    Given a positive integer n, return true if and only if Alice wins the game otherwise return false, 
    assuming both players play optimally.

Example 1:
    Input: n = 1
    Output: true
    Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:
    Input: n = 2
    Output: false
    Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:
    Input: n = 4
    Output: true
    Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

Constraints:
    1 <= n <= 10^5
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return False  # Alice can't even start, GG
        if n == 1:
            return True
        # main method: (Game theory, Dynamic programming)
        #     idea: for X's turn, if X must win (currently, there are S(X_{1}) = p stones),
        #         after X remove q_{1}^2 stones, for the other player Y, S(Y_{1}) = (p - q_{1}^2) is a must-lose state.
        #         keep moving, if Y still can remove stones, then S(X_{2}) = S(Y_{1}) - q_{2}^2 stones,
        #         this is still X's must-win state. so on and so forth, till Y can't remove any stones, Y lose.
        # consider all possible initial state:
        # case_0: if X starts 0 stone, X must lose.
        #            -> if * start 0, * must lose
        # case_1: if X starts 1 stone, 1 = 1^2, remove it, get 0 stone for Y, so Y must lose.
        #            -> if * start 1, * must win
        # case_2: if X starts 2 stones, 2 is not a perfect square, 2 - 1^2 = 1 for Y, consider case_1, Y must win.
        #            -> if * start 2, * must lose
        # case_3: if X starts 3 stones, 3 - 1^2 = 2 for Y, consider case_2, X must win.
        #            -> if * start 3, * must win
        # case_4: if X starts 4 stones, 4 - 2^2 = 0 for Y, X must win.
        #            -> if * start 4, * must win
        # so, set a dp table, dp[i] describes case_i
        return self._winnerSquareGame(n)

    def _winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]  # case_0, 1, 2, ..., n (default False because case_0 is False)

        for case_i in range(1, n + 1):  # X starts with case_i stones, i = 1, 2, 3, ..., n
            q = 1  # to form a perfect square
            while q * q <= case_i:  # remove q^2 stones
                if not dp[int(case_i - q * q)]:  # if after current remove, the other player (Y) is must-lose state
                    dp[case_i] = True  # then the current player (X) is must-win state
                    break
                q += 1  # for X, can't conduce to win by (case_i - q * q), try a larger q
                # if all q can't fulfill, then dp[case_i] is default False

        return dp[n]  # case_n is the final result of this problem


def main():
    # Example 1: Output: true
    # n = 1

    # Example 2: Output: false
    # n = 2

    # Example 3: Output: true
    # n = 4

    # Example 4: Output: true
    n = 1000

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.winnerSquareGame(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
