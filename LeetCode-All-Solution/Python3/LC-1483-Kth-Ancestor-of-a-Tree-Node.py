#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1483-Kth-Ancestor-of-a-Tree-Node.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1483 - (Hard) - Kth Ancestor of a Tree Node
https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

Description & Requirement:
    You are given a tree with n nodes numbered from 0 to n - 1 
    in the form of a parent array parent where parent[i] is the parent of ith node. 
    The root of the tree is node 0. Find the kth ancestor of a given node.

    The k-th ancestor of a tree node is the kth node in the path from that node to the root node.

    Implement the TreeAncestor class:
        TreeAncestor(int n, int[] parent) Initializes the object 
            with the number of nodes in the tree and the parent array.
        int getKthAncestor(int node, int k) return the kth ancestor of the given node node. 
            If there is no such ancestor, return -1.

Example 1:
    Input
        ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
        [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
    Output
        [null, 1, 0, -1]
    Explanation
        TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
        treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
        treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
        treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor

Constraints:
    1 <= k <= n <= 5 * 10^4
    parent.length == n
    parent[0] == -1
    0 <= parent[i] < n for all 0 < i < n
    0 <= node < n
    There will be at most 5 * 10^4 queries.
"""


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = 16
        self.ancestors = [[-1] * self.LOG for _ in range(n)]
        for i in range(n):
            self.ancestors[i][0] = parent[i]
        for j in range(1, self.LOG):
            for i in range(n):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if (k >> j) & 1:
                node = self.ancestors[node][j]
                if node == -1:
                    return -1
        return node


def main():
    # Example 1: Output: [null, 1, 0, -1]
    command_list = ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
    param_list = [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]

    # init instance
    obj = TreeAncestor(param_list[0][0], param_list[0][1])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "getKthAncestor" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.getKthAncestor(param[0], param[1]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
