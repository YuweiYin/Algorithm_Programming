#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1051-Height-Checker.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-13
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1051 - (Easy) - Height Checker
https://leetcode.com/problems/height-checker/

Description & Requirement:
    A school is trying to take an annual photo of all the students. 
    The students are asked to stand in a single file line in non-decreasing order by height. 
    Let this ordering be represented by the integer array expected 
    where expected[i] is the expected height of the ith student in line.

    You are given an integer array heights representing the current order that the students are standing in. 
    Each heights[i] is the height of the ith student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].

Example 1:
    Input: heights = [1,1,4,2,1,3]
    Output: 3
    Explanation: 
        heights:  [1,1,4,2,1,3]
        expected: [1,1,1,2,3,4]
        Indices 2, 4, and 5 do not match.
Example 2:
    Input: heights = [5,1,2,3,4]
    Output: 5
    Explanation:
        heights:  [5,1,2,3,4]
        expected: [1,2,3,4,5]
        All indices do not match.
Example 3:
    Input: heights = [1,2,3,4,5]
    Output: 0
    Explanation:
        heights:  [1,2,3,4,5]
        expected: [1,2,3,4,5]
        All indices match.

Constraints:
    1 <= heights.length <= 100
    1 <= heights[i] <= 100
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # exception case
        assert isinstance(heights, list) and len(heights) >= 1
        # main method: (sort list and compare elements of the same index)
        return self._heightChecker(heights)

    def _heightChecker(self, heights: List[int]) -> int:
        assert isinstance(heights, list) and len(heights) >= 1

        target_heights = sorted(heights)
        res = 0
        for idx in range(len(heights)):
            if heights[idx] != target_heights[idx]:
                res += 1

        return res


def main():
    # Example 1: Output: 3
    heights = [1, 1, 4, 2, 1, 3]

    # Example 2: Output: 5
    # heights = [5, 1, 2, 3, 4]

    # Example 3: Output: 0
    # heights = [1, 2, 3, 4, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.heightChecker(heights)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
