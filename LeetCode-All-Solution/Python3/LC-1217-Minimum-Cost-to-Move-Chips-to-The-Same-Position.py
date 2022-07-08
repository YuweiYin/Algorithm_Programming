#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1217-Minimum-Cost-to-Move-Chips-to-The-Same-Position.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1217 - (Easy) - Minimum Cost to Move Chips to The Same Position
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

Description & Requirement:
    We have n chips, where the position of the ith chip is position[i].

    We need to move all the chips to the same position. 
    In one step, we can change the position of the ith chip from position[i] to:
        position[i] + 2 or position[i] - 2 with cost = 0.
        position[i] + 1 or position[i] - 1 with cost = 1.

    Return the minimum cost needed to move all the chips to the same position.

Example 1:
    Input: position = [1,2,3]
    Output: 1
    Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
        Second step: Move the chip at position 2 to position 1 with cost = 1.
        Total cost is 1.
Example 2:
    Input: position = [2,2,2,3,3]
    Output: 2
    Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
Example 3:
    Input: position = [1,1000000000]
    Output: 1

Constraints:
    1 <= position.length <= 100
    1 <= position[i] <= 10^9
"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # exception case
        assert isinstance(position, list) and len(position) >= 1
        # main method: (we can always move chips to the first or second position without cost)
        return self._minCostToMoveChips(position)

    def _minCostToMoveChips(self, position: List[int]) -> int:
        """
        Runtime: 35 ms, faster than 90.31% of Python3 submissions for Minimum Cost to Move Chips to The Same Position.
        Memory Usage: 14 MB, less than 13.23% of Python3 submissions for Minimum Cost to Move Chips to The Same Position
        """
        assert isinstance(position, list) and len(position) >= 1

        counter = dict({0: 0, 1: 0})
        for chips in position:
            counter[chips & 0x01] += 1

        return min(counter[0], counter[1])


def main():
    # Example 1: Output: 1
    # position = [1, 2, 3]

    # Example 2: Output: 2
    # position = [2, 2, 2, 3, 3]

    # Example 3: Output: 1
    position = [1, 1000000000]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCostToMoveChips(position)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
