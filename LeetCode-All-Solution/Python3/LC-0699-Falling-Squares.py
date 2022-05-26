#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0699-Falling-Squares.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-26
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0699 - (Hard) - Falling Squares
https://leetcode.com/problems/falling-squares/

Description & Requirement:
    There are several squares being dropped onto the X-axis of a 2D plane.

    You are given a 2D integer array positions where positions[i] = [left_i, sideLength_i] represents the i-th square 
    with a side length of sideLength_i that is dropped with its left edge aligned with X-coordinate left_i.

    Each square is dropped one at a time from a height above any landed squares. It then falls downward 
    (negative Y direction) until it either lands on the top side of another square or on the X-axis. 
    A square brushing the left/right side of another square does not count as landing on it. 
    Once it lands, it freezes in place and cannot be moved.

    After each square is dropped, you must record the height of the current tallest stack of squares.

    Return an integer array ans where ans[i] represents the height described above after dropping the ith square.

Example 1:
    Input: positions = [[1,2],[2,3],[6,1]]
    Output: [2,5,5]
    Explanation:
        After the first drop, the tallest stack is square 1 with a height of 2.
        After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
        After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
        Thus, we return an answer of [2, 5, 5].
Example 2:
    Input: positions = [[100,100],[200,100]]
    Output: [100,100]
    Explanation:
        After the first drop, the tallest stack is square 1 with a height of 100.
        After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
        Thus, we return an answer of [100, 100].
        Note that square 2 only brushes the right side of square 1, which does not count as landing on it.

Constraints:
    1 <= positions.length <= 1000
    1 <= left_i <= 10^8
    1 <= sideLength_i <= 10^6
"""


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(positions, list) and len(positions) >= 1
        for position in positions:
            assert isinstance(position, list) and len(position) == 2 and position[0] >= 1 and position[1] >= 1
        # main method: (simulate the process, update the max height of each point of the abscissa; or Segment Tree)
        return self._fallingSquares(positions)

    def _fallingSquares(self, positions: List[List[int]]) -> List[int]:
        assert isinstance(positions, list) and len(positions) >= 1
        len_pos = len(positions)

        res = [0 for _ in range(len_pos)]
        for i in range(len_pos):
            left_i, side_i, right_i = positions[i][0], positions[i][1], sum(positions[i])
            res[i] = side_i  # the height of res[i] is at least side_i
            for j in range(i):
                left_j, right_j = positions[j][0], sum(positions[j])
                if left_i < right_j and left_j < right_i:  # interval overlapping
                    res[i] = max(res[i], res[j] + side_i)  # update res[i]
        for i in range(1, len_pos):
            res[i] = max(res[i], res[i - 1])

        return res


def main():
    # Example 1: Output: [2,5,5]
    positions = [[1, 2], [2, 3], [6, 1]]

    # Example 2: Output: [100,100]
    # positions = [[100, 100], [200, 100]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.fallingSquares(positions)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
