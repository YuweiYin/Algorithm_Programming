#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1823-Find-the-Winner-of-the-Circular-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-24
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1823 - (Medium) - Find the Winner of the Circular Game
https://leetcode.com/problems/find-the-winner-of-the-circular-game/

Description & Requirement:
    There are n friends that are playing a game. 
    The friends are sitting in a circle and are numbered from 1 to n in clockwise order. 
    More formally, moving clockwise from the i-th friend brings you to the (i+1)-th friend for 1 <= i < n, 
    and moving clockwise from the n-th friend brings you to the 1-st friend.

    The rules of the game are as follows:
        1. Start at the 1st friend.
        2. Count the next k friends in the clockwise direction including the friend you started at. 
            The counting wraps around the circle and may count some friends more than once.
        3. The last friend you counted leaves the circle and loses the game.
        4.1. If there is still more than one friend in the circle, 
            go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
        4.2. Else, the last friend in the circle wins the game.

    Given the number of friends, n, and an integer k, return the winner of the game.

Example 1:
    Input: n = 5, k = 2
    Output: 3
    Explanation: Here are the steps of the game:
        1) Start at friend 1.
        2) Count 2 friends clockwise, which are friends 1 and 2.
        3) Friend 2 leaves the circle. Next start is friend 3.
        4) Count 2 friends clockwise, which are friends 3 and 4.
        5) Friend 4 leaves the circle. Next start is friend 5.
        6) Count 2 friends clockwise, which are friends 5 and 1.
        7) Friend 1 leaves the circle. Next start is friend 3.
        8) Count 2 friends clockwise, which are friends 3 and 5.
        9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
Example 2:
    Input: n = 6, k = 5
    Output: 1
    Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

Constraints:
    1 <= k <= n <= 500
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # exception case
        assert isinstance(n, int) and n > 0
        assert isinstance(k, int) and n >= k > 0
        # main method: (1. simulate the process; 2. [Josephus problem](https://en.wikipedia.org/wiki/Josephus_problem))
        return self._findTheWinner(n, k)

    def _findTheWinner(self, n: int, k: int) -> int:

        def __josephus(_n, _k):
            if _n == 1:  # only 1 left, that is the winner
                return 1
            else:
                # __josephus(_n - 1, _k) means someone has lost
                # note than __josephus(_n - 1, _k) will consider the position starting from (k % n) + 1 instead of 1
                #     because (k % n)-th person was lost
                # winner is considered as position 1, so the former position of winner is (1 + (k - 1) % n) + 1 = k + 1
                #     then former position of winner is ((k + 1) + (k - 1) % n) + 1 = 2k + 1, and so on (always Nk + 1)
                return ((__josephus(_n - 1, _k) + _k - 1) % _n) + 1

        return __josephus(n, k)


def main():
    # Example 1: Output: 3
    n = 5
    k = 2

    # Example 2: Output: 1
    # n = 6
    # k = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findTheWinner(n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
