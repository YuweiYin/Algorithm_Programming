#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1007-Minimum-Domino-Rotations-For-Equal-Row.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-20
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1007 - (Medium) - Minimum Domino Rotations For Equal Row
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

Description & Requirement:
    In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. 
    (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

    We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

    Return the minimum number of rotations so that all the values in tops are the same, 
        or all the values in bottoms are the same.
    If it cannot be done, return -1.

Example 1:
    Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
    Output: 2
    Explanation: 
        The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
        If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, 
            as indicated by the second figure.
Example 2:
    Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
    Output: -1
    Explanation: 
        In this case, it is not possible to rotate the dominoes to make one row of values equal.

Constraints:
    2 <= tops.length <= 2 * 10^4
    bottoms.length == tops.length
    1 <= tops[i], bottoms[i] <= 6
"""


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # exception case
        assert isinstance(tops, list) and len(tops) >= 2
        assert isinstance(bottoms, list) and len(tops) == len(bottoms)
        # main method: (all top[i] == top[0]/bottom[0] or all bottom[i] == top[0]/bottom[0], otherwise, return -1)
        return self._minDominoRotations(tops, bottoms)

    def _minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        len_domino = len(tops)
        assert len_domino == len(bottoms) >= 2

        # top_equal_swap_top[i] is the swap number of i-th domino in order to make all top[i] == top[0]
        top_equal_swap_top = [0 for _ in range(len_domino)]
        # top_equal_swap_bottom[i] is the swap number of i-th domino in order to make all top[i] == bottom[0]
        top_equal_swap_bottom = [0 for _ in range(len_domino)]
        # bottom_equal_swap_top[i] is the swap number of i-th domino in order to make all bottom[i] == top[0]
        bottom_equal_swap_top = [0 for _ in range(len_domino)]
        # bottom_equal_swap_bottom[i] is the swap number of i-th domino in order to make all bottom[i] == bottom[0]
        bottom_equal_swap_bottom = [0 for _ in range(len_domino)]

        target_top = tops[0]
        target_bottom = bottoms[0]

        for idx in range(len_domino):
            cur_top = tops[idx]
            cur_bottom = bottoms[idx]
            # top_equal_swap_top[i] is the swap number of i-th domino in order to make all top[i] == top[0]
            if cur_top != target_top:
                if cur_bottom == target_top:
                    top_equal_swap_top[idx] += 1
                else:
                    top_equal_swap_top[idx] = -1  # can not make it
            # top_equal_swap_bottom[i] is the swap number of i-th domino in order to make all top[i] == bottom[0]
            if cur_top != target_bottom:
                if cur_bottom == target_bottom:
                    top_equal_swap_bottom[idx] += 1
                else:
                    top_equal_swap_bottom[idx] = -1  # can not make it
            # bottom_equal_swap_top[i] is the swap number of i-th domino in order to make all bottom[i] == top[0]
            if cur_bottom != target_top:
                if cur_top == target_top:
                    bottom_equal_swap_top[idx] += 1
                else:
                    bottom_equal_swap_top[idx] = -1  # can not make it
            # bottom_equal_swap_bottom[i] is the swap number of i-th domino in order to make all bottom[i] == bottom[0]
            if cur_bottom != target_bottom:
                if cur_top == target_bottom:
                    bottom_equal_swap_bottom[idx] += 1
                else:
                    bottom_equal_swap_bottom[idx] = -1  # can not make it

        def __get_res(swap_list: list) -> int:
            ans = 0
            for swap_num in swap_list:
                if swap_num == -1:  # can not make it
                    return -1
                ans += swap_num
            return ans

        res = len_domino  # max
        res_1 = __get_res(top_equal_swap_top)
        res_2 = __get_res(top_equal_swap_bottom)
        res_3 = __get_res(bottom_equal_swap_top)
        res_4 = __get_res(bottom_equal_swap_bottom)
        if res_1 >= 0:
            res = min(res, res_1)
        if res_2 >= 0:
            res = min(res, res_2)
        if res_3 >= 0:
            res = min(res, res_3)
        if res_4 >= 0:
            res = min(res, res_4)
        return -1 if res == len_domino else res


def main():
    # Example 1: Output: 2
    tops = [2, 1, 2, 4, 2, 2]
    bottoms = [5, 2, 6, 2, 3, 2]

    # Example 2: Output: -1
    # tops = [3, 5, 1, 2, 3]
    # bottoms = [3, 6, 3, 3, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minDominoRotations(tops, bottoms)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
