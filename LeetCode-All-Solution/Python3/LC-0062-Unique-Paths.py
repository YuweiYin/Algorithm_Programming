#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0062-Unique-Paths.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-26
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0062 - (Medium) - Unique Paths
https://leetcode.com/problems/unique-paths/

Description & Requirement:
    There is a robot on an m x n grid. 
    The robot is initially located at the top-left corner (i.e., grid[0][0]). 
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
    The robot can only move either down or right at any point in time.

    Given the two integers m and n, 
    return the number of possible unique paths that the robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
    Input: m = 3, n = 7
    Output: 28
Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down

Constraints:
    1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # exception case
        if not isinstance(m, int) or m <= 0 or not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if m == 1 or n == 1:
            return 1  # only one way: go straight right or go straight down
        # main method: (Mathematics - Combinatorics)
        #     idea: each step, either m-- or n--, till m == 1 and n == 1
        #     so there are m-1 steps for downward move, and n-1 steps for rightward move
        #     assume m >= n, the number of all combinations is select n-1 positions from m+n-2 slots
        #     i.e., C_{m+n-2}^{n-1}
        return self._uniquePaths(m, n)

    def _uniquePaths(self, m: int, n: int) -> int:
        assert isinstance(m, int) and m > 1 and isinstance(n, int) and n > 1

        def __combination_number(x: int, y: int) -> int:
            if x < y:  # swap, guarantee that x >= y
                x, y = y, x
            if y == 0 or y == x:
                return 1
            if y == 1 or y == x - 1:
                return x
            combo = float(1.0)

            x_nums = [i for i in range(x - y + 1, x + 1)]  # x-y+1, x-y+2, ..., x
            y_nums = [i for i in range(1, y + 1)]  # 1, 2, ..., y
            assert len(x_nums) == len(y_nums) == y
            cur_index = 0
            while cur_index < y:
                combo *= x_nums[cur_index] / y_nums[cur_index]  # more likely to overflow if Prod all x_num in x_nums
                cur_index += 1

            return int(round(combo, ndigits=0))

        return __combination_number(m + n - 2, n - 1) if m >= n else __combination_number(m + n - 2, m - 1)


def main():
    # Example 1: Output: 28
    # m = 3
    # n = 7

    # Example 2: Output: 3
    # m = 3
    # n = 2

    # Example 3: Output: 48620
    m = 10
    n = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.uniquePaths(m, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
