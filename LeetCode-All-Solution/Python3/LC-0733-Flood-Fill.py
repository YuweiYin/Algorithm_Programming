#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0733-Flood-Fill.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-07
=================================================================="""

import sys
import time
from typing import List
import queue
# import collections

"""
LeetCode - 0733 - (Easy) - Flood Fill
https://leetcode.com/problems/flood-fill/

Description:
    An image is represented by an m x n integer grid image where 
    image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and newColor. 
    You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, 
    plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
    plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
    Replace the color of all of the aforementioned pixels with newColor.

Requirement:
    Return the modified image after performing the flood fill.

Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
    Output: [[2,2,2],[2,2,2]]

Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], newColor < 216
    0 <= sr < m
    0 <= sc < n
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # exception case
        if not isinstance(image, list) or len(image) <= 0 or not isinstance(image[0], list):
            return image
        len_c = len(image[0])  # check every row is the same length
        for row in image:
            if not isinstance(row, list) or len(row) != len_c:
                return image
        if not isinstance(sr, int) or not isinstance(sc, int) or not isinstance(newColor, int):
            return image
        if sr >= len(image) or sr < 0 or sc >= len_c or sc < 0:  # check if indices are out of boundary
            return image
        if newColor == image[sr][sc]:  # needn't change color
            return image
        # main method: BFS or DFS
        return self._floodFillBFS(image, sr, sc, newColor)
        # return self._floodFillDFS(image, sr, sc, newColor)

    def _floodFillBFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        len_r = len(image)
        len_c = len(image[0])
        target_color = image[sr][sc]  # record the target_color to find the valid neighbors

        # next_queue = collections.deque()  # BFS queue
        next_queue = queue.Queue()  # BFS queue
        next_queue.put([sr, sc])

        while not next_queue.empty():
            cur_r, cur_c = next_queue.get()  # get current block to be drawn
            if image[cur_r][cur_c] == target_color:  # avoid repeated block
                image[cur_r][cur_c] = newColor  # draw it
                # find valid neighbors (4 directions) and add them into the queue
                if cur_r + 1 < len_r and image[cur_r + 1][cur_c] == target_color:
                    next_queue.put([cur_r + 1, cur_c])
                if cur_r - 1 >= 0 and image[cur_r - 1][cur_c] == target_color:
                    next_queue.put([cur_r - 1, cur_c])
                if cur_c + 1 < len_c and image[cur_r][cur_c + 1] == target_color:
                    next_queue.put([cur_r, cur_c + 1])
                if cur_c - 1 >= 0 and image[cur_r][cur_c - 1] == target_color:
                    next_queue.put([cur_r, cur_c - 1])

        return image

    def _floodFillDFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        len_r = len(image)
        len_c = len(image[0])
        target_color = image[sr][sc]  # record the target_color to find the valid neighbors

        def __dfs(cur_r: int, cur_c: int) -> None:
            image[cur_r][cur_c] = newColor  # draw it
            # find valid neighbors (4 directions) and perform dfs
            if cur_r + 1 < len_r and image[cur_r + 1][cur_c] == target_color:
                __dfs(cur_r + 1, cur_c)
            if cur_r - 1 >= 0 and image[cur_r - 1][cur_c] == target_color:
                __dfs(cur_r - 1, cur_c)
            if cur_c + 1 < len_c and image[cur_r][cur_c + 1] == target_color:
                __dfs(cur_r, cur_c + 1)
            if cur_c - 1 >= 0 and image[cur_r][cur_c - 1] == target_color:
                __dfs(cur_r, cur_c - 1)

        __dfs(sr, sc)
        return image


def main():
    # Example 1: Output: [[2,2,2],[2,2,0],[2,0,1]]
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2

    # Example 2: Output: [[2,2,2],[2,2,2]]
    # image = [[0, 0, 0], [0, 0, 0]]
    # sr = 0
    # sc = 0
    # newColor = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.floodFill(image, sr, sc, newColor)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
