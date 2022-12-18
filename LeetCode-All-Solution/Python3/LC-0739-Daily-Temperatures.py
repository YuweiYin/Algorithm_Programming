#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0739-Daily-Temperatures.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0739 - (Medium) - Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Description & Requirement:
    Given an array of integers temperatures represents the daily temperatures, 
    return an array answer such that answer[i] is the number of days you have to wait after the i-th day 
    to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]

Constraints:
    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # exception case
        assert isinstance(temperatures, list) and len(temperatures) >= 1
        # main method: (monotonous stack)
        return self._dailyTemperatures(temperatures)

    def _dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        assert isinstance(temperatures, list) and len(temperatures) >= 1

        length = len(temperatures)
        res = [0 for _ in range(length)]
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res


def main():
    # Example 1: Output: [1,1,4,2,1,1,0,0]
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    # Example 2: Output: [1,1,1,0]
    # temperatures = [30, 40, 50, 60]

    # Example 3: Output: [1,1,0]
    # temperatures = [30, 60, 90]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.dailyTemperatures(temperatures)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
