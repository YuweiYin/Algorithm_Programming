#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0965-Univalued-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-24
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0965 - (Easy) - Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/

Description & Requirement:
    A binary tree is uni-valued if every node in the tree has the same value.

    Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:
    Input: root = [1,1,1,1,1,null,1]
    Output: true
Example 2:
    Input: root = [2,2,2,5,2]
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    0 <= Node.val < 100
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
        for idx, cur_root in enumerate(node_list):
            if cur_root is not None:
                cur_root_right_index = (idx + 1) << 1
                cur_root_left_index = cur_root_right_index - 1
                if cur_root_left_index < len_node_list:
                    cur_root.left = node_list[cur_root_left_index]
                if cur_root_right_index < len_node_list:
                    cur_root.right = node_list[cur_root_right_index]
        return node_list[0]  # return root_node

    @staticmethod
    def show_binary_tree_pre_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                val_list.append(cur_root.val)
                __dfs(cur_root.left)
                __dfs(cur_root.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_mid_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                __dfs(cur_root.left)
                val_list.append(cur_root.val)
                __dfs(cur_root.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_post_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                __dfs(cur_root.left)
                __dfs(cur_root.right)
                val_list.append(cur_root.val)

        __dfs(root_node)
        return val_list


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # exception case
        if not isinstance(root, TreeNode):
            return False
        # main method: (traverse)
        return self._isUnivalTree(root)

    def _isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        assert isinstance(root, TreeNode)
        root_val = root.val

        def __valid(node: Optional[TreeNode]) -> bool:
            if isinstance(node, TreeNode):
                if node.val != root_val:
                    return False
                return __valid(node.left) and __valid(node.right)
            else:
                return True

        return __valid(root)


def main():
    # Example 1: Output: true
    root = [1, 1, 1, 1, 1, None, 1]

    # Example 2: Output: false
    # root = [2, 2, 2, 5, 2]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isUnivalTree(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
