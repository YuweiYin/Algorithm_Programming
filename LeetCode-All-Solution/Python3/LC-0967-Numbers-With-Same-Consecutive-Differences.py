#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0967-Numbers-With-Same-Consecutive-Differences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0967 - (Medium) - Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Description & Requirement:
    Return all non-negative integers of length n such that 
    the absolute difference between every two consecutive digits is k.

    Note that every number in the answer must not have leading zeros. 
    For example, 01 has one leading zero and is invalid.

    You may return the answer in any order.

Example 1:
    Input: n = 3, k = 7
    Output: [181,292,707,818,929]
    Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:
    Input: n = 2, k = 1
    Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Constraints:
    2 <= n <= 9
    0 <= k <= 9
"""


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(k, int) and k >= 0
        # main method: (enumerate all possibilities)
        return self._numsSameConsecDiff(n, k)

    def _numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        assert isinstance(n, int) and n >= 2
        assert isinstance(k, int) and k >= 0

        res = {x for x in range(1, 10)}
        for _ in range(n - 1):
            ans = set()
            for num in res:
                digit = num % 10
                if digit - k >= 0:
                    ans.add(10 * num + digit - k)
                if digit + k <= 9:
                    ans.add(10 * num + digit + k)
            res = ans

        if n == 1:
            res.add(0)

        return list(res)


def main():
    # Example 1: Output: [181,292,707,818,929]
    n = 3
    k = 7

    # Example 2: Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    # n = 2
    # k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numsSameConsecDiff(n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
