#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1373-Maximum-Sum-BST-in-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-20
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 1373 - (Hard) - Maximum Sum BST in Binary Tree
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

Description & Requirement:
    Given a binary tree root, return the maximum sum of all keys of 
    any sub-tree which is also a Binary Search Tree (BST).

    Assume a BST is defined as follows:
        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
    Output: 20
    Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:
    Input: root = [4,3,null,1,2]
    Output: 2
    Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:
    Input: root = [-4,-2,-5]
    Output: 0
    Explanation: All values are negatives. Return an empty BST.

Constraints:
    The number of nodes in the tree is in the range [1, 4 * 10^4].
    -4 * 10^4 <= Node.val <= 4 * 10^4
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


class SubTree:
    def __init__(self, is_bst, min_value, max_value, sum_value):
        self.is_bst = is_bst
        self.min_value = min_value
        self.max_value = max_value
        self.sum_value = sum_value


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (DFS)
        return self._maxSumBST(root)

    def _maxSumBST(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        def __dfs(root):
            if root is None:
                return SubTree(True, float("inf"), -float("inf"), 0)

            left = __dfs(root.left)
            right = __dfs(root.right)

            if left.is_bst and right.is_bst and left.max_value < root.val < right.min_value:
                cur_sum = root.val + left.sum_value + right.sum_value
                res[0] = max(res[0], cur_sum)
                return SubTree(True, min(left.min_value, root.val), max(root.val, right.max_value), cur_sum)
            else:
                return SubTree(False, 0, 0, 0)

        res = [0]
        __dfs(root)

        return res[0]


def main():
    # Example 1: Output: 20
    # root = [1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6]

    # Example 2: Output: 2
    # root = [4, 3, None, 1, 2]

    # Example 3: Output: 0
    root = [-4, -2, -5]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSumBST(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
