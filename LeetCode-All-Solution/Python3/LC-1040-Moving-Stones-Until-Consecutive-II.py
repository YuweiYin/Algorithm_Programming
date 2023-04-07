#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1040-Moving-Stones-Until-Consecutive-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-07
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1040 - (Medium) - Moving Stones Until Consecutive II
https://leetcode.com/problems/moving-stones-until-consecutive-ii/

Description & Requirement:
    There are some stones in different positions on the X-axis. 
    You are given an integer array stones, the positions of the stones.

    Call a stone an endpoint stone if it has the smallest or largest position. 
    In one move, you pick up an endpoint stone and move it to an unoccupied position 
    so that it is no longer an endpoint stone.

        In particular, if the stones are at say, stones = [1,2,5], you cannot move 
        the endpoint stone at position 5, since moving it to any position (such as 0, or 3) 
        will still keep that stone as an endpoint stone.

    The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

    Return an integer array answer of length 2 where:
        answer[0] is the minimum number of moves you can play, and
        answer[1] is the maximum number of moves you can play.

Example 1:
    Input: stones = [7,4,9]
    Output: [1,2]
    Explanation: We can move 4 -> 8 for one move to finish the game.
        Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
Example 2:
    Input: stones = [6,5,4,3,10]
    Output: [2,3]
    Explanation: We can move 3 -> 8 then 10 -> 7 to finish the game.
        Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
        Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.

Constraints:
    3 <= stones.length <= 10^4
    1 <= stones[i] <= 10^9
    All the values of stones are unique.
"""


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        # exception case
        assert isinstance(stones, list) and len(stones) >= 3
        # main method: (two pointers)
        return self._numMovesStonesII(stones)

    def _numMovesStonesII(self, stones: List[int]) -> List[int]:
        assert isinstance(stones, list) and len(stones) >= 3

        n = len(stones)
        stones.sort()
        if stones[-1] - stones[0] + 1 == n:
            return [0, 0]

        ma = max(stones[-2] - stones[0] + 1, stones[-1] - stones[1] + 1) - (n - 1)
        mi = n

        j = 0
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 <= n:
                j += 1
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                mi = min(mi, 2)
            else:
                mi = min(mi, n - (j - i + 1))

        return [mi, ma]


def main():
    # Example 1: Output: [1,2]
    # stones = [7, 4, 9]

    # Example 2: Output: [2,3]
    stones = [6, 5, 4, 3, 10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numMovesStonesII(stones)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
