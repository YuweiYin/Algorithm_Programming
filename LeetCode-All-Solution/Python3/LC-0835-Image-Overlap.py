#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0835-Image-Overlap.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-27
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0835 - (Medium) - Image Overlap
https://leetcode.com/problems/image-overlap/

Description & Requirement:
    You are given two images, img1 and img2, represented as binary, square matrices of size n x n. 
    A binary matrix has only 0s and 1s as values.

    We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down 
    any number of units. We then place it on top of the other image. We can then calculate the overlap by 
    counting the number of positions that have a 1 in both images.

    Note also that a translation does not include any kind of rotation. 
    Any 1 bits that are translated outside of the matrix borders are erased.

    Return the largest possible overlap.

Example 1:
    Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
    Output: 3
    Explanation: We translate img1 to right by 1 unit and down by 1 unit.
        The number of positions that have a 1 in both images is 3 (shown in red).
Example 2:
    Input: img1 = [[1]], img2 = [[1]]
    Output: 1
Example 3:
    Input: img1 = [[0]], img2 = [[0]]
    Output: 0

Constraints:
    n == img1.length == img1[i].length
    n == img2.length == img2[i].length
    1 <= n <= 30
    img1[i][j] is either 0 or 1.
    img2[i][j] is either 0 or 1.
"""


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # exception case
        assert isinstance(img1, list) and len(img1) >= 1
        n = len(img1)
        for row in img1:
            assert isinstance(row, list) and len(row) == n
        assert isinstance(img2, list) and len(img2) == n
        for row in img2:
            assert isinstance(row, list) and len(row) == n
        # main method: (loop, O(n^2 * n^2))
        return self._largestOverlap(img1, img2)

    def _largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        Runtime: 595 ms, faster than 85.96% of Python3 online submissions for Image Overlap.
        Memory Usage: 14.5 MB, less than 59.06% of Python3 online submissions for Image Overlap.
        """
        assert isinstance(img1, list) and len(img1) >= 1
        n = len(img1)
        assert isinstance(img2, list) and len(img2) == n

        cnt = collections.Counter()
        for i_1, row_1 in enumerate(img1):
            for j_1, v_1 in enumerate(row_1):
                if v_1 > 0:
                    for i_2, row_2 in enumerate(img2):
                        for j_2, v_2 in enumerate(row_2):
                            if v_2 > 0:
                                cnt[i_1 - i_2, j_1 - j_2] += 1

        return max(cnt.values() or [0])


def main():
    # Example 1: Output: 3
    img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
    img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]

    # Example 2: Output: 1
    # img1 = [[1]]
    # img2 = [[1]]

    # Example 3: Output: 0
    # img1 = [[0]]
    # img2 = [[0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestOverlap(img1, img2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
