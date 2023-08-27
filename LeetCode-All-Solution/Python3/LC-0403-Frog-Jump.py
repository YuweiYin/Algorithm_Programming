#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0403-Frog-Jump.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 0403 - (Hard) Frog Jump
https://leetcode.com/problems/frog-jump/

Description & Requirement:
    A frog is crossing a river. The river is divided into some number of units, and at each unit, 
    there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

    Given a list of stones' positions (in units) in sorted ascending order, 
    determine if the frog can cross the river by landing on the last stone. 
    Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

    If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. 
    The frog can only jump in the forward direction.

Example 1:
    Input: stones = [0,1,3,5,6,8,12,17]
    Output: true
    Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, 
        then 2 units to the 3rd stone, then 2 units to the 4th stone, 
        then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:
    Input: stones = [0,1,2,3,4,8,9,11]
    Output: false
    Explanation: There is no way to jump to the last stone as the gap 
        between the 5th and 6th stone is too large.

Constraints:
    2 <= stones.length <= 2000
    0 <= stones[i] <= 2^31 - 1
    stones[0] == 0
    stones is sorted in a strictly increasing order.
"""


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # exception case
        assert isinstance(stones, list) and len(stones) >= 2
        # main method: (dynamic programming)
        return self._canCross(stones)

    def _canCross(self, stones: List[int]) -> bool:
        assert isinstance(stones, list) and len(stones) >= 2

        n = len(stones)
        dp = [[False for _ in range(n + 1)] for _ in range(n)]
        if stones[1] != 1:
            return False
        dp[0][0] = dp[1][1] = True

        for i in range(2, n):
            for j in range(i - 1, -1, -1):
                diff = stones[i] - stones[j]
                if diff >= n:
                    break
                if dp[j][diff - 1] or dp[j][diff] or dp[j][diff + 1]:
                    dp[i][diff] = True

        for j in range(n):
            if dp[n - 1][j]:
                return True

        return False


def main():
    # Example 1: Output: true
    stones = [0, 1, 3, 5, 6, 8, 12, 17]

    # Example 2: Output: false
    # stones = [0, 1, 2, 3, 4, 8, 9, 11]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.canCross(stones)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
