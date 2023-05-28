#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1439-Find-the-Kth-Smallest-Sum-of-a-Matrix-With-Sorted-Rows.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-28
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 1439 - (Hard) - Find the Kth Smallest Sum of a Matrix With Sorted Rows
https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

Description & Requirement:
    You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.

    You are allowed to choose exactly one element from each row to form an array.

    Return the kth smallest array sum among all possible arrays.

Example 1:
    Input: mat = [[1,3,11],[2,4,6]], k = 5
    Output: 7
    Explanation: Choosing one element from each row, the first k smallest sum are:
        [1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
Example 2:
    Input: mat = [[1,3,11],[2,4,6]], k = 9
    Output: 17
Example 3:
    Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
    Output: 9
    Explanation: Choosing one element from each row, the first k smallest sum are:
        [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  

Constraints:
    m == mat.length
    n == mat.length[i]
    1 <= m, n <= 40
    1 <= mat[i][j] <= 5000
    1 <= k <= min(200, nm)
    mat[i] is a non-decreasing array.
"""


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat[0]) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (heap)
        return self._kthSmallest(mat, k)

    def _kthSmallest(self, mat: List[List[int]], k: int) -> int:
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat[0]) >= 1
        assert isinstance(k, int) and k >= 1

        def __merge(f: List[int], g: List[int], cur_k: int) -> List[int]:
            if len(g) > len(f):
                return __merge(g, f, cur_k)

            heap = [(f[0] + g[i], 0, i) for i in range(len(g))]
            heapq.heapify(heap)

            ans = []
            while cur_k and heap:
                entry = heapq.heappop(heap)
                ans.append(entry[0])
                if entry[1] + 1 < len(f):
                    heapq.heappush(heap, (f[entry[1] + 1] + g[entry[2]], entry[1] + 1, entry[2]))
                cur_k -= 1

            return ans

        prev = mat[0]
        for i in range(1, len(mat)):
            prev = __merge(prev, mat[i], k)

        return prev[k - 1]


def main():
    # Example 1: Output: 7
    # mat = [[1, 3, 11], [2, 4, 6]]
    # k = 5

    # Example 2: Output: 17
    # mat = [[1, 3, 11], [2, 4, 6]]
    # k = 9

    # Example 3: Output: 9
    mat = [[1, 10, 10], [1, 4, 5], [2, 3, 6]]
    k = 7

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kthSmallest(mat, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
