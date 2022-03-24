#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0661-Image-Smoother.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-24
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0661 - (Easy) - Image Smoother
https://leetcode.com/problems/image-smoother/

Description & Requirement:
    An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image 
    by rounding down the average of the cell and the eight surrounding cells 
    (i.e., the average of the nine cells in the blue smoother). 
    If one or more of the surrounding cells of a cell is not present, 
    we do not consider it in the average (i.e., the average of the four cells in the red smoother).

    Given an m x n integer matrix img representing the grayscale of an image, 
    return the image after applying the smoother on each cell of it.

Example 1:
    Input: img = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[0,0,0],[0,0,0],[0,0,0]]
    Explanation:
        For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
        For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
        For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:
    Input: img = [[100,200,100],[200,50,200],[100,200,100]]
    Output: [[137,141,137],[141,138,141],[137,141,137]]
    Explanation:
        For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
        For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
        For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:
    m == img.length
    n == img[i].length
    1 <= m, n <= 200
    0 <= img[i][j] <= 255
"""


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(img, list) and len(img) > 0
        max_col = len(img[0])
        for row in img:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (1. just calculate average of all cells; 2-dim prefix sum.)
        return self._imageSmoother(img)

    def _imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        assert len(img) > 0 and len(img[0]) > 0
        max_row = len(img)
        max_col = len(img[0])

        idx_shift = [[0, 0], [0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]

        res = [[0 for _ in range(max_col)] for _ in range(max_row)]
        for row_idx in range(max_row):
            for col_idx in range(max_col):
                cur_sum = 0
                cur_counter = 0
                for shift in idx_shift:
                    cur_row, cur_col = row_idx + shift[0], col_idx + shift[1]
                    if 0 <= cur_row < max_row and 0 <= cur_col < max_col:
                        cur_sum += img[cur_row][cur_col]
                        cur_counter += 1
                if cur_counter > 0:
                    res[row_idx][col_idx] = int(cur_sum / cur_counter)

        return res


def main():
    # Example 1: Output: [[0,0,0],[0,0,0],[0,0,0]]
    # img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    # Example 2: Output: [[137,141,137],[141,138,141],[137,141,137]]
    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.imageSmoother(img)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
