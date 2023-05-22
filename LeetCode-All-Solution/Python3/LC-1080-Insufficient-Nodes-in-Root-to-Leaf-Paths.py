#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1080-Insufficient-Nodes-in-Root-to-Leaf-Paths.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-22
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 1080 - (Medium) - Insufficient Nodes in Root to Leaf Paths
https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

Description & Requirement:
    Given the root of a binary tree and an integer limit, 
    delete all insufficient nodes in the tree simultaneously, 
    and return the root of the resulting binary tree.

    A node is insufficient if every root to leaf path intersecting this node 
    has a sum strictly less than limit.

    A leaf is a node with no children.

Example 1:
    Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
    Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:
    Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
    Output: [5,4,8,11,null,17,4,7,null,null,null,5]
Example 3:
    Input: root = [1,2,-3,-5,null,4,null], limit = -1
    Output: [1,null,-3,4]

Constraints:
    The number of nodes in the tree is in the range [1, 5000].
    -10^5 <= Node.val <= 10^5
    -10^9 <= limit <= 10^9
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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # exception case
        assert isinstance(root, TreeNode) and isinstance(limit, int)
        # main method: (DFS)
        return self._sufficientSubset(root, limit)

    def _sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        assert isinstance(root, TreeNode) and isinstance(limit, int)

        def __check_leaf(node, sum, limit):
            if not isinstance(node, TreeNode):
                return False

            if not isinstance(node.left, TreeNode) and not isinstance(node.right, TreeNode):
                return node.val + sum >= limit

            have_sufficient_left = __check_leaf(node.left, sum + node.val, limit)
            have_sufficient_right = __check_leaf(node.right, sum + node.val, limit)

            if not have_sufficient_left:
                node.left = None
            if not have_sufficient_right:
                node.right = None

            return have_sufficient_left or have_sufficient_right

        return root if __check_leaf(root, 0, limit) else None


def main():
    # Example 1: Output: [1,2,3,4,null,null,7,8,9,null,14]
    root = [1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]
    limit = 1

    # Example 2: Output: [5,4,8,11,null,17,4,7,null,null,null,5]
    # root = [5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]
    # limit = 22

    # Example 3: Output: [1,null,-3,4]
    # root = [1, 2, -3, -5, None, 4, None]
    # limit = -1

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sufficientSubset(root_node, limit)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
