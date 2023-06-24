#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0956-Tallest-Billboard.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-24
=================================================================="""

import sys
import time
from typing import List
# import collections
import functools
# import itertools

"""
LeetCode - 0956 - (Hard) - Tallest Billboard
https://leetcode.com/problems/tallest-billboard/

Description & Requirement:
    You are installing a billboard and want it to have the largest height. 
    The billboard will have two steel supports, one on each side. 
    Each steel support must be an equal height.

    You are given a collection of rods that can be welded together. 
    For example, if you have rods of lengths 1, 2, and 3, 
    you can weld them together to make a support of length 6.

    Return the largest possible height of your billboard installation. 
    If you cannot support the billboard, return 0.

Example 1:
    Input: rods = [1,2,3,6]
    Output: 6
    Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:
    Input: rods = [1,2,3,4,5,6]
    Output: 10
    Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:
    Input: rods = [1,2]
    Output: 0
    Explanation: The billboard cannot be supported, so we return 0.

Constraints:
    1 <= rods.length <= 20
    1 <= rods[i] <= 1000
    sum(rods[i]) <= 5000
"""


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # exception case
        assert isinstance(rods, list) and len(rods) >= 1
        # main method: (dynamic programming)
        return self._tallestBillboard(rods)

    def _tallestBillboard(self, rods: List[int]) -> int:
        assert isinstance(rods, list) and len(rods) >= 1

        @functools.lru_cache(maxsize=None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else -int(1e9+7)
            return max(dp(i + 1, s),
                       dp(i + 1, s - rods[i]),
                       dp(i + 1, s + rods[i]) + rods[i])

        return dp(0, 0)


def main():
    # Example 1: Output: 6
    rods = [1, 2, 3, 6]

    # Example 2: Output: 10
    # rods = [1, 2, 3, 4, 5, 6]

    # Example 3: Output: 0
    # rods = [1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.tallestBillboard(rods)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
