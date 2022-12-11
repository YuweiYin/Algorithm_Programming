#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0124-Binary-Tree-Maximum-Path-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-11
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0124 - (Hard) - Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Description & Requirement:
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
    has an edge connecting them. A node can only appear in the sequence at most once. 
    Note that the path does not need to pass through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
    The number of nodes in the tree is in the range [1, 3 * 10^4].
    -1000 <= Node.val <= 1000
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (DFS traverse)
        return self._maxPathSum(root)

    def _maxPathSum(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        res = [root.val]

        def __dfs(node):
            if not node:
                return 0

            left_sum = max(__dfs(node.left), 0)
            right_sum = max(__dfs(node.right), 0)
            merged_sum = node.val + left_sum + right_sum
            res[0] = max(res[0], merged_sum)

            return node.val + max(left_sum, right_sum)

        __dfs(root)
        return res[0]


def main():
    # Example 1: Output: 6
    # root = [1, 2, 3]

    # Example 2: Output: 42
    root = [-10, 9, 20, None, None, 15, 7]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxPathSum(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
