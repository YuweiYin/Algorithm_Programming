#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0094-Binary-Tree-Inorder-Traversal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-06
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections

"""
LeetCode - 0094 - (Easy) - Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Description & Requirement:
    Given the root of a binary tree, 
    return the inorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,null,null,3]
    Output: [1,3,2]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [1]
    Output: [1]

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # exception case
        if not isinstance(root, TreeNode):
            return []  # no tree, just null
        # main method: (DFS inorder Traversal)
        return self._inorderTraversal(root)

    def _inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Runtime: 34 ms, faster than 88.55% of Python3 online submissions for Binary Tree Inorder Traversal.
        Memory Usage: 13.8 MB, less than 60.15% of Python3 online submissions for Binary Tree Inorder Traversal.
        """
        assert isinstance(root, TreeNode)
        res = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                res.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(root)
        return res


def main():
    # Example 1: Output: [1,2,3]
    root = [1, None, 2, None, None, 3]

    # Example 2: Output: []
    # root = []

    # Example 3: Output: [1]
    # root = [1]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.inorderTraversal(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)
    # print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
