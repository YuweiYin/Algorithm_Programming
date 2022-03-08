#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0226-Invert-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-08
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0226 - (Easy) - Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Description & Requirement:
    Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]
Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
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
    def show_binary_tree_in_order(root_node) -> List[int]:
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

    @staticmethod
    def show_binary_tree_level_order(root_node) -> List[List[int]]:
        if not isinstance(root_node, TreeNode):
            return []

        res = []
        bfs_queue = [root_node]  # deal with all nodes in the same layer at a time

        while len(bfs_queue) > 0:
            new_bfs_queue = []  # nodes of the next layer
            new_layer_nodes = []  # node vals of this layer
            for node in bfs_queue:
                new_layer_nodes.append(node.val)
                if isinstance(node.left, TreeNode):
                    new_bfs_queue.append(node.left)
                if isinstance(node.right, TreeNode):
                    new_bfs_queue.append(node.right)
            res.append(new_layer_nodes)  # update res
            bfs_queue = new_bfs_queue  # update bfs_queue

        return res


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):  # no nodes
            return None
        # main method: (dfs traverse: swap left and right children of every node)
        return self._invertTree(root)

    def _invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        assert isinstance(root, TreeNode)

        def __dfs(cur_node: Optional[TreeNode]):
            if isinstance(cur_node, TreeNode):
                # swap left and right children of every node
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                # dfs traverse children nodes
                if isinstance(cur_node.left, TreeNode):
                    __dfs(cur_node.left)
                if isinstance(cur_node.right, TreeNode):
                    __dfs(cur_node.right)

        __dfs(root)
        return root


def main():
    # Example 1: Output: [4,7,2,9,6,3,1]
    root = [4, 2, 7, 1, 3, 6, 9]

    # Example 2: Output: [2,3,1]
    # root = [2, 1, 3]

    # Example 3: Output: []
    # root = []

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.invertTree(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(TreeNode.show_binary_tree_level_order(root_node))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
