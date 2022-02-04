#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1725-Number-Of-Rectangles-That-Can-Form-The-Largest-Square.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-04
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1725 - (Easy) - Number Of Rectangles That Can Form The Largest Square
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

Description & Requirement:
    You are given an array rectangles where rectangles[i] = [l_i, w_i] 
    represents the ith rectangle of length l_i and width w_i.

    You can cut the ith rectangle to form a square with a side length of k if both k <= l_i and k <= w_i. 
    For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

    Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

    Return the number of rectangles that can make a square with a side length of maxLen.

Example 1:
    Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
    Output: 3
    Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
    The largest possible square is of length 5, and you can get it out of 3 rectangles.
Example 2:
    Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
    Output: 3

Constraints:
    1 <= rectangles.length <= 1000
    rectangles[i].length == 2
    1 <= li, wi <= 10^9
    li != wi
"""


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # exception case
        if not isinstance(rectangles, list) or len(rectangles) <= 0:
            return 0
        # main method: (min(length, width) is the length of each square, then count the number of max square length)
        return self._countGoodRectangles(rectangles)

    def _countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        assert len(rectangles) >= 1

        # min(length, width) is the length of each square
        square_len_list = [min(length, width) for length, width in rectangles]
        max_square_len = max(square_len_list)

        # count the number of max square length
        res = 0
        for square_len in square_len_list:
            if square_len == max_square_len:
                res += 1

        return res


def main():
    # Example 1: Output: 3
    rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]

    # Example 2: Output: 3
    # rectangles = [[2, 3], [3, 7], [4, 3], [3, 7]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countGoodRectangles(rectangles)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
