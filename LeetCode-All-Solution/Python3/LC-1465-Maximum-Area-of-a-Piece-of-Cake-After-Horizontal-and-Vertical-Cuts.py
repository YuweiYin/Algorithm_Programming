#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1465-Maximum-Area-of-a-Piece-of-Cake-After-Horizontal-and-Vertical-Cuts.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-02
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1465 - (Medium) - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

Description & Requirement:
    You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

        horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly,
        verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

    Return the maximum area of a piece of cake after you cut at each horizontal and vertical position 
    provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, 
    return this modulo 10^9 + 7.

Example 1:
    Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
    Output: 4 
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts.
        After you cut the cake, the green piece of cake has the maximum area.
Example 2:
    Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
    Output: 6
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts.
        After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:
    Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
    Output: 9

Constraints:
    2 <= h, w <= 10^9
    1 <= horizontalCuts.length <= min(h - 1, 10^5)
    1 <= verticalCuts.length <= min(w - 1, 10^5)
    1 <= horizontalCuts[i] < h
    1 <= verticalCuts[i] < w
    All the elements in horizontalCuts are distinct.
    All the elements in verticalCuts are distinct.
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # exception case
        assert isinstance(h, int) and h >= 2
        assert isinstance(w, int) and w >= 2
        assert isinstance(horizontalCuts, list) and 1 <= len(horizontalCuts) <= min(h - 1, int(1e5))
        assert isinstance(verticalCuts, list) and 1 <= len(verticalCuts) <= min(w - 1, int(1e5))
        for cut in horizontalCuts:
            assert isinstance(cut, int) and 1 <= cut < h
        for cut in verticalCuts:
            assert isinstance(cut, int) and 1 <= cut < w
        # main method: (sort height array and width array in descending order)
        return self._maxArea(h, w, horizontalCuts, verticalCuts)

    def _maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        assert isinstance(h, int) and h >= 2
        assert isinstance(w, int) and w >= 2
        assert isinstance(horizontalCuts, list) and 1 <= len(horizontalCuts) <= min(h - 1, int(1e5))
        assert isinstance(verticalCuts, list) and 1 <= len(verticalCuts) <= min(w - 1, int(1e5))

        MOD = int(1e9+7)

        horizontalCuts.sort()
        verticalCuts.sort()

        height = [(h - horizontalCuts[-1]) % MOD]
        width = [(w - verticalCuts[-1]) % MOD]

        last_cut = 0
        for cut in horizontalCuts:
            height.append((cut - last_cut) % MOD)
            last_cut = cut

        last_cut = 0
        for cut in verticalCuts:
            width.append((cut - last_cut) % MOD)
            last_cut = cut

        height.sort()
        width.sort()

        return int(height[-1] * width[-1]) % MOD


def main():
    # Example 1: Output: 4
    # h = 5
    # w = 4
    # horizontalCuts = [1, 2, 4]
    # verticalCuts = [1, 3]

    # Example 2: Output: 6
    # h = 5
    # w = 4
    # horizontalCuts = [3, 1]
    # verticalCuts = [1]

    # Example 3: Output: 9
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxArea(h, w, horizontalCuts, verticalCuts)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
