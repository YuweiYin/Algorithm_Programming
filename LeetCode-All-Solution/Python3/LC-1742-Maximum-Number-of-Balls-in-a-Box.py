#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1742-Maximum-Number-of-Balls-in-a-Box.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-22
=================================================================="""

import sys
import time
# from typing import List
import collections
# import functools

"""
LeetCode - 1742 - (Easy) - Maximum Number of Balls in a Box
https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

Description & Requirement:
    You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive 
    (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

    Your job at this factory is to put each ball in the box with a number equal to the sum of digits of 
    the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and 
    the ball number 10 will be put in the box number 1 + 0 = 1.

    Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

Example 1:
    Input: lowLimit = 1, highLimit = 10
    Output: 2
    Explanation:
        Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
        Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
        Box 1 has the most number of balls with 2 balls.
Example 2:
    Input: lowLimit = 5, highLimit = 15
    Output: 2
    Explanation:
        Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
        Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
        Boxes 5 and 6 have the most number of balls with 2 balls in each.
Example 3:
    Input: lowLimit = 19, highLimit = 28
    Output: 2
    Explanation:
        Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
        Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
        Box 10 has the most number of balls with 2 balls.

Constraints:
    1 <= lowLimit <= highLimit <= 10^5
"""


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # exception case
        assert isinstance(lowLimit, int) and isinstance(highLimit, int) and 1 <= lowLimit <= highLimit
        # main method: (hash counter)
        return self._countBalls(lowLimit, highLimit)

    def _countBalls(self, lowLimit: int, highLimit: int) -> int:
        assert isinstance(lowLimit, int) and isinstance(highLimit, int) and 1 <= lowLimit <= highLimit

        count = collections.Counter(sum(map(int, str(i))) for i in range(lowLimit, highLimit + 1))

        return max(count.values())


def main():
    # Example 1: Output: 2
    # lowLimit = 1
    # highLimit = 10

    # Example 2: Output: 2
    # lowLimit = 5
    # highLimit = 15

    # Example 3: Output: 2
    lowLimit = 19
    highLimit = 28

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countBalls(lowLimit, highLimit)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
