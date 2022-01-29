#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0084-Largest-Rectangle-in-Histogram.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-29
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0084 - (Hard) - Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Description & Requirement:
    Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
    return the area of the largest rectangle in the histogram.

Example 1:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The above is a histogram where width of each bar is 1.
        The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
    Input: heights = [2,4]
    Output: 4

Constraints:
    1 <= heights.length <= 10^5
    0 <= heights[i] <= 10^4
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # exception case
        if not isinstance(heights, list) or len(heights) <= 0:
            return 0  # Error input type
        if len(heights) == 1:
            return heights[0]
        if len(heights) == 2:
            return max(2 * min(heights), max(heights))
        # main method: (Monotonous Stack)
        #     idea: if the new height is larger, keep pushing into stack; otherwise, pop stack until new h > stack top
        #     e.g., heights = [1, 3, 4, 5, 2, 7]
        #     push 1, push 3, push 4, push 5, and encounter 2, now consider 3, 4, 5 in ascending order
        #         5 itself can only form a rectangular with height == 5 and width == 1, so area = 5
        #         4 can cooperate with 5 to from a rectangular with height == 4 and width == 2, so area = 8
        #         3 can cooperate with 4 and 5 to form a rectangular with height == 3 and width == 3, so area = 9,
        #     so pop 5, 4, 3 respectively, and push 2. now, the stack has 1 and 2, keep pushing 7
        #     at last, no more height value left, deal with all elements in stack, i.e., 1, 2, 7
        #     the same process, 7 can form 7 * 1 rectangular and get area 7
        #     2 can form 2 * 2 rectangular and get area 4 (width == 2 is the dist between item 2 and the right border)
        #     1 can form 1 * 6 rectangular and get area 6 (width == 6 is the dist between item 1 and the right border)
        # other idea: Divide & Conquer + Segment Tree  (Time: O(n log n), Space O(n))
        #     step 1: construct segment tree beforehand O(n log n).
        #         each leaf denotes an interval. the leaf value is the lowest height in this interval
        #     step 2: divide & conquer, init interval is the whole height array, cut in the mid each time
        #         for each interval, use segment tree to search the lowest height and calculate the max possible area
        # if not use segment tree to search the min height in the given interval, then D&C alg will cost O(n^2) Time
        return self._largestRectangleArea(heights)  # Time: O(n);  Space: O(n)

    def _largestRectangleArea(self, heights: List[int]) -> int:
        len_h = len(heights)
        assert len_h >= 3

        res = 0  # max area

        # stack list store the index in heights array
        stack = [-1]  # use -1 as the stack bottom, -1 must be the smallest index & number coz 0 <= heights[i] <= 10^4

        # keep the numbers in stack is in ascending order: if a newly coming num >= stack top, then push it
        # otherwise, pop until new stack top is less than the newly coming num
        for idx, num in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= num:
                # pop until num > stack_top
                top_index = stack.pop()
                cur_height = heights[top_index]  # the pop height is the height of the current rectangular

                # the width of the current rectangular is the index distance between idx and top_index (new top)
                # the new stack top stack[-1] is a height that less than the newly popped item (with cur_height)
                # between the new stack top and the newly popped item, can be a gap, where those items have been dealt
                # those items must larger than the new stack top and the newly popped item.
                # the left most is stack bottom -1, len_h - (-1) - 1 == len_h, so the process remain correct
                cur_width = idx - stack[-1] - 1

                # calculate the area of the current rectangular & update the max value
                res = max(res, cur_height * cur_width)
            # now, num > stack_top, push num and continue the process
            stack.append(idx)

        # at last, stack may not be empty, so deal with the rest of them one by one
        idx = len_h
        while stack[-1] != -1:
            top_index = stack.pop()
            cur_height = heights[top_index]
            # now, width is the index dist between the right border (idx == len_h) and the new stack top
            cur_width = idx - stack[-1] - 1
            res = max(res, cur_height * cur_width)

        return res


def main():
    # Example 1: Output: 10
    #     Explanation: The above is a histogram where width of each bar is 1.
    #         The largest rectangle is shown in the red area, which has an area = 10 units.
    heights = [2, 1, 5, 6, 2, 3]

    # Example 2: Output: 4
    # heights = [2, 4]

    # Example 3: Output: 3
    # heights = [2, 1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestRectangleArea(heights)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
