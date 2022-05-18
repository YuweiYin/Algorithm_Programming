#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0668-Kth-Smallest-Number-in-Multiplication-Table.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-18
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0668 - (Hard) - Kth Smallest Number in Multiplication Table
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

Description & Requirement:
    Nearly everyone has used the [Multiplication Table](https://en.wikipedia.org/wiki/Multiplication_table). 
    The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

    Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example 1:
    Input: m = 3, n = 3, k = 5
    Output: 3
    Explanation: The 5th smallest number is 3.
Example 2:
    Input: m = 2, n = 3, k = 6
    Output: 6
    Explanation: The 6th smallest number is 6.

Constraints:
    1 <= m, n <= 3 * 10^4
    1 <= k <= m * n
"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # exception case
        assert isinstance(m, int) and m >= 1
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and 1 <= k <= m * n
        # main method: (binary search)
        return self._findKthNumber(m, n, k)  # Time: O(n); Space: O(1)

    def _findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        Runtime: 887 ms, faster than 88.62% of Python3 online submissions for Kth Smallest Number in M Table.
        Memory Usage: 14 MB, less than 31.98% of Python3 online submissions for Kth Smallest Number in M Table.
        """
        assert isinstance(m, int) and isinstance(n, int) and isinstance(k, int)

        left, right = 1, m * n
        while left < right:
            mid = (left + right) >> 1
            order = int(mid / n) * n  # the order of mid number in the table
            for i in range(int(mid / n) + 1, m + 1):
                order += int(mid / i)
            if order >= k:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 3
    # m = 3
    # n = 3
    # k = 5

    # Example 2: Output: 6
    m = 2
    n = 3
    k = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findKthNumber(m, n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
