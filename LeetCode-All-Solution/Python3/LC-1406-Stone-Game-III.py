#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1406-Stone-Game-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1406 - (Hard) - Stone Game III
https://leetcode.com/problems/stone-game-iii/

Description & Requirement:
    Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, 
    and each stone has an associated value which is an integer given in the array stoneValue.

    Alice and Bob take turns, with Alice starting first. On each player's turn, 
    that player can take 1, 2, or 3 stones from the first remaining stones in the row.

    The score of each player is the sum of the values of the stones taken. 
    The score of each player is 0 initially.

    The objective of the game is to end with the highest score, and 
    the winner is the player with the highest score and there could be a tie. 
    The game continues until all the stones have been taken.

    Assume Alice and Bob play optimally.

    Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

Example 1:
    Input: values = [1,2,3,7]
    Output: "Bob"
    Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. 
        Now the score of Bob is 7 and Bob wins.
Example 2:
    Input: values = [1,2,3,-9]
    Output: "Alice"
    Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
        If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, 
            Alice will take the pile with value = -9 and lose.
        If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, 
            Alice will take the pile with value = -9 and also lose.
        Remember that both play optimally so here Alice will choose the scenario that makes her win.
Example 3:
    Input: values = [1,2,3,6]
    Output: "Tie"
    Explanation: Alice cannot win this game. She can end the game in a draw if 
        she decided to choose all the first three piles, otherwise she will lose.

Constraints:
    1 <= stoneValue.length <= 5 * 10^4
    -1000 <= stoneValue[i] <= 1000
"""


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # exception case
        assert isinstance(stoneValue, list) and len(stoneValue) >= 1
        # main method: (dynamic programming & suffix sum)
        return self._stoneGameIII(stoneValue)

    def _stoneGameIII(self, stoneValue: List[int]) -> str:
        assert isinstance(stoneValue, list) and len(stoneValue) >= 1

        n = len(stoneValue)

        suffix_sum = [0] * (n - 1) + [stoneValue[-1]]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]

        dp = [0] * n + [0]
        for i in range(n - 1, -1, -1):
            dp[i] = suffix_sum[i] - min(dp[i + 1:i + 4])

        total = sum(stoneValue)
        if dp[0] * 2 == total:
            return "Tie"
        else:
            return "Alice" if (dp[0] * 2 > total) else "Bob"


def main():
    # Example 1: Output: "Bob"
    values = [1, 2, 3, 7]

    # Example 2: Output: "Alice"
    # values = [1, 2, 3, -9]

    # Example 3: Output: "Tie"
    # values = [1, 2, 3, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.stoneGameIII(values)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
