#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0101-Symmetric-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-07
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0101 - (Easy) - Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Description & Requirement:
    Given the root of a binary tree, 
    check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true
Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

Follow up:
    Could you solve it both recursively and iteratively?
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # exception case
        if not isinstance(root, TreeNode):  # no nodes
            return False
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):  # the root has no children
            return True
        if not isinstance(root.left, TreeNode) or not isinstance(root.right, TreeNode):  # only on child
            return False
        # main method: (dfs traverse)
        return self._isSymmetric(root)

    def _isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def __dfs(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
            if not isinstance(left_node, TreeNode) and not isinstance(right_node, TreeNode):  # both reach to leaf
                return True
            if not isinstance(left_node, TreeNode) or not isinstance(right_node, TreeNode):  # only one reach to leaf
                return False
            if left_node.val != right_node.val:  # vals are not equal
                return False
            # now, vals are equal, check their children
            if isinstance(left_node.left, TreeNode) or isinstance(right_node.right, TreeNode):
                if not __dfs(left_node.left, right_node.right):  # left_node.left matches right_node.right
                    return False
            if isinstance(left_node.right, TreeNode) or isinstance(right_node.left, TreeNode):
                if not __dfs(left_node.right, right_node.left):  # left_node.right matches right_node.left
                    return False
            return True

        return __dfs(root.left, root.right)


def main():
    # Example 1: Output: true
    # root = [1, 2, 2, 3, 4, 4, 3]

    # Example 2: Output: false
    # root = [1, 2, 2, None, 3, None, 3]

    # Example 3: Output: false
    root = [2, 3, 3, 4, None, 5, 4]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isSymmetric(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
