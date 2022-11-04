#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0754-Reach-a-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0754 - (Medium) - Reach a Number
https://leetcode.com/problems/reach-a-number/

Description & Requirement:
    You are standing at position 0 on an infinite number line. There is a destination at position target.

    You can make some number of moves numMoves so that:
        On each move, you can either go left or right.
        During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.

    Given the integer target, return the minimum number of moves required 
    (i.e., the minimum numMoves) to reach the destination.

Example 1:
    Input: target = 2
    Output: 3
    Explanation:
        On the 1st move, we step from 0 to 1 (1 step).
        On the 2nd move, we step from 1 to -1 (2 steps).
        On the 3rd move, we step from -1 to 2 (3 steps).
Example 2:
    Input: target = 3
    Output: 2
    Explanation:
        On the 1st move, we step from 0 to 1 (1 step).
        On the 2nd move, we step from 1 to 3 (2 steps).

Constraints:
    -10^9 <= target <= 10^9
    target != 0
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        # exception case
        assert isinstance(target, int) and target != 0
        # main method: (mathematics)
        return self._reachNumber(target)

    def _reachNumber(self, target: int) -> int:
        assert isinstance(target, int) and target != 0

        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + (k % 2)


def main():
    # Example 1: Output: 3
    # target = 2

    # Example 2: Output: 2
    target = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reachNumber(target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
