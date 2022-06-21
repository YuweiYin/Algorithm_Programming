#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1642-Furthest-Building-You-Can-Reach.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-21
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools

"""
LeetCode - 1642 - (Medium) - Furthest Building You Can Reach
https://leetcode.com/problems/furthest-building-you-can-reach/

Description & Requirement:
    You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

    You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

    While moving from building i to building i+1 (0-indexed),
        If the current building's height is greater than or equal to the next building's height, 
            you do not need a ladder or bricks.
        If the current building's height is less than the next building's height, 
            you can either use one ladder or (h[i+1] - h[i]) bricks.

    Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example 1:
    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Output: 4
    Explanation: Starting at building 0, you can follow these steps:
        - Go to building 1 without using ladders nor bricks since 4 >= 2.
        - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
        - Go to building 3 without using ladders nor bricks since 7 >= 6.
        - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
        It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:
    Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
    Output: 7
Example 3:
    Input: heights = [14,3,19,3], bricks = 17, ladders = 0
    Output: 3

Constraints:
    1 <= heights.length <= 10^5
    1 <= heights[i] <= 10^6
    0 <= bricks <= 10^9
    0 <= ladders <= heights.length
"""


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # exception case
        assert isinstance(heights, list) and len(heights) >= 1
        for height in heights:
            assert isinstance(height, int) and height >= 1
        assert isinstance(bricks, int) and bricks >= 0
        assert isinstance(ladders, int) and 0 <= ladders <= len(heights)
        # main method: (Heap + Greedy)
        return self._furthestBuilding(heights, bricks, ladders)

    def _furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        assert isinstance(heights, list) and len(heights) >= 1
        assert isinstance(bricks, int) and bricks >= 0
        assert isinstance(ladders, int) and 0 <= ladders <= len(heights)

        heap = []
        heapq.heapify(heap)  # min heap, record the height of gaps
        height_for_bricks = 0  # the height that must be handled by bricks
        for idx in range(1, len(heights)):
            height_gap = heights[idx] - heights[idx - 1]
            if height_gap > 0:
                heapq.heappush(heap, height_gap)
                if len(heap) > ladders:  # the number of gaps is larger than that of ladders
                    height_for_bricks += heapq.heappop(heap)  # pop the min gap
                if height_for_bricks > bricks:  # if the existing bricks can not meet the needs, return
                    return idx - 1

        return len(heights) - 1  # max distance


def main():
    # Example 1: Output: 4
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1

    # Example 2: Output: 7
    # heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    # bricks = 10
    # ladders = 2

    # Example 3: Output: 3
    # heights = [14, 3, 19, 3]
    # bricks = 17
    # ladders = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.furthestBuilding(heights, bricks, ladders)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
