#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2335-Minimum-Amount-of-Time-to-Fill-Cups.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-11
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2335 - (Easy) - Minimum Amount of Time to Fill Cups
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

Description & Requirement:
    You have a water dispenser that can dispense cold, warm, and hot water. 
    Every second, you can either fill up 2 cups with different types of water, 
    or 1 cup of any type of water.

    You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] 
    denote the number of cold, warm, and hot water cups you need to fill respectively. 
    Return the minimum number of seconds needed to fill up all the cups.

Example 1:
    Input: amount = [1,4,2]
    Output: 4
    Explanation: One way to fill up the cups is:
        Second 1: Fill up a cold cup and a warm cup.
        Second 2: Fill up a warm cup and a hot cup.
        Second 3: Fill up a warm cup and a hot cup.
        Second 4: Fill up a warm cup.
        It can be proven that 4 is the minimum number of seconds needed.
Example 2:
    Input: amount = [5,4,4]
    Output: 7
    Explanation: One way to fill up the cups is:
        Second 1: Fill up a cold cup, and a hot cup.
        Second 2: Fill up a cold cup, and a warm cup.
        Second 3: Fill up a cold cup, and a warm cup.
        Second 4: Fill up a warm cup, and a hot cup.
        Second 5: Fill up a cold cup, and a hot cup.
        Second 6: Fill up a cold cup, and a warm cup.
        Second 7: Fill up a hot cup.
Example 3:
    Input: amount = [5,0,0]
    Output: 5
    Explanation: Every second, we fill up a cold cup.

Constraints:
    amount.length == 3
    0 <= amount[i] <= 100
"""


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # exception case
        assert isinstance(amount, list) and len(amount) == 3
        # main method: (sort & greedy)
        return self._fillCups(amount)

    def _fillCups(self, amount: List[int]) -> int:
        assert isinstance(amount, list) and len(amount) == 3

        amount.sort()
        if amount[2] > amount[1] + amount[0]:
            return amount[2]

        return (sum(amount) + 1) >> 1


def main():
    # Example 1: Output: 4
    # amount = [1, 4, 2]

    # Example 2: Output: 7
    amount = [5, 4, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.fillCups(amount)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
