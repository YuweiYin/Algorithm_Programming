#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2600-K-Items-With-the-Maximum-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-05
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 2600 - (Easy) - K Items With the Maximum Sum
https://leetcode.com/problems/k-items-with-the-maximum-sum/

Description & Requirement:
    There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.

    You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.

    The bag initially contains:
        numOnes items with 1s written on them.
        numZeroes items with 0s written on them.
        numNegOnes items with -1s written on them.

    We want to pick exactly k items among the available items. 
    Return the maximum possible sum of numbers written on the items.

Example 1:
    Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
    Output: 2
    Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. 
        We take 2 items with 1 written on them and get a sum in a total of 2.
        It can be proven that 2 is the maximum possible sum.
Example 2:
    Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
    Output: 3
    Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. 
        We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3.
        It can be proven that 3 is the maximum possible sum.

Constraints:
    0 <= numOnes, numZeros, numNegOnes <= 50
    0 <= k <= numOnes + numZeros + numNegOnes
"""


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # exception case
        assert isinstance(numOnes, int) and numOnes >= 0
        assert isinstance(numZeros, int) and numZeros >= 0
        assert isinstance(numNegOnes, int) and numNegOnes >= 0
        assert isinstance(k, int) and 0 <= numOnes + numZeros + numNegOnes
        # main method: (greedy)
        return self._kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)

    def _kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        assert isinstance(numOnes, int) and numOnes >= 0
        assert isinstance(numZeros, int) and numZeros >= 0
        assert isinstance(numNegOnes, int) and numNegOnes >= 0
        assert isinstance(k, int) and 0 <= numOnes + numZeros + numNegOnes

        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - numOnes - numZeros)


def main():
    # Example 1: Output: 2
    # numOnes = 3
    # numZeros = 2
    # numNegOnes = 0
    # k = 2

    # Example 2: Output: 3
    numOnes = 3
    numZeros = 2
    numNegOnes = 0
    k = 4

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
