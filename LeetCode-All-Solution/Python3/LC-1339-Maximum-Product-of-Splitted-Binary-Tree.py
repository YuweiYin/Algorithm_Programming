#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1339-Maximum-Product-of-Splitted-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-10
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 1339 - (Medium) - Maximum Product of Splitted Binary Tree
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

Description & Requirement:
    Given the root of a binary tree, split the binary tree into two subtrees by removing one edge 
    such that the product of the sums of the subtrees is maximized.

    Return the maximum product of the sums of the two subtrees. 
    Since the answer may be too large, return it modulo 10^9 + 7.

    Note that you need to maximize the answer before taking the mod and not after taking it.

Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: 110
    Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:
    Input: root = [1,null,2,3,4,null,null,5,6]
    Output: 90
    Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Constraints:
    The number of nodes in the tree is in the range [2, 5 * 10^4].
    1 <= Node.val <= 10^4
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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (DFS pre-order traverse)
        return self._maxProduct(root)

    def _maxProduct(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        node_sum = [0]
        res = [0]

        def __dfs_sum(node: Optional[TreeNode]) -> None:
            if isinstance(node, TreeNode):
                node_sum[0] += node.val
                __dfs_sum(node.left)
                __dfs_sum(node.right)

        def __dfs_best_prod(node: Optional[TreeNode]) -> int:
            if isinstance(node, TreeNode):
                cur_prod = __dfs_best_prod(node.left) + __dfs_best_prod(node.right) + node.val
                if abs(2 * cur_prod - node_sum[0]) < abs(2 * res[0] - node_sum[0]):
                    res[0] = cur_prod
                return cur_prod
            else:
                return 0

        __dfs_sum(root)
        __dfs_best_prod(root)

        return (res[0] * (node_sum[0] - res[0])) % int(1e9+7)


def main():
    # Example 1: Output: 110
    root = [1, 2, 3, 4, 5, 6]

    # Example 2: Output: 90
    # root = [1, None, 2, 3, 4, None, None, 5, 6]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxProduct(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
