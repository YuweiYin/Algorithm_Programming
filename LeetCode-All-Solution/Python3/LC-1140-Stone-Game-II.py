#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1140-Stone-Game-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-22
=================================================================="""

import sys
import time
from typing import List
import functools
# import collections

"""
LeetCode - 1140 - (Medium) - Stone Game II
https://leetcode.com/problems/stone-game-ii/

Description & Requirement:
    Alice and Bob continue their games with piles of stones. 
    There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. 
    The objective of the game is to end with the most stones. 

    Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

    On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. 
    Then, we set M = max(M, X).

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:
    Input: piles = [2,7,9,4,4]
    Output: 10
    Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, 
        then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. 
        If Alice takes two piles at the beginning, then Bob can take all three piles left. 
        In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:
    Input: piles = [1,2,3,4,5,100]
    Output: 104

Constraints:
    1 <= piles.length <= 100
    1 <= piles[i] <= 10^4
"""


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # exception case
        assert isinstance(piles, list) and len(piles) >= 1
        # main method: (memorized search / dynamic programming + prefix sum)
        return self._stoneGameII(piles)

    def _stoneGameII(self, piles: List[int]) -> int:
        assert isinstance(piles, list) and len(piles) >= 1

        prefix_sum = [0]
        for pile in piles:
            prefix_sum.append(prefix_sum[-1] + pile)

        @functools.lru_cache(None)
        def __dp(index, m):
            if index == len(piles):
                return 0
            cur_max = - int(1e9+7)
            for x in range(1, (m << 1) + 1):
                if index + x > len(piles):
                    break
                cur_max = max(cur_max, prefix_sum[index + x] - prefix_sum[index] - __dp(index + x, max(m, x)))

            return cur_max

        return int(prefix_sum[-1] + __dp(0, 1)) >> 1


def main():
    # Example 1: Output: 10
    # piles = [2, 7, 9, 4, 4]

    # Example 2: Output: 104
    piles = [1, 2, 3, 4, 5, 100]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.stoneGameII(piles)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
