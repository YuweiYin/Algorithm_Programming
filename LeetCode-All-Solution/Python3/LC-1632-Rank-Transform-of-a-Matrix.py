#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1632-Rank-Transform-of-a-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-25
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1632 - (Hard) - Rank Transform of a Matrix
https://leetcode.com/problems/rank-transform-of-a-matrix/

Description & Requirement:
    Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

    The rank is an integer that represents how large an element is compared to other elements. 
        It is calculated using the following rules:
    The rank is an integer starting from 1.
        If two elements p and q are in the same row or column, then:
        If p < q then rank(p) < rank(q)
        If p == q then rank(p) == rank(q)
        If p > q then rank(p) > rank(q)
    The rank should be as small as possible.

    The test cases are generated so that answer is unique under the given rules.

Example 1:
    Input: matrix = [[1,2],[3,4]]
    Output: [[1,2],[2,3]]
    Explanation:
        The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
        The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
        The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
        The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], 
            and both matrix[0][1] and matrix[1][0] are rank 2.
Example 2:
    Input: matrix = [[7,7],[7,7]]
    Output: [[1,1],[1,1]]
Example 3:
    Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
    Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 500
    -109 <= matrix[row][col] <= 10^9
"""


class UnionFind:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.root = [[[i, j] for j in range(n)] for i in range(m)]
        self.size = [[1] * n for _ in range(m)]

    def find(self, i, j):
        ri, rj = self.root[i][j]
        if [ri, rj] == [i, j]:
            return [i, j]
        self.root[i][j] = self.find(ri, rj)
        return self.root[i][j]

    def union(self, i1, j1, i2, j2):
        ri1, rj1 = self.find(i1, j1)
        ri2, rj2 = self.find(i2, j2)
        if [ri1, rj1] != [ri2, rj2]:
            if self.size[ri1][rj1] >= self.size[ri2][rj2]:
                self.root[ri2][rj2] = [ri1, rj1]
                self.size[ri1][rj1] += self.size[ri2][rj2]
            else:
                self.root[ri1][rj1] = [ri2, rj2]
                self.size[ri2][rj2] += self.size[ri1][rj1]


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(matrix, list) and len(matrix) >= 1
        n = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == n
        # main method: (union find set)
        return self._matrixRankTransform(matrix)

    def _matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        assert isinstance(matrix, list) and len(matrix) >= 1
        m, n = len(matrix), len(matrix[0])

        uf = UnionFind(m, n)
        for i, row in enumerate(matrix):
            num2index = collections.defaultdict(list)
            for j, num in enumerate(row):
                num2index[num].append([i, j])
            for indices in num2index.values():
                i1, j1 = indices[0]
                for k in range(1, len(indices)):
                    i2, j2 = indices[k]
                    uf.union(i1, j1, i2, j2)

        for j in range(n):
            num2index = collections.defaultdict(list)
            for i in range(m):
                num2index[matrix[i][j]].append([i, j])
            for indices in num2index.values():
                i1, j1 = indices[0]
                for k in range(1, len(indices)):
                    i2, j2 = indices[k]
                    uf.union(i1, j1, i2, j2)

        degree = collections.Counter()
        adj = collections.defaultdict(list)
        for i, row in enumerate(matrix):
            num2index = {}
            for j, num in enumerate(row):
                num2index[num] = (i, j)
            num2index_keys = sorted(num2index.keys())
            for k in range(1, len(num2index_keys)):
                i1, j1 = num2index[num2index_keys[k - 1]]
                i2, j2 = num2index[num2index_keys[k]]
                ri1, rj1 = uf.find(i1, j1)
                ri2, rj2 = uf.find(i2, j2)
                degree[(ri2, rj2)] += 1
                adj[(ri1, rj1)].append([ri2, rj2])

        for j in range(n):
            num2index = {}
            for i in range(m):
                num = matrix[i][j]
                num2index[num] = (i, j)
            num2index_keys = sorted(num2index.keys())
            for k in range(1, len(num2index_keys)):
                i1, j1 = num2index[num2index_keys[k - 1]]
                i2, j2 = num2index[num2index_keys[k]]
                ri1, rj1 = uf.find(i1, j1)
                ri2, rj2 = uf.find(i2, j2)
                degree[(ri2, rj2)] += 1
                adj[(ri1, rj1)].append([ri2, rj2])

        root_set = set()
        ranks = {}
        for i in range(m):
            for j in range(n):
                ri, rj = uf.find(i, j)
                root_set.add((ri, rj))
                ranks[(ri, rj)] = 1

        queue = collections.deque([[i, j] for i, j in root_set if degree[(i, j)] == 0])
        while len(queue) > 0:
            i, j = queue.popleft()
            for ui, uj in adj[(i, j)]:
                degree[(ui, uj)] -= 1
                if degree[(ui, uj)] == 0:
                    queue.append([ui, uj])
                ranks[(ui, uj)] = max(ranks[(ui, uj)], ranks[(i, j)] + 1)

        res = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ri, rj = uf.find(i, j)
                res[i][j] = ranks[(ri, rj)]

        return res


def main():
    # Example 1: Output: [[1,2],[2,3]]
    # matrix = [[1, 2], [3, 4]]

    # Example 2: Output: [[1,1],[1,1]]
    # matrix = [[7, 7], [7, 7]]

    # Example 3: Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
    matrix = [
        [20, -21, 14],
        [-19, 4, 19],
        [22, -47, 24],
        [-19, 4, 19]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.matrixRankTransform(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
