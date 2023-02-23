#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1238-Circular-Permutation-in-Binary-Representation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-23
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1238 - (Medium) - Circular Permutation in Binary Representation
https://leetcode.com/problems/circular-permutation-in-binary-representation/

Description & Requirement:
    Given 2 integers n and start. Your task is return any permutation p of (0, 1, 2, .., 2^n - 1) such that:
        p[0] = start
        p[i] and p[i+1] differ by only one bit in their binary representation.
        p[0] and p[2^n -1] must also differ by only one bit in their binary representation.

Example 1:
    Input: n = 2, start = 3
    Output: [3,2,0,1]
    Explanation: The binary representation of the permutation is (11,10,00,01). 
        All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
Example 2:
    Input: n = 3, start = 2
    Output: [2,6,7,5,4,0,1,3]
    Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).

Constraints:
    1 <= n <= 16
    0 <= start < 2^n
"""


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(start, int) and start >= 0
        # main method: (xor)
        # similar to Question 89. Gray Code: https://leetcode.com/problems/gray-code/
        return self._circularPermutation(n, start)

    def _circularPermutation(self, n: int, start: int) -> List[int]:
        assert isinstance(n, int) and n >= 1
        assert isinstance(start, int) and start >= 0

        res = [start]
        for i in range(1, n + 1):
            for j in range(len(res) - 1, -1, -1):
                res.append(((res[j] ^ start) | (1 << (i - 1))) ^ start)

        # # Method 2
        # res = [0] * (1 << n)
        # for i in range(1 << n):
        #     res[i] = (i >> 1) ^ i ^ start

        return res


def main():
    # Example 1: Output: [3,2,0,1]
    # n = 2
    # start = 3

    # Example 2: Output: [2,6,7,5,4,0,1,3]
    n = 3
    start = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.circularPermutation(n, start)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
