#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1691-Maximum-Height-by-Stacking-Cuboids.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-10
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1691 - (Hard) - Maximum Height by Stacking Cuboids
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

Description & Requirement:
    Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [width_i, length_i, height_i] (0-indexed). 
    Choose a subset of cuboids and place them on each other.

    You can place cuboid i on cuboid j if width_i <= width_j and length_i <= length_j and height_i <= height_j. 
    You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

    Return the maximum height of the stacked cuboids.

Example 1:
    Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
    Output: 190
    Explanation:
        Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
        Cuboid 0 is placed next with the 45x20 side facing down with height 50.
        Cuboid 2 is placed next with the 23x12 side facing down with height 45.
        The total height is 95 + 50 + 45 = 190.
Example 2:
    Input: cuboids = [[38,25,45],[76,35,3]]
    Output: 76
    Explanation:
        You can't place any of the cuboids on the other.
        We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.
Example 3:
    Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
    Output: 102
    Explanation:
        After rearranging the cuboids, you can see that all cuboids have the same dimension.
        You can place the 11x7 side down on all cuboids so their heights are 17.
        The maximum height of stacked cuboids is 6 * 17 = 102.

Constraints:
    n == cuboids.length
    1 <= n <= 100
    1 <= width_i, length_i, height_i <= 100
"""


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # exception case
        assert isinstance(cuboids, list) and len(cuboids) >= 1
        # main method: (dynamic programming)
        return self._maxHeight(cuboids)

    def _maxHeight(self, cuboids: List[List[int]]) -> int:
        assert isinstance(cuboids, list) and len(cuboids) >= 1

        n = len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort(key=lambda x: sum(x))

        res = 0
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1] and cuboids[i][2] >= cuboids[j][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
            res = max(res, dp[i])

        return res


def main():
    # Example 1: Output: 190
    # cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]

    # Example 2: Output: 76
    # cuboids = [[38, 25, 45], [76, 35, 3]]

    # Example 3: Output: 102
    cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxHeight(cuboids)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
