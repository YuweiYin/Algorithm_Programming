#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0538-Convert-BST-to-Greater-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-16
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0538 - (Medium) - Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/

Description & Requirement:
    Given the root of a Binary Search Tree (BST), convert it to a Greater Tree 
    such that every key of the original BST is changed to 
    the original key plus the sum of all keys greater than the original key in BST.

    As a reminder, a binary search tree is a tree that satisfies these constraints:
        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:
    Input: root = [0,null,1]
    Output: [1,null,1]

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -10^4 <= Node.val <= 10^4
    All the values in the tree are unique.
    root is guaranteed to be a valid binary search tree.

Note:
    This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        # main method: (suffix sum, record number mapping)
        return self._convertBST(root)

    def _convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        assert isinstance(root, TreeNode)

        val_list = []

        def __dfs(cur_node) -> None:  # in-order traverse
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                val_list.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(root)

        suffix_sum = [0]
        for idx, val in enumerate(val_list[::-1]):
            suffix_sum.append(suffix_sum[idx] + val)
        suffix_sum = suffix_sum[::-1]

        val_map = dict({})
        for idx, val in enumerate(val_list):
            val_map[val] = suffix_sum[idx]
        del val_list
        del suffix_sum

        def __modify_val(cur_node: Optional[TreeNode]) -> None:
            if isinstance(cur_node, TreeNode):
                cur_node.val = val_map[cur_node.val]
                __modify_val(cur_node.left)
                __modify_val(cur_node.right)

        __modify_val(root)
        return root


def main():
    # Example 1: Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]

    # Example 2: Output: [1,null,1]
    # root = [0, None, 1]

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.convertBST(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    if isinstance(ans, TreeNode):
        print(TreeNode.show_binary_tree_mid_order(ans))
    else:
        print("null")

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
