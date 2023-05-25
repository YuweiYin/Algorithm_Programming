#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0837-New-21-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-25
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0837 - (Medium) - New 21 Game
https://leetcode.com/problems/new-21-game/

Description & Requirement:
    Alice plays the following game, loosely based on the card game "21".

    Alice starts with 0 points and draws numbers while she has less than k points. During each draw, 
    she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. 
    Each draw is independent and the outcomes have equal probabilities.

    Alice stops drawing numbers when she gets k or more points.

    Return the probability that Alice has n or fewer points.

    Answers within 10-5 of the actual answer are considered accepted.

Example 1:
    Input: n = 10, k = 1, maxPts = 10
    Output: 1.00000
    Explanation: Alice gets a single card, then stops.
Example 2:
    Input: n = 6, k = 1, maxPts = 10
    Output: 0.60000
    Explanation: Alice gets a single card, then stops.
        In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:
    Input: n = 21, k = 17, maxPts = 10
    Output: 0.73278

Constraints:
    0 <= k <= n <= 10^4
    1 <= maxPts <= 10^4
"""


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # exception case
        assert isinstance(n, int) and isinstance(k, int) and 0 <= k <= n
        assert isinstance(maxPts, int) and maxPts >= 1
        # main method: (dynamic programming)
        return self._new21Game(n, k, maxPts)

    def _new21Game(self, n: int, k: int, maxPts: int) -> float:
        assert isinstance(n, int) and isinstance(k, int) and 0 <= k <= n
        assert isinstance(maxPts, int) and maxPts >= 1

        if k == 0:
            return 1.0

        dp = [0.0] * (k + maxPts)
        for i in range(k, min(n, k + maxPts - 1) + 1):
            dp[i] = 1.0

        dp[k - 1] = float(min(n - k + 1, maxPts)) / maxPts
        for i in range(k - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + maxPts + 1] - dp[i + 1]) / maxPts

        return float(dp[0])


def main():
    # Example 1: Output: 1.00000
    # n = 10
    # k = 1
    # maxPts = 10

    # Example 2: Output: 0.60000
    # n = 6
    # k = 1
    # maxPts = 10

    # Example 3: Output: 0.73278
    n = 21
    k = 17
    maxPts = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.new21Game(n, k, maxPts)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
