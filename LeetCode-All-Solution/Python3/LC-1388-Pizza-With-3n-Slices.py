#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1388-Pizza-With-3n-Slices.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1388 - (Hard) Pizza With 3n Slices
https://leetcode.com/problems/pizza-with-3n-slices/

Description & Requirement:
    There is a pizza with 3n slices of varying size, 
    you and your friends will take slices of pizza as follows:
        You will pick any pizza slice.
        Your friend Alice will pick the next slice in the anti-clockwise direction of your pick.
        Your friend Bob will pick the next slice in the clockwise direction of your pick.
        Repeat until there are no more slices of pizzas.

    Given an integer array slices that represent the sizes of the pizza slices in a clockwise direction, 
    return the maximum possible sum of slice sizes that you can pick.

Example 1:
    Input: slices = [1,2,3,4,5,6]
    Output: 10
    Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. 
        Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. 
        Total = 4 + 6.
Example 2:
    Input: slices = [8,9,8,6,1,1]
    Output: 16
    Explanation: Pick pizza slice of size 8 in each turn. 
        If you pick slice with size 9 your partners will pick slices of size 8.

Constraints:
    3 * n == slices.length
    1 <= slices.length <= 500
    1 <= slices[i] <= 1000
"""


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # exception case
        assert isinstance(slices, list) and len(slices) >= 1 and len(slices) % 3 == 0
        # main method: (dynamic programming)
        return self._maxSizeSlices(slices)

    def _maxSizeSlices(self, slices: List[int]) -> int:
        assert isinstance(slices, list) and len(slices) >= 1 and len(slices) % 3 == 0

        def __dp(s: List[int]):
            m, n = len(s), (len(s) + 1) // 3
            dp = [[-int(1e9+7) for _ in range(n + 1)] for _ in range(m)]
            dp[0][0], dp[0][1] = 0, s[0]
            dp[1][0], dp[1][1] = 0, max(s[0], s[1])

            for i in range(2, m, 1):
                dp[i][0] = 0
                for j in range(1, n + 1, 1):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + s[i])

            return dp[-1][-1]

        s_1 = slices[1:]
        s_2 = slices[0: -1]
        res_1 = __dp(s_1)
        res_2 = __dp(s_2)

        return max(res_1, res_2)


def main():
    # Example 1: Output: 10
    slices = [1, 2, 3, 4, 5, 6]

    # Example 2: Output: 16
    # slices = [8, 9, 8, 6, 1, 1]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxSizeSlices(slices)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
