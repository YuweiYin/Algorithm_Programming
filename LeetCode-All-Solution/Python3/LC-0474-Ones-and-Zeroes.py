#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0474-Ones-and-Zeroes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-23
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0474 - (Medium) - Ones and Zeroes
https://leetcode.com/problems/ones-and-zeroes/

Description & Requirement:
    You are given an array of binary strings strs and two integers m and n.

    Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

    A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:
    Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
    Output: 4
    Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
        Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
        {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:
    Input: strs = ["10","0","1"], m = 1, n = 1
    Output: 2
    Explanation: The largest subset is {"0", "1"}, so the answer is 2.

Constraints:
    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] consists only of digits '0' and '1'.
    1 <= m, n <= 100
"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # exception case
        assert isinstance(strs, list) and len(strs) >= 1
        for string in strs:
            assert isinstance(string, str) and len(string) >= 1
        assert isinstance(m, int) and m >= 1 and isinstance(n, int) and n >= 1
        # main method: (2-backpack problem)
        return self._findMaxForm(strs, m, n)

    def _findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            # count the 0s and 1s in the current string
            cur_m, cur_n = 0, 0
            for ch in strs[i - 1]:
                if ch == "0":
                    cur_m += 1
                elif ch == "1":
                    cur_n += 1
            # consider the dp transition path (equation)
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]  # at least we can not use this string
                    if cur_m <= j and cur_n <= k:  # valid transition from the previous string
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - cur_m][k - cur_n] + 1)

        return dp[-1][-1][-1]


def main():
    # Example 1: Output: 4
    # strs = ["10", "0001", "111001", "1", "0"]
    # m = 5
    # n = 3

    # Example 2: Output: 2
    strs = ["10", "0", "1"]
    m = 1
    n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMaxForm(strs, m, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
