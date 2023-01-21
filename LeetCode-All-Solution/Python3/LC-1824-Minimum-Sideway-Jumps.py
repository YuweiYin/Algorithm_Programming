#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1824-Minimum-Sideway-Jumps.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1824 - (Medium) - Minimum Sideway Jumps
https://leetcode.com/problems/minimum-sideway-jumps/

Description & Requirement:
    There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. 
    A frog starts at point 0 in the second lane and wants to jump to point n. 
    However, there could be obstacles along the way.

    You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) 
    describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i.
    There will be at most one obstacle in the 3 lanes at each point.

        For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.

    The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane 
    at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane 
    (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

        For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.

    Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

    Note: There will be no obstacles on points 0 and n.

Example 1:
    Input: obstacles = [0,1,2,3,0]
    Output: 2 
    Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
        Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).
Example 2:
    Input: obstacles = [0,1,1,3,3,0]
    Output: 0
    Explanation: There are no obstacles on lane 2. No side jumps are required.
Example 3:
    Input: obstacles = [0,2,1,0,3,0]
    Output: 2
    Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.

Constraints:
    obstacles.length == n + 1
    1 <= n <= 5 * 10^5
    0 <= obstacles[i] <= 3
    obstacles[0] == obstacles[n] == 0
"""


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # exception case
        assert isinstance(obstacles, list) and len(obstacles) >= 2
        # main method: (dynamic programming)
        return self._minSideJumps(obstacles)

    def _minSideJumps(self, obstacles: List[int]) -> int:
        assert isinstance(obstacles, list) and len(obstacles) >= 2

        dp = [1, 0, 1]

        for i in range(1, len(obstacles)):
            min_jump = float("inf")

            for j in range(3):
                if j == obstacles[i] - 1:
                    dp[j] = float("inf")
                else:
                    min_jump = min(min_jump, dp[j])

            for j in range(3):
                if j != obstacles[i] - 1:
                    dp[j] = min(dp[j], min_jump + 1)

        return min(dp)


def main():
    # Example 1: Output: 2
    # obstacles = [0, 1, 2, 3, 0]

    # Example 2: Output: 0
    # obstacles = [0, 1, 1, 3, 3, 0]

    # Example 3: Output: 2
    obstacles = [0, 2, 1, 0, 3, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minSideJumps(obstacles)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
