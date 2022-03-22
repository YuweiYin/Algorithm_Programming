#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2038-Remove-Colored-Pieces-if-Both-Neighbors-are-the-Same-Color.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-22
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 2038 - (Medium) - Remove Colored Pieces if Both Neighbors are the Same Color
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

Description & Requirement:
    There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. 
    You are given a string colors of length n where colors[i] is the color of the ith piece.

    Alice and Bob are playing a game where they take alternating turns removing pieces from the line. 
    In this game, Alice moves first.

    Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. 
        She is not allowed to remove pieces that are colored 'B'.
    Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. 
        He is not allowed to remove pieces that are colored 'A'.
    Alice and Bob cannot remove pieces from the edge of the line.

    If a player cannot make a move on their turn, that player loses and the other player wins.
    Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

Example 1:
    Input: colors = "AAABABB"
    Output: true
    Explanation:
        AAABABB -> AABABB
        Alice moves first.
        She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.
    
        Now it's Bob's turn.
        Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
        Thus, Alice wins, so return true.
Example 2:
    Input: colors = "AA"
    Output: false
    Explanation:
        Alice has her turn first.
        There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
        Thus, Bob wins, so return false.
Example 3:
    Input: colors = "ABBBBBBBAAA"
    Output: false
    Explanation:
        ABBBBBBBAAA -> ABBBBBBBAA
        Alice moves first.
        Her only option is to remove the second to last 'A' from the right.
    
        ABBBBBBBAA -> ABBBBBBAA
        Next is Bob's turn.
        He has many options for which 'B' piece to remove. He can pick any.
    
        On Alice's second turn, she has no more pieces that she can remove.
        Thus, Bob wins, so return false.

Constraints:
    1 <= colors.length <= 10^5
    colors consists of only the letters 'A' and 'B'
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # exception case
        assert isinstance(colors, str) and len(colors) > 0
        # main method: (the total number of movement can be determined at first)
        #     because Alice's movement (removing "A" for "AAA") won't add a "BBB" for Bob to move. and vice versa.
        return self._winnerOfGame(colors)

    def _winnerOfGame(self, colors: str) -> bool:
        len_colors = len(colors)
        assert len_colors > 0
        if len_colors < 3:
            return False

        total_move_alice = 0
        total_move_bob = 0
        for idx in range(3, len_colors + 1):
            cur_triplet = colors[idx - 3: idx]
            if cur_triplet == "AAA":
                total_move_alice += 1
            elif cur_triplet == "BBB":
                total_move_bob += 1
            else:
                continue

        return total_move_alice > total_move_bob


def main():
    # Example 1: Output: true
    colors = "AAABABB"

    # Example 2: Output: false
    # colors = "AA"

    # Example 3: Output: false
    # colors = "ABBBBBBBAAA"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.winnerOfGame(colors)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
