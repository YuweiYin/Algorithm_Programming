#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1584-Min-Cost-to-Connect-All-Points.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-26
=================================================================="""

import sys
import time
from typing import List, Tuple
import bisect
# import functools

"""
LeetCode - 1584 - (Medium) - Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/

Description & Requirement:
    You are given an array points representing integer coordinates of some points on a 2D-plane,
    where points[i] = [xi, yi].

    The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: 
    |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

    Return the minimum cost to make all points connected. 
    All points are connected if there is exactly one simple path between any two points.

Example 1:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
    Explanation:
        We can connect the points as shown above to get the minimum cost of 20.
        Notice that there is a unique path between every pair of points.
Example 2:
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18

Constraints:
    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    All pairs (xi, yi) are distinct.
"""


class UnionFindSet:
    def __init__(self, n):
        self.n = n  # the number of initial sets
        self.rank = [1 for _ in range(n)]  # initially, each set has only 1 element with rank 1 (rank: set length)
        self.disjoint_set = list(range(n))  # if d_s[i] == d_s[j], then element i and j are in the same set

    def find_set(self, x: int) -> int:
        if self.disjoint_set[x] == x:  # x is the root element of a set, just return it
            return x
        self.disjoint_set[x] = self.find_set(self.disjoint_set[x])  # recursively merge links to the root of the set
        return self.disjoint_set[x]

    def union_set(self, x: int, y: int) -> bool:
        set_x, set_y = self.find_set(x), self.find_set(y)  # find the set roots of element x and y separately
        if set_x == set_y:  # no need to union
            return False

        if self.rank[set_x] < self.rank[set_y]:  # let set_x be the larger set (with larger rank)
            set_x, set_y = set_y, set_x

        self.rank[set_x] += self.rank[set_y]
        self.disjoint_set[set_y] = set_x
        return True


class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n  # the number of tree nodes
        self.bit_tree = [float("inf") for _ in range(n)]
        self.identity = [-1 for _ in range(n)]

    def update(self, idx: int, val: int, identity: int):
        while idx > 0:
            if self.bit_tree[idx] > val:
                self.bit_tree[idx] = val
                self.identity[idx] = identity
            idx -= idx & (-idx)  # remove the lowest bit

    def query(self, idx: int) -> int:
        min_id = -1
        min_val = float("inf")
        while idx < self.n:
            if min_val > self.bit_tree[idx]:
                min_val = self.bit_tree[idx]
                min_id = self.identity[idx]
            idx += idx & (-idx)  # add the lowest bit
        return min_id


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # exception case
        assert isinstance(points, list) and len(points) >= 1
        for point in points:
            assert isinstance(point, list) and len(point) == 2
        # main method: (MST & Union Find) TODO
        return self._minCostConnectPoints(points)

    def _minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Runtime: 329 ms, faster than 100.00% of Python3 online submissions for Min Cost to Connect All Points.
        Memory Usage: 15.2 MB, less than 93.60% of Python3 online submissions for Min Cost to Connect All Points.
        """
        assert isinstance(points, list) and len(points) >= 1
        n = len(points)
        edges = []

        def build(pos: List[Tuple[int, int, int]]):
            pos.sort()
            diff_list = [y - x for (x, y, _) in pos]
            diff_sort = sorted(set(diff_list))

            bit = BinaryIndexedTree(len(diff_sort) + 1)
            for i in range(n - 1, -1, -1):
                pos_sect = bisect.bisect(diff_sort, diff_list[i])
                j = bit.query(pos_sect)
                if j != -1:
                    distance = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
                    edges.append((distance, pos[i][2], pos[j][2]))
                bit.update(pos_sect, pos[i][0] + pos[i][1], i)

        build([(x, y, i) for i, (x, y) in enumerate(points)])
        build([(y, x, i) for i, (x, y) in enumerate(points)])
        build([(-y, x, i) for i, (x, y) in enumerate(points)])
        build([(x, -y, i) for i, (x, y) in enumerate(points)])

        ufs = UnionFindSet(n)
        edges.sort()

        res, num = 0, 1
        for length, x, y in edges:
            if ufs.union_set(x, y):
                res += length
                num += 1
                if num == n:
                    break

        return res


def main():
    # Example 1: Output: 20
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

    # Example 2: Output: 18
    # points = [[3, 12], [-2, 5], [-4, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCostConnectPoints(points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
