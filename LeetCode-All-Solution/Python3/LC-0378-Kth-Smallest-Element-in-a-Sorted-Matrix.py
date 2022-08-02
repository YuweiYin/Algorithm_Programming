#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0378-Kth-Smallest-Element-in-a-Sorted-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-02
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0378 - (Medium) - Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Description & Requirement:
    Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
    return the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    You must find a solution with a memory complexity better than O(n2).

Example 1:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:
    Input: matrix = [[-5]], k = 1
    Output: -5

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -10^9 <= matrix[i][j] <= 10^9
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n^2

Follow up:
    Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
    Could you solve the problem in O(n) time complexity? 
        The solution may be too advanced for an interview but you may find reading this paper fun.
        http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(matrix, list) and len(matrix) >= 1
        n = len(matrix)
        for row in matrix:
            assert isinstance(row, list) and len(row) == n
        assert isinstance(k, int) and 1 <= k <= n * n
        # main method: (binary search)
        return self._kthSmallest(matrix, k)

    def _kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Runtime: 174 ms, faster than 98.16% of Python3 submissions for Kth Smallest Element in a Sorted Matrix.
        Memory Usage: 18.8 MB, less than 38.85% of Python3 submissions for Kth Smallest Element in a Sorted Matrix.
        """
        assert isinstance(matrix, list) and len(matrix) >= 1
        n = len(matrix)
        assert isinstance(k, int) and 1 <= k <= n * n

        def check(cur_mid: int) -> bool:
            row, col = n - 1, 0  # start position
            num = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= cur_mid:
                    num += row + 1  # accumulate the number of items in this column that are smaller than mid
                    col += 1
                else:
                    row -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]  # the smallest number and the largest number
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 13
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8

    # Example 2: Output: -5
    # matrix = [[-5]]
    # k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kthSmallest(matrix, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
