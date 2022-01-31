#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0343-Integer-Break.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-31
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0343 - (Medium) - Integer Break
https://leetcode.com/problems/integer-break/

Description & Requirement:
    Given an integer n, break it into the sum of k positive integers, where k >= 2, 
    and maximize the product of those integers.

    Return the maximum product you can get.

Example 1:
    Input: n = 2
    Output: 1
    Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:
    Input: n = 10
    Output: 36
    Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Constraints:
    2 <= n <= 58
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if n <= 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        # main method: (1. Mathematics; 2. Dynamic Programming)
        #     Math idea: to get maximum product, apparently need to split n equally
        return self._integerBreak(n)

    def _integerBreak(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 84.39% of Python3 online submissions for Integer Break.
        Memory Usage: 13.9 MB, less than 98.81% of Python3 online submissions for Integer Break.
        """
        assert n >= 5

        res = 1  # n is split into 1, 1, ... 1, prod is 1^n = 1

        for k_fold in range(2, (n >> 1) + 1):  # k_fold is the number of split folds
            cur_split_num = n // k_fold
            cur_split_mod = n % k_fold
            cur_res = 1
            for _ in range(cur_split_mod):  # multiplication, get product (has mod residual)
                cur_res *= (cur_split_num + 1)
            for _ in range(k_fold - cur_split_mod):  # multiplication, get product (don't have mod residual)
                cur_res *= cur_split_num
            res = max(res, cur_res)

        return res


def main():
    # Example 1: Output: 1
    #     Explanation: 2 = 1 + 1, 1 × 1 = 1.
    # n = 2

    # Example 2: Output: 36
    #     Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
    n = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.integerBreak(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
