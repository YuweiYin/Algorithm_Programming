#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0077-Combinations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-11
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0077 - (Medium) - Combinations
https://leetcode.com/problems/combinations/

Description & Requirement:
    Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
    You may return the answer in any order.

Example 1:
    Input: n = 4, k = 2
    Output:
        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]
Example 2:
    Input: n = 1, k = 1
    Output: [[1]]

Constraints:
    1 <= n <= 20
    1 <= k <= n
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # exception case
        if not isinstance(n, int) or n <= 0 or not isinstance(k, int) or k <= 0 or k > n:
            return []  # Error input type
        if n == 1:
            return [[1]]
        if k == 1:
            return [[num] for num in range(1, n + 1)]
        # main method: (dfs & backtrack)
        return self._combine(n, k)

    def _combine(self, n: int, k: int) -> List[List[int]]:
        res_combo = []  # stack

        def __dfs(cur_combo: List[int], cur_start: int):
            if len(cur_combo) == k:  # end of recursion
                res_combo.append(cur_combo[:])
                return

            for num in range(cur_start, n + 1):
                cur_combo.append(num)  # move on
                __dfs(cur_combo, num + 1)  # dfs
                cur_combo.pop()  # backtrack

        combo = []
        __dfs(combo, 1)

        return res_combo


def main():
    # Example 1: Output: [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
    # n = 4
    # k = 2

    # Example 2: Output: [[1]]
    # n = 1
    # k = 1

    # Example 3: Output:
    n = 20
    k = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.combine(n ,k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
