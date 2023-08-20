#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2236-Root-Equals-Sum-of-Children.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-20
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools
# import itertools

"""
LeetCode - 2236 - (Easy) Root Equals Sum of Children
https://leetcode.com/problems/root-equals-sum-of-children/

Description & Requirement:
    You are given the root of a binary tree that consists of exactly 3 nodes: 
    the root, its left child, and its right child.

    Return true if the value of the root is equal to the sum of 
    the values of its two children, or false otherwise.

Example 1:
    Input: root = [10,4,6]
    Output: true
    Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
        10 is equal to 4 + 6, so we return true.
Example 2:
    Input: root = [5,3,1]
    Output: false
    Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
        5 is not equal to 3 + 1, so we return false.

Constraints:
    The tree consists only of the root, its left child, and its right child.
    -100 <= Node.val <= 100
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
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (just do it)
        return self._checkTree(root)

    def _checkTree(self, root: Optional[TreeNode]) -> bool:
        assert isinstance(root, TreeNode)

        return root.val == root.left.val + root.right.val


def main():
    # Example 1: Output: true
    root = [10, 4, 6]

    # Example 2: Output: false
    # root = [5, 3, 1]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.checkTree(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
