#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0100-Same-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-10
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0100 - (Easy) - Same Tree
https://leetcode.com/problems/same-tree/

Description & Requirement:
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true
Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false
Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -10^4 <= Node.val <= 10^4
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # main method: (DFS)
        return self._isSameTree(p, q)

    def _isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not isinstance(p, TreeNode) and not isinstance(q, TreeNode):
            return True
        elif not isinstance(p, TreeNode) or not isinstance(q, TreeNode):
            return False
        elif p.val != q.val:
            return False
        else:
            return self._isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    # Example 1: Output: true
    # p = [1, 2, 3]
    # q = [1, 2, 3]

    # Example 2: Output: false
    # p = [1, 2]
    # q = [1, None, 2]

    # Example 3: Output: false
    p = [1, 2, 1]
    q = [1, 1, 2]

    p_node = TreeNode.build_binary_tree_layer(p)
    q_node = TreeNode.build_binary_tree_layer(q)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isSameTree(p_node, q_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
