#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0106-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-16
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0106 - (Medium) - Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Description & Requirement:
    Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree 
    and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
Example 2:
    Input: inorder = [-1], postorder = [-1]
    Output: [-1]

Constraints:
    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree.
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # exception case
        assert isinstance(inorder, list) and isinstance(postorder, list) and len(inorder) == len(postorder) >= 1
        # main method: (divide and conquer + dfs)
        return self._buildTree(inorder, postorder)

    def _buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        assert isinstance(inorder, list) and isinstance(postorder, list) and len(inorder) == len(postorder) >= 1

        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])

        pos = inorder.index(postorder[-1])
        root.left = self._buildTree(inorder[:pos], postorder[:pos])
        root.right = self._buildTree(inorder[pos + 1:], postorder[pos: -1])

        return root


def main():
    # Example 1: Output: [3,9,20,null,null,15,7]
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    # Example 2: Output: [-1]
    # inorder = [-1]
    # postorder = [-1]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.buildTree(inorder, postorder)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
