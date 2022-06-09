#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0497-Random-Point-in-Non-overlapping-Rectangles.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-09
=================================================================="""

import sys
import time
from typing import List
import random
import bisect
# import functools

"""
LeetCode - 0497 - (Easy) - Random Point in Non-overlapping Rectangles
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

Description & Requirement:
    You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] 
    indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and 
    (xi, yi) is the top-right corner point of the ith rectangle. 
    Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. 
    A point on the perimeter of a rectangle is included in the space covered by the rectangle.

    Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

    Note that an integer point is a point that has integer coordinates.

    Implement the Solution class:
        Solution(int[][] rects) Initializes the object with the given rectangles rects.
        int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.

Example 1:
    Input
        ["Solution", "pick", "pick", "pick", "pick", "pick"]
        [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
    Output
        [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
    Explanation
        Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
        solution.pick(); // return [1, -2]
        solution.pick(); // return [1, -1]
        solution.pick(); // return [-1, -2]
        solution.pick(); // return [-2, -2]
        solution.pick(); // return [0, 0]

Constraints:
    1 <= rects.length <= 100
    rects[i].length == 4
    -10^9 <= ai < xi <= 10^9
    -10^9 <= bi < yi <= 10^9
    xi - ai <= 2000
    yi - bi <= 2000
    All the rectangles do not overlap.
    At most 10^4 calls will be made to pick.
"""


class Solution:

    def __init__(self, rects: List[List[int]]):
        """
        Time: O(n)
        """
        self.rects = rects
        self.prefix_sum = [0]  # 2-dim prefix sum
        for rect in rects:
            a, b, x, y = rect
            self.prefix_sum.append(self.prefix_sum[-1] + (x - a + 1) * (y - b + 1))

    def pick(self) -> List[int]:
        """
        Time: O(log n)
        Runtime: 174 ms, faster than 94.44% of Python3 online submissions for Random Point in Non-overlapping Rect.
        Memory Usage: 18.6 MB, less than 43.33% of Python3 online submissions for Random Point in Non-overlapping Rect.
        """
        rand_num = random.randrange(self.prefix_sum[-1])  # find a random
        rect_idx = bisect.bisect_right(self.prefix_sum, rand_num) - 1
        a, b, x, y = self.rects[rect_idx]
        delta_a, delta_b = divmod(rand_num - self.prefix_sum[rect_idx], y - b + 1)
        return [a + delta_a, b + delta_b]


def main():
    # Example 1: Output: [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
    command_list = ["Solution", "pick", "pick", "pick", "pick", "pick"]
    param_list = [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]

    # init instance
    # solution = Solution()
    rects = param_list[0][0]
    obj = Solution(rects)

    # run & time
    start = time.process_time()
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        # param = param_list[idx]
        if command == "pick":
            ans.append(obj.pick())
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
