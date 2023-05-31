#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1130-Minimum-Cost-Tree-From-Leaf-Values.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-31
=================================================================="""

import sys
import time
from typing import List
# import collections
import functools

"""
LeetCode - 1130 - (Medium) - Minimum Cost Tree From Leaf Values
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

Description & Requirement:
    Given an array arr of positive integers, consider all binary trees such that:

        Each node has either 0 or 2 children;
        The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
        The value of each non-leaf node is equal to the product of the largest leaf value 
            in its left and right subtree, respectively.

    Among all possible binary trees considered, return the smallest possible sum of 
    the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

    A node is a leaf if and only if it has zero children.

Example 1:
    Input: arr = [6,2,4]
    Output: 32
    Explanation: There are two possible trees shown.
        The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
Example 2:
    Input: arr = [4,11]
    Output: 44

Constraints:
    2 <= arr.length <= 40
    1 <= arr[i] <= 15
    It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 2^31).
"""


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 2
        # main method: (dynamic programming)
        return self._mctFromLeafValues(arr)

    def _mctFromLeafValues(self, arr: List[int]) -> int:
        assert isinstance(arr, list) and len(arr) >= 2

        @functools.lru_cache(None)
        def __dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            return min(__dfs(i, k) + __dfs(k + 1, j) + dp[i][k] * dp[k + 1][j] for k in range(i, j))

        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = arr[i]
            for j in range(i + 1, n):
                dp[i][j] = max(dp[i][j - 1], arr[j])

        return __dfs(0, n - 1)


def main():
    # Example 1: Output: 32
    arr = [6, 2, 4]

    # Example 2: Output: 44
    # arr = [4, 11]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mctFromLeafValues(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
