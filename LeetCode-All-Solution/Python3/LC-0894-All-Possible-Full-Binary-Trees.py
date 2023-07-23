#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0894-All-Possible-Full-Binary-Trees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-23
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools
# import itertools

"""
LeetCode - 0894 - (Medium) - All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/

Description & Requirement:
    Given an integer n, return a list of all possible full binary trees with n nodes. 
    Each node of each tree in the answer must have Node.val == 0.

    Each element of the answer is the root node of one possible tree. 
    You may return the final list of trees in any order.

    A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:
    Input: n = 7
    Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
        [0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:
    Input: n = 3
    Output: [[0,0,0]]

Constraints:
    1 <= n <= 20
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  # the left and right of leaf_node are both None

    @staticmethod
    def build_binary_tree_layer(val_list: List[int]):
        if not isinstance(val_list, list) or len(val_list) <= 0:
            return None

        node_list = []
        for v in val_list:
            if v is None:
                node_list.append(None)
            else:
                node_list.append(TreeNode(val=v))
        len_node_list = len(node_list)
        for idx, cur_node in enumerate(node_list):
            if cur_node is not None:
                cur_node_right_index = (idx + 1) << 1
                cur_node_left_index = cur_node_right_index - 1
                if cur_node_left_index < len_node_list:
                    cur_node.left = node_list[cur_node_left_index]
                if cur_node_right_index < len_node_list:
                    cur_node.right = node_list[cur_node_right_index]
        return node_list[0]  # return root_node

    @staticmethod
    def show_binary_tree_pre_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                val_list.append(cur_node.val)
                __dfs(cur_node.left)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_mid_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                val_list.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_post_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                __dfs(cur_node.right)
                val_list.append(cur_node.val)

        __dfs(root_node)
        return val_list


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (recursion)
        return self._allPossibleFBT(n)

    def _allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        assert isinstance(n, int) and n >= 1

        res = []

        if n == 1:
            return [TreeNode(0)]
        if n % 2 == 0:
            return []

        left_num = 1
        right_num = n - 2

        while right_num > 0:
            left_tree = self._allPossibleFBT(left_num)
            right_tree = self._allPossibleFBT(right_num)

            for i in range(len(left_tree)):
                for j in range(len(right_tree)):
                    root = TreeNode(0)
                    root.left = left_tree[i]
                    root.right = right_tree[j]
                    res.append(root)

            left_num += 2
            right_num -= 2

        return res


def main():
    # Example 1: Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
    #     [0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    n = 7

    # Example 2: Output: [[0,0,0]]
    n = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.allPossibleFBT(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
