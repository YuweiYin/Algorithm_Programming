#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0111-Minimum-Depth-of-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-10
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0111 - (Easy) - Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

Description & Requirement:
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path 
    from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 2
Example 2:
    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5

Constraints:
    The number of nodes in the tree is in the range [0, 10^5].
    -1000 <= Node.val <= 1000
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0
        # main method: (DFS)
        return self._minDepth(root)

    def _minDepth(self, root: Optional[TreeNode]) -> int:
        if not isinstance(root, TreeNode):
            return 0

        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return 1

        left_min_depth = self._minDepth(root.left)
        right_min_depth = self._minDepth(root.right)

        if isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return left_min_depth + 1

        if not isinstance(root.left, TreeNode) and isinstance(root.right, TreeNode):
            return right_min_depth + 1

        return min(left_min_depth, right_min_depth) + 1


def main():
    # Example 1: Output: 2
    # root = [3, 9, 20, None, None, 15, 7]

    # Example 2: Output: 5
    root = [2, None, 3, None, 4, None, 5, None, 6]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minDepth(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
