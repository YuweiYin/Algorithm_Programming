#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-1709-Get-Kth-Magic-Number-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-28
=================================================================="""

import sys
import time
import heapq
# from typing import List
# import collections
# import functools

"""
LeetCode - INTERVIEW-1709 - (Medium) - Get Kth Magic Number
https://leetcode.cn/problems/get-kth-magic-number-lcci/

Description & Requirement:
    Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7. 
    Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors. 
    For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.

Example 1:
    Input: k = 5
    Output: 9
"""


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        # exception case
        assert isinstance(k, int)
        # main method: (heap)
        return self._getKthMagicNumber(k)

    def _getKthMagicNumber(self, k: int) -> int:
        assert isinstance(k, int)

        factors = {3, 5, 7}
        visited = {1}
        heap = [1]

        for _ in range(k - 1):
            cur_num = heapq.heappop(heap)
            for factor in factors:
                next_num = cur_num * factor
                if next_num not in visited:
                    visited.add(next_num)
                    heapq.heappush(heap, next_num)

        return heapq.heappop(heap)


def main():
    # Example 1: Output: 9
    k = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getKthMagicNumber(k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
