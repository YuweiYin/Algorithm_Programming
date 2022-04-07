#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1046-Last-Stone-Weight.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-07
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools

"""
LeetCode - 1046 - (Easy) - Last Stone Weight
https://leetcode.com/problems/last-stone-weight/

Description & Requirement:
    You are given an array of integers stones where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
    Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

    At the end of the game, there is at most one stone left.

    Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation: 
        We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:
    Input: stones = [1]
    Output: 1

Constraints:
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # exception case
        assert isinstance(stones, list) and len(stones) >= 1
        # main method: (heap stimulate)
        return self._lastStoneWeight(stones)

    def _lastStoneWeight(self, stones: List[int]) -> int:
        assert len(stones) >= 1

        stones = [- stone for stone in stones]  # heapify in descending order
        heapq.heapify(stones)

        while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, - abs(x - y))

        return - stones[0] if len(stones) > 0 else 0


def main():
    # Example 1: Output: 1
    # stones = [2, 7, 4, 1, 8, 1]

    # Example 2: Output: 1
    stones = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lastStoneWeight(stones)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
