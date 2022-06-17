#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0968-Binary-Tree-Cameras.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-17
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0968 - (Easy) - Binary Tree Cameras
https://leetcode.com/problems/binary-tree-cameras/

Description & Requirement:
    You are given the root of a binary tree. We install cameras on the tree nodes where 
    each camera at a node can monitor its parent, itself, and its immediate children.

    Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
    Input: root = [0,0,null,0,0]
    Output: 1
    Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:
    Input: root = [0,0,null,0,null,0,null,null,0]
    Output: 2
    Explanation: At least two cameras are needed to monitor all nodes of the tree. 
        The above image shows one of the valid configurations of camera placement.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    Node.val == 0
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return 1
        # main method: (DFS & DP)
        return self._minCameraCover(root)

    def _minCameraCover(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)
        # set 3 types of states to represent the number of cameras we need to cover the whole subtree of cur_node
        # state a: must place a camera on the current node
        # state b: it's optional to place a camera on the current node
        # state c: it's optional to cover the current node
        # node.a = node.left.c + node.right.c + 1
        # node.b = min(node.a, min(node.left.a + node.right.b, node.left.b + node.right.a))

        def __dfs(node: TreeNode):
            if not isinstance(node, TreeNode):
                return float("inf"), 0, 0

            # recursively calculate the states of the left and right children of the current node
            left_a, left_b, left_c = __dfs(node.left)
            right_a, right_b, right_c = __dfs(node.right)
            # update the states of the current node
            cur_a = left_c + right_c + 1
            cur_b = min(cur_a, left_a + right_b, right_a + left_b)
            cur_c = min(cur_a, left_b + right_b)
            return cur_a, cur_b, cur_c

        root_a, root_b, root_c = __dfs(root)
        return root_b


def main():
    # Example 1: Output: 1
    root = [0, 0, None, 0, 0]

    # Example 2: Output: 2
    # root = [0, 0, None, 0, None, 0, None, None, 0]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCameraCover(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
