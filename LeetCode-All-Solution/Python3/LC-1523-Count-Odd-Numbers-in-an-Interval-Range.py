#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1523-Count-Odd-Numbers-in-an-Interval-Range.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-13
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1523 - (Easy) - Count Odd Numbers in an Interval Range
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

Description & Requirement:
    Given two non-negative integers low and high. 
    Return the count of odd numbers between low and high (inclusive).

Example 1:
    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:
    Input: low = 8, high = 10
    Output: 1
    Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
    0 <= low <= high <= 10^9
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # exception case
        assert isinstance(low, int) and isinstance(high, int) and 0 <= low <= high
        # main method: (prefix)
        return self._countOdds(low, high)

    def _countOdds(self, low: int, high: int) -> int:
        assert isinstance(low, int) and isinstance(high, int) and 0 <= low <= high

        return ((high + 1) >> 1) - (low >> 1)


def main():
    # Example 1: Output: 3
    low = 3
    high = 7

    # Example 2: Output: 1
    # low = 8
    # high = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countOdds(low, high)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
