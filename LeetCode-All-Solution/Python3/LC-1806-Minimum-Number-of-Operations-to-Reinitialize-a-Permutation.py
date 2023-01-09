#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1806-Minimum-Number-of-Operations-to-Reinitialize-a-Permutation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-09
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1806 - (Medium) - Minimum Number of Operations to Reinitialize a Permutation
https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

Description & Requirement:
    You are given an even integer n. You initially have a permutation perm of size n where perm[i] == i (0-indexed).

    In one operation, you will create a new array arr, and for each i:
        If i % 2 == 0, then arr[i] = perm[i / 2].
        If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].

    You will then assign arr to perm.

    Return the minimum non-zero number of operations you need to perform on perm to 
    return the permutation to its initial value.

Example 1:
    Input: n = 2
    Output: 1
    Explanation: perm = [0,1] initially.
        After the 1st operation, perm = [0,1]
        So it takes only 1 operation.
Example 2:
    Input: n = 4
    Output: 2
    Explanation: perm = [0,1,2,3] initially.
        After the 1st operation, perm = [0,2,1,3]
        After the 2nd operation, perm = [0,1,2,3]
        So it takes only 2 operations.
Example 3:
    Input: n = 6
    Output: 4

Constraints:
    2 <= n <= 1000
    n is even.
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 2 and n & 0x01 == 0
        # main method: (mathematics OR simulate the process as the rule tells)
        return self._reinitializePermutation(n)

    def _reinitializePermutation(self, n: int) -> int:
        """
        Time: beats 100%; Space: beats 73.45%
        """
        assert isinstance(n, int) and n >= 2 and n & 0x01 == 0

        if n == 2:
            return 1

        res = 1
        pow2 = 2
        MOD = n - 1
        while pow2 != 1:
            pow2 = (pow2 << 1) % MOD
            res += 1

        return res


def main():
    # Example 1: Output: 1
    # n = 2

    # Example 2: Output: 2
    # n = 4

    # Example 3: Output: 4
    n = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reinitializePermutation(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
