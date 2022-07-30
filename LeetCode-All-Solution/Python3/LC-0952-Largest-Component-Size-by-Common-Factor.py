#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0952-Largest-Component-Size-by-Common-Factor.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-30
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0952 - (Hard) - Largest Component Size by Common Factor
https://leetcode.com/problems/largest-component-size-by-common-factor/

Description & Requirement:
    You are given an integer array of unique positive integers nums. Consider the following graph:
        There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
        There is an undirected edge between nums[i] and nums[j] 
            if nums[i] and nums[j] share a common factor greater than 1.

    Return the size of the largest connected component in the graph.

Example 1:
    Input: nums = [4,6,15,35]
    Output: 4
Example 2:
    Input: nums = [20,50,9,63]
    Output: 2
Example 3:
    Input: nums = [2,3,6,7,4,12,21,39]
    Output: 8

Constraints:
    1 <= nums.length <= 2 * 10^4
    1 <= nums[i] <= 10^5
    All the values of nums are unique.
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert len(nums) == len(set(nums))
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (Union Find)
        return self._largestComponentSize(nums)

    def _largestComponentSize(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        uf = UnionFind(max(nums) + 1)
        for num in nums:
            factor = 2
            while factor * factor <= num:
                if num % factor == 0:
                    uf.merge(num, factor)
                    uf.merge(num, num // factor)
                factor += 1

        uf_counter = collections.Counter(uf.find(num) for num in nums)
        return max(uf_counter.values())


def main():
    # Example 1: Output: 4
    # nums = [4, 6, 15, 35]

    # Example 2: Output: 2
    # nums = [20, 50, 9, 63]

    # Example 3: Output: 8
    nums = [2, 3, 6, 7, 4, 12, 21, 39]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestComponentSize(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
