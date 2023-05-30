#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1110-Delete-Nodes-And-Return-Forest.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-30
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 1110 - (Medium) - Delete Nodes And Return Forest
https://leetcode.com/problems/delete-nodes-and-return-forest/

Description & Requirement:
    Given the root of a binary tree, each node in the tree has a distinct value.

    After deleting all nodes with a value in to_delete, 
    we are left with a forest (a disjoint union of trees).

    Return the roots of the trees in the remaining forest. 
    You may return the result in any order.

Example 1:
    Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    Output: [[1,2,null,4],[6],[7]]
Example 2:
    Input: root = [1,2,4,null,3], to_delete = [3]
    Output: [[1,2,4]]

Constraints:
    The number of nodes in the given tree is at most 1000.
    Each node has a distinct value between 1 and 1000.
    to_delete.length <= 1000
    to_delete contains distinct values between 1 and 1000.
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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # exception case
        assert isinstance(root, TreeNode)
        assert isinstance(to_delete, list) and len(to_delete) >= 1
        # main method: (DFS)
        return self._delNodes(root, to_delete)

    def _delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        assert isinstance(root, TreeNode)
        assert isinstance(to_delete, list) and len(to_delete) >= 1

        def __dfs(node: Optional[TreeNode], is_root: bool, to_delete_set: set[int], roots: List[TreeNode]) -> \
                Optional[TreeNode]:
            if not isinstance(node, TreeNode):
                return None

            delete = node.val in to_delete_set
            node.left = __dfs(node.left, delete, to_delete_set, roots)
            node.right = __dfs(node.right, delete, to_delete_set, roots)

            if delete:
                return None
            else:
                if is_root:
                    roots.append(node)
                return node

        roots = []
        __dfs(root, True, set(to_delete), roots)

        return roots


def main():
    # Example 1: Output: [[1,2,null,4],[6],[7]]
    root = [1, 2, 3, 4, 5, 6, 7]
    to_delete = [3, 5]

    # Example 2: Output: [[1,2,4]]
    root = [1, 2, 4, None, 3]
    to_delete = [3]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.delNodes(root_node, to_delete)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
