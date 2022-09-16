#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0850-Rectangle-Area-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-16
=================================================================="""

import sys
import time
from typing import List
import bisect
# import collections
# import functools

"""
LeetCode - 0850 - (Hard) - Rectangle Area II
https://leetcode.com/problems/rectangle-area-ii/

Description & Requirement:
    You are given a 2D array of axis-aligned rectangles. 
    Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates 
    of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.

    Calculate the total area covered by all rectangles in the plane. 
    Any area covered by two or more rectangles should only be counted once.

    Return the total area. Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    Output: 6
    Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
    From (1,1) to (2,2), the green and red rectangles overlap.
    From (1,0) to (2,3), all three rectangles overlap.
Example 2:
    Input: rectangles = [[0,0,1000000000,1000000000]]
    Output: 49
    Explanation: The answer is 10^{18} modulo (10^9 + 7), which is 49.

Constraints:
    1 <= rectangles.length <= 200
    rectanges[i].length == 4
    0 <= xi1, yi1, xi2, yi2 <= 10^9
"""


class SegmentTree:
    def __init__(self):
        self.cover = 0
        self.length = 0
        self.max_length = 0


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # exception case
        assert isinstance(rectangles, list) and len(rectangles) >= 1
        for rec in rectangles:
            assert isinstance(rec, list) and len(rec) == 4
            for num in rec:
                assert isinstance(num, int) and num >= 0
        # main method: (Segment Tree)
        return self._rectangleArea(rectangles)

    def _rectangleArea(self, rectangles: List[List[int]]) -> int:
        assert isinstance(rectangles, list) and len(rectangles) >= 1

        bound = set()
        for rec in rectangles:
            bound.add(rec[1])  # lower bound
            bound.add(rec[3])  # upper bound

        bound = sorted(bound)
        m = len(bound)
        tree = [SegmentTree() for _ in range(m * 4 + 1)]

        def init(idx: int, l: int, r: int) -> None:
            tree[idx].cover = tree[idx].length = 0
            if l == r:
                tree[idx].max_length = bound[l] - bound[l - 1]
                return

            mid = (l + r) >> 1
            init(idx * 2, l, mid)
            init(idx * 2 + 1, mid + 1, r)
            tree[idx].max_length = tree[idx * 2].max_length + tree[idx * 2 + 1].max_length

        def update(idx: int, l: int, r: int, ul: int, ur: int, diff: int) -> None:
            if l > ur or r < ul:
                return
            if ul <= l and r <= ur:
                tree[idx].cover += diff
                pushup(idx, l, r)
                return

            mid = (l + r) >> 1
            update(idx * 2, l, mid, ul, ur, diff)
            update(idx * 2 + 1, mid + 1, r, ul, ur, diff)
            pushup(idx, l, r)

        def pushup(idx: int, l: int, r: int) -> None:
            if tree[idx].cover > 0:
                tree[idx].length = tree[idx].max_length
            elif l == r:
                tree[idx].length = 0
            else:
                tree[idx].length = tree[idx * 2].length + tree[idx * 2 + 1].length

        init(1, 1, m - 1)

        sweep = list()
        for i, rect in enumerate(rectangles):
            sweep.append((rect[0], i, 1))  # left bound
            sweep.append((rect[2], i, -1))  # right bound
        sweep.sort()

        ans = i = 0
        while i < len(sweep):
            j = i
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            if j + 1 == len(sweep):
                break

            # deal with the left and right bounds that have the same x-index
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                # binary search: get the index range of the completely covered segment
                left = bisect.bisect_left(bound, rectangles[idx][1]) + 1
                right = bisect.bisect_left(bound, rectangles[idx][3])
                update(1, 1, m - 1, left, right, diff)

            ans += tree[1].length * (sweep[j + 1][0] - sweep[j][0])
            i = j + 1

        return ans % int(1e9+7)


def main():
    # Example 1: Output: 6
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]

    # Example 2: Output: 49
    # rectangles = [[0, 0, 1000000000, 1000000000]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rectangleArea(rectangles)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
