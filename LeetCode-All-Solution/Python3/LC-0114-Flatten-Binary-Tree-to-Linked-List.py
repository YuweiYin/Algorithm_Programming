#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0114-Flatten-Binary-Tree-to-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-27
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0114 - (Medium) - Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Description & Requirement:
    Given the root of a binary tree, flatten the tree into a "linked list":
        The "linked list" should use the same TreeNode class where 
            the right child pointer points to the next node in the list and the left child pointer is always null.
        The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [0]
    Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

Follow up:
    Can you flatten the tree in-place (with O(1) extra space)?
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # exception case
        if not isinstance(root, TreeNode):
            return
        # main method: (find predecessor)
        self._flatten(root)

    def _flatten(self, root: Optional[TreeNode]) -> None:
        assert isinstance(root, TreeNode)

        cur_node = root
        while isinstance(cur_node, TreeNode):
            if isinstance(cur_node.left, TreeNode):
                predecessor = next_node = cur_node.left
                while isinstance(predecessor.right, TreeNode):
                    predecessor = predecessor.right
                predecessor.right = cur_node.right
                cur_node.left = None
                cur_node.right = next_node
            cur_node = cur_node.right


def main():
    # Example 1: Output: [1,null,2,null,3,null,4,null,5,null,6]
    root = [1, 2, 5, 3, 4, None, 6]

    # Example 2: Output: []
    # root = []

    # Example 3: Output: [0]
    # root = [0]

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_pre_order(root_node))

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.flatten(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(TreeNode.show_binary_tree_pre_order(root_node))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
