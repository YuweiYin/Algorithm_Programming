#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1569-Number-of-Ways-to-Reorder-Array-to-Get-Same-BST.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1569 - (Hard) - Number of Ways to Reorder Array to Get Same BST
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

Description & Requirement:
    Given an array nums that represents a permutation of integers from 1 to n. 
    We are going to construct a binary search tree (BST) by inserting the elements 
    of nums in order into an initially empty BST. Find the number of different ways 
    to reorder nums so that the constructed BST is identical to that formed from the original array nums.

        For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, 
        and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

    Return the number of ways to reorder nums such that the BST formed 
    is identical to the original BST formed from nums.

    Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: nums = [2,1,3]
    Output: 1
    Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. 
        There are no other ways to reorder nums which will yield the same BST.
Example 2:
    Input: nums = [3,4,5,1,2]
    Output: 5
    Explanation: The following 5 arrays will yield the same BST: 
        [3,1,2,4,5]
        [3,1,4,2,5]
        [3,1,4,5,2]
        [3,4,1,2,5]
        [3,4,1,5,2]
Example 3:
    Input: nums = [1,2,3]
    Output: 0
    Explanation: There are no other orderings of nums that will yield the same BST.

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= nums.length
    All integers in nums are distinct.
"""


class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 1
        self.ans = 0


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def getroot(self, x: int) -> int:
        return self.root[self.find(x)]

    def unite(self, x: int, y: int):
        self.root[y] = self.root[x]
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]

    def find_unite(self, x: int, y: int) -> bool:
        parentX, parentY = self.find(x), self.find(y)
        if parentX != parentY:
            self.unite(parentX, parentY)
            return True
        return False


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (union find)
        return self._numOfWays(nums)

    def _numOfWays(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        n = len(nums)
        if n == 1:
            return 0

        MOD = int(1e9+7)
        fac = [0] * n
        inv = [0] * n
        facInv = [0] * n
        fac[0] = inv[0] = facInv[0] = 1
        fac[1] = inv[1] = facInv[1] = 1
        for i in range(2, n):
            fac[i] = fac[i - 1] * i % MOD
            inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
            facInv[i] = facInv[i - 1] * inv[i] % MOD

        found = dict()
        uf = UnionFind(n)
        for i in range(n - 1, -1, -1):
            val = nums[i] - 1
            node = TreeNode()
            if val > 0 and val - 1 in found:
                l_child = uf.getroot(val - 1)
                node.left = found[l_child]
                node.size += node.left.size
                uf.find_unite(val, l_child)
            if val < n - 1 and val + 1 in found:
                r_child = uf.getroot(val + 1)
                node.right = found[r_child]
                node.size += node.right.size
                uf.find_unite(val, r_child)

            l_size = node.left.size if node.left else 0
            r_size = node.right.size if node.right else 0
            l_res = node.left.ans if node.left else 1
            r_res = node.right.ans if node.right else 1
            node.ans = fac[l_size + r_size] * facInv[l_size] * facInv[r_size] * l_res * r_res % MOD
            found[val] = node

        return (found[nums[0] - 1].ans - 1 + MOD) % MOD


def main():
    # Example 1: Output: 1
    # nums = [2, 1, 3]

    # Example 2: Output: 5
    nums = [3, 4, 5, 1, 2]

    # Example 3: Output: 0
    # nums = [1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numOfWays(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
