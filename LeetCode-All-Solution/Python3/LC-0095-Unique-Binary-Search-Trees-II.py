#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0095-Unique-Binary-Search-Trees-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-05
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools
# import itertools

"""
LeetCode - 0095 - (Medium) - Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/

Description & Requirement:
    Given an integer n, return all the structurally unique BST's (binary search trees), 
    which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
    Input: n = 3
    Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:
    Input: n = 1
    Output: [[1]]

Constraints:
    1 <= n <= 8
"""


# Definition for a binary tree node.
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (backtrace)
        return self._generateTrees(n)

    def _generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        assert isinstance(n, int) and n >= 1

        def __backtrace(start: int, end: int):
            if start > end:
                return [None]

            res_trees = []
            for i in range(start, end + 1):
                left_trees = __backtrace(start, i - 1)
                right_trees = __backtrace(i + 1, end)

                for lt in left_trees:
                    for rt in right_trees:
                        new_tree = TreeNode(i)
                        new_tree.left = lt
                        new_tree.right = rt
                        res_trees.append(new_tree)

            return res_trees

        return __backtrace(1, n) if n else []


def main():
    # Example 1: Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
    n = 3

    # Example 2: Output: [[1]]
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.generateTrees(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
