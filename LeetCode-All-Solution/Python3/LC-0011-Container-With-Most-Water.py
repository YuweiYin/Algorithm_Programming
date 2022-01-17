#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0011-Container-With-Most-Water.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-17
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0011 - (Medium) - Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Description & Requirement:
    You are given an integer array height of length n. 
    There are n vertical lines drawn such that 
    the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, 
    such that the container contains the most water.

    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
        In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # exception case
        if not isinstance(height, list) or len(height) <= 1:
            return 0  # Error input type
        if len(height) == 2:
            return min(height[0], height[1])
        # main method: (two pointer, move from both ends of the list till meet each other)
        return self._maxArea(height)

    def _maxArea(self, height: List[int]) -> int:
        len_height = len(height)
        assert len_height > 2

        res = 0
        left_index = 0
        right_index = len_height - 1

        while left_index < right_index:
            cur_area = (right_index - left_index) * min(height[left_index], height[right_index])
            res = max(res, cur_area)
            # move the lower line to get larger area
            # because if move the higher line, the next area is still limited by the lower line
            if height[left_index] <= height[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return res


def main():
    # Example 1: Output: 49
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # Example 2: Output: 1
    # height = [1, 1]

    # Example 3: Output: 4
    # height = [1, 2, 4, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxArea(height)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
