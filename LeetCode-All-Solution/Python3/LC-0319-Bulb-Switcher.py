#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0319-Bulb-Switcher.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-27
=================================================================="""

import sys
import time
import math
# from typing import List
# import collections
# import functools

"""
LeetCode - 0319 - (Medium) - Bulb Switcher
https://leetcode.com/problems/bulb-switcher/

Description & Requirement:
    There are n bulbs that are initially off. 
    You first turn on all the bulbs, then you turn off every second bulb.

    On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
    For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb.

    Return the number of bulbs that are on after n rounds.

Example 1:
    Input: n = 3
    Output: 1
    Explanation: At first, the three bulbs are [off, off, off].
        After the first round, the three bulbs are [on, on, on].
        After the second round, the three bulbs are [on, off, on].
        After the third round, the three bulbs are [on, off, off]. 
        So you should return 1 because there is only one bulb is on.
Example 2:
    Input: n = 0
    Output: 0
Example 3:
    Input: n = 1
    Output: 1

Constraints:
    0 <= n <= 10^9
"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 0
        # main method: (mathematics)
        return self._bulbSwitch(n)

    def _bulbSwitch(self, n: int) -> int:
        assert isinstance(n, int) and n >= 0

        return int(math.sqrt(n + 0.5))


def main():
    # Example 1: Output: 1
    # n = 3

    # Example 2: Output: 0
    # n = 0

    # Example 3: Output: 1
    n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.bulbSwitch(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
