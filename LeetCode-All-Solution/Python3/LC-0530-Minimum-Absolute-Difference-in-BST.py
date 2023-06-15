#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0530-Minimum-Absolute-Difference-in-BST.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-14
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0530 - (Easy) - Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Description & Requirement:
    Given the root of a Binary Search Tree (BST), 
    return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1
Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [2, 10^4].
    0 <= Node.val <= 10^5

Note:
    This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (in-order traversal)
        return self._getMinimumDifference(root)

    def _getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        def __in_traverse(node: TreeNode):
            if isinstance(node, TreeNode):
                __in_traverse(node.left)
                val_list.append(node.val)
                __in_traverse(node.right)

        val_list = []
        __in_traverse(root)

        res = int(1e9 + 7)
        for i in range(len(val_list) - 1):
            res = min(res, abs(val_list[i] - val_list[i + 1]))

        return res


def main():
    # Example 1: Output: 1
    root = [4, 2, 6, 1, 3]

    # Example 2: Output: 1
    # root = [1, 0, 48, None, None, 12, 49]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getMinimumDifference(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
