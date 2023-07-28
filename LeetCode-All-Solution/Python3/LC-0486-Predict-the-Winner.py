#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0486-Predict-the-Winner.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-28
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 0486 - (Medium) - Predict the Winner
https://leetcode.com/problems/predict-the-winner/

Description & Requirement:
    You are given an integer array nums. 
    Two players are playing a game with this array: player 1 and player 2.

    Player 1 and player 2 take turns, with player 1 starting first. 
    Both players start the game with a score of 0. At each turn, 
    the player takes one of the numbers from either end of the array 
    (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. 
    The player adds the chosen number to their score. 
    The game ends when there are no more elements in the array.

    Return true if Player 1 can win the game. If the scores of both players are equal, 
    then player 1 is still the winner, and you should also return true. 
    You may assume that both players are playing optimally.

Example 1:
    Input: nums = [1,5,2]
    Output: false
    Explanation: Initially, player 1 can choose between 1 and 2. 
        If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. 
        If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
        So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
        Hence, player 1 will never be the winner and you need to return false.
Example 2:
    Input: nums = [1,5,233,7]
    Output: true
    Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. 
        No matter which number player 2 choose, player 1 can choose 233.
        Finally, player 1 has more score (234) than player 2 (12), 
        so you need to return True representing player1 can win.

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 10^7
"""


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (dynamic programming)
        return self._PredictTheWinner(nums)

    def _PredictTheWinner(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 1

        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            dp[i] = num

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0


def main():
    # Example 1: Output: False
    # nums = [1, 5, 2]

    # Example 2: Output: True
    nums = [1, 5, 233, 7]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.PredictTheWinner(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
