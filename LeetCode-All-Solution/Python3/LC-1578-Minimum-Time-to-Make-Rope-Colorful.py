#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1578-Minimum-Time-to-Make-Rope-Colorful.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1578 - (Medium) - Minimum Time to Make Rope Colorful
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

Description & Requirement:
    Alice has n balloons arranged on a rope. You are given a 0-indexed string colors 
    where colors[i] is the color of the ith balloon.

    Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, 
    so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. 
    You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) 
    that Bob needs to remove the ith balloon from the rope.

    Return the minimum time Bob needs to make the rope colorful.

Example 1:
    Input: colors = "abaac", neededTime = [1,2,3,4,5]
    Output: 3
    Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
        Bob can remove the blue balloon at index 2. This takes 3 seconds.
        There are no longer two consecutive balloons of the same color. Total time = 3.
Example 2:
    Input: colors = "abc", neededTime = [1,2,3]
    Output: 0
    Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
Example 3:
    Input: colors = "aabaa", neededTime = [1,2,3,4,1]
    Output: 2
    Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
        There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

Constraints:
    n == colors.length == neededTime.length
    1 <= n <= 10^5
    1 <= neededTime[i] <= 10^4
    colors contains only lowercase English letters.
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # exception case
        assert isinstance(colors, str) and isinstance(neededTime, list) and len(colors) == len(neededTime) >= 1
        for t in neededTime:
            assert isinstance(t, int) and t >= 1
        # main method: (greedily remove the cheapest balloons amony the consecutive ones that have the same color)
        return self._minCost(colors, neededTime)

    def _minCost(self, colors: str, neededTime: List[int]) -> int:
        assert isinstance(colors, str) and isinstance(neededTime, list) and len(colors) == len(neededTime) >= 1

        res = 0
        n = len(colors)
        idx = 0

        while idx < n:
            cur_c = colors[idx]
            max_time = 0
            sum_time = 0

            while idx < n and colors[idx] == cur_c:
                max_time = max(max_time, neededTime[idx])
                sum_time += neededTime[idx]
                idx += 1

            res += sum_time - max_time

        return res


def main():
    # Example 1: Output: 3
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]

    # Example 2: Output: 0
    # colors = "abc"
    # neededTime = [1, 2, 3]

    # Example 3: Output: 2
    # colors = "aabaa"
    # neededTime = [1, 2, 3, 4, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCost(colors, neededTime)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
