#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0096-Unique-Binary-Search-Trees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-14
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 0096 - (Medium) - Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/

Description & Requirement:
    Given an integer n, return the number of structurally unique BST's (binary search trees) 
    which has exactly n nodes of unique values from 1 to n.

Example 1:
    Input: n = 3
    Output: 5
Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n > 0
        # main method: (divide & conquer)
        #     divide: for the current [i, i+1, ..., j-1, j], consider each number as the root node of a subtree
        #         e.g., [1, 2, 3, 4, 5, 6], choose 4, then its left subtree is [1, 2, 3], right subtree is [5, 6]
        #     optimize: dynamic programming
        # return self._numTreesDC(n)
        return self._numTreesDP(n)

    def _numTreesDC(self, n: int) -> int:

        def __dfs(left_num: int, right_num: int) -> int:
            if left_num > right_num:  # no numbers
                return 0
            if left_num == right_num:  # 1 number
                return 1
            if left_num + 1 == right_num:  # 2 numbers
                # either left_num is root and right_num is the right subtree
                # or right_num is root and left_num is the left subtree
                return 2
            ans = 0
            for root_num in range(left_num + 1, right_num):  # choose each middle number to be the root node
                # number of he left combination * number of the right combination
                ans += __dfs(left_num, root_num - 1) * __dfs(root_num + 1, right_num)
            ans += __dfs(left_num + 1,  right_num)  # choose left_num to be the root node
            ans += __dfs(left_num, right_num - 1)  # choose right_num to be the root node
            return ans

        res = __dfs(1, n)
        return res

    def _numTreesDP(self, n: int) -> int:
        """
        Runtime: 28 ms, faster than 91.32% of Python3 online submissions for Unique Binary Search Trees.
        Memory Usage: 14 MB, less than 75.83% of Python3 online submissions for Unique Binary Search Trees.
        """
        dp = [0 for _ in range(n + 1)]  # dp[i] is the number of combination when the subtree has i nodes
        dp[0], dp[1] = 1, 1  # set dp[0] == 1, and any number multiply 1 get itself

        for subtree_size in range(2, n + 1):  # subtree size = 2, 3, ..., n
            # consider all numbers( 1, 2, ..., subtree_size) as the root num
            for root_num in range(1, subtree_size + 1):
                # accumulate: number of he left combination * number of the right combination
                # the current left subtree size is (root_num - 1)
                # the current right subtree size is (subtree_size - root_num)
                dp[subtree_size] += dp[root_num - 1] * dp[subtree_size - root_num]

        return dp[n]


def main():
    # Example 1: Output: 5
    # n = 3

    # Example 2: Output: 1
    # n = 1

    # Example 3: Output: 16796
    # n = 10

    # Example 4: Output: 9694845
    # n = 15

    # Example 5: Output: 1767263190
    n = 19

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numTrees(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
