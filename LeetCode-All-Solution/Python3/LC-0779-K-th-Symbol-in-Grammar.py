#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0779-K-th-Symbol-in-Grammar.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-20
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0779 - (Medium) - K-th Symbol in Grammar
https://leetcode.com/problems/k-th-symbol-in-grammar/

Description & Requirement:
    We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, 
    we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

        For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

    Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:
    Input: n = 1, k = 1
    Output: 0
    Explanation: row 1: 0
Example 2:
    Input: n = 2, k = 1
    Output: 0
    Explanation: 
        row 1: 0
        row 2: 01
Example 3:
    Input: n = 2, k = 2
    Output: 1
    Explanation: 
        row 1: 0
        row 2: 01

Constraints:
    1 <= n <= 30
    1 <= k <= 2^{n-1}
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and 1 <= k <= 1 << (n - 1)
        # main method: (find the pattern: 0 - 01 - 0110 - 01101001 => "01" to "0110" and "10" to "1001")
        return self._kthGrammar(n, k)

    def _kthGrammar(self, n: int, k: int) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and 1 <= k <= 1 << (n - 1)

        res = 0
        k -= 1
        while k > 0:
            k &= k - 1
            res ^= 1

        return res


def main():
    # Example 1: Output: 0
    # n = 1
    # k = 1

    # Example 2: Output: 0
    # n = 2
    # k = 1

    # Example 3: Output: 1
    n = 2
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kthGrammar(n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
