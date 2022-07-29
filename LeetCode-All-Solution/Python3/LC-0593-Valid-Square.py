#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0593-Valid-Square.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-29
=================================================================="""

import sys
import time
from typing import List, Tuple

# import functools

"""
LeetCode - 0593 - (Medium) - Valid Square
https://leetcode.com/problems/valid-square/

Description & Requirement:
    Given the coordinates of four points in 2D space p1, p2, p3 and p4, 
    return true if the four points construct a square.

    The coordinate of a point pi is represented as [xi, yi]. 
    The input is not given in any order.

    A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Example 1:
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: true
Example 2:
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
    Output: false
Example 3:
    Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
    Output: true

Constraints:
    p1.length == p2.length == p3.length == p4.length == 2
    -10^4 <= xi, yi <= 10^4
"""


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # exception case
        assert isinstance(p1, list) and isinstance(p2, list) and isinstance(p3, list) and isinstance(p4, list)
        assert len(p1) == len(p2) == len(p3) == len(p4) == 2
        # main method: (computational geometry)
        return self._validSquare(p1, p2, p3, p4)

    def _validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        assert isinstance(p1, list) and isinstance(p2, list) and isinstance(p3, list) and isinstance(p4, list)
        assert len(p1) == len(p2) == len(p3) == len(p4) == 2

        def __is_length_equal(vec1: Tuple[int, int], vec2: Tuple[int, int]) -> bool:
            return vec1[0] * vec1[0] + vec1[1] * vec1[1] == vec2[0] * vec2[0] + vec2[1] * vec2[1]

        def __is_mid_point_same(pt1: List[int], pt2: List[int], pt3: List[int], pt4: List[int]) -> bool:
            # return True if the mid points of the parallelogram's two diagonals are the same point
            return pt1[0] + pt2[0] == pt3[0] + pt4[0] and pt1[1] + pt2[1] == pt3[1] + pt4[1]

        def __vector_cosine(vec1: Tuple[int, int], vec2: Tuple[int, int]) -> int:
            return vec1[0] * vec2[0] + vec1[1] * vec2[1]

        def __is_square(pt1: List[int], pt2: List[int], pt3: List[int], pt4: List[int]) -> bool:
            vector_1 = (pt1[0] - pt2[0], pt1[1] - pt2[1])
            vector_2 = (pt3[0] - pt4[0], pt3[1] - pt4[1])
            return __is_mid_point_same(pt1, pt2, pt3, pt4) and \
                __is_length_equal(vector_1, vector_2) and \
                __vector_cosine(vector_1, vector_2) == 0

        if p1 == p2:
            return False
        if __is_square(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if __is_square(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if __is_square(p1, p4, p2, p3):
            return True

        return False


def main():
    # Example 1: Output: true
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]

    # Example 2: Output: false
    # p1 = [0, 0]
    # p2 = [1, 1]
    # p3 = [1, 0]
    # p4 = [0, 12]

    # Example 3: Output: true
    # p1 = [1, 0]
    # p2 = [-1, 0]
    # p3 = [0, 1]
    # p4 = [0, -1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.validSquare(p1, p2, p3, p4)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
