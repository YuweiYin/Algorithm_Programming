#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0764-Largest-Plus-Sign.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0764 - (Medium) - Largest Plus Sign
https://leetcode.com/problems/largest-plus-sign/

Description & Requirement:
    You are given an integer n. You have an n x n binary grid grid with all values initially 1's 
    except for some indices given in the array mines. 
    The i-th element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

    Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

    An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 
    along with four arms of length k - 1 going up, down, left, and right, and made of 1's. 
    Note that there could be 0's or 1's beyond the arms of the plus sign, 
    only the relevant area of the plus sign is checked for 1's.

Example 1:
    Input: n = 5, mines = [[4,2]]
    Output: 2
    Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
Example 2:
    Input: n = 1, mines = [[0,0]]
    Output: 0
    Explanation: There is no plus sign, so return 0.

Constraints:
    1 <= n <= 500
    1 <= mines.length <= 5000
    0 <= xi, yi < n
    All the pairs (xi, yi) are unique.
"""


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(mines, list) and len(mines) >= 1
        # main method: (dynamic programming)
        return self._orderOfLargestPlusSign(n, mines)

    def _orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(mines, list) and len(mines) >= 1

        dp = [[n for _ in range(n)] for _ in range(n)]
        forbidden = set(map(tuple, mines))

        for r in range(n):
            # left
            count = 0
            for c in range(n):
                count = 0 if (r, c) in forbidden else count + 1
                dp[r][c] = min(dp[r][c], count)
            # right
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in forbidden else count + 1
                dp[r][c] = min(dp[r][c], count)

        for c in range(n):
            # up
            count = 0
            for r in range(n):
                count = 0 if (r, c) in forbidden else count + 1
                dp[r][c] = min(dp[r][c], count)
            # down
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in forbidden else count + 1
                dp[r][c] = min(dp[r][c], count)

        return max([max(row) for row in dp])


def main():
    # Example 1: Output: 2
    # n = 5
    # mines = [[4, 2]]

    # Example 2: Output: 0
    n = 1
    mines = [[0, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.orderOfLargestPlusSign(n, mines)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
