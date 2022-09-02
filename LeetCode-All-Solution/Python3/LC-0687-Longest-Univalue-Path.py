#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0687-Longest-Univalue-Path.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-02
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0687 - (Medium) - Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/

Description & Requirement:
    Given the root of a binary tree, return the length of the longest path, 
    where each node in the path has the same value. 
    This path may or may not pass through the root.

    The length of the path between two nodes is represented by the number of edges between them.

Example 1:
    Input: root = [5,4,5,1,1,null,5]
    Output: 2
    Explanation: The shown image shows that the longest path of the same value (i.e. 5).
Example 2:
    Input: root = [1,4,5,4,4,null,5]
    Output: 2
    Explanation: The shown image shows that the longest path of the same value (i.e. 4).

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -1000 <= Node.val <= 1000
    The depth of the tree will not exceed 1000.
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0
        # main method: (DFS)
        return self._longestUnivaluePath(root)

    def _longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        res = [0]

        def __dfs(node: Optional[TreeNode]) -> int:
            if not isinstance(node, TreeNode):
                return 0
            left = __dfs(node.left)
            right = __dfs(node.right)

            if isinstance(node.left, TreeNode) and node.left.val == node.val:
                left_new = left + 1
            else:
                left_new = 0

            if isinstance(node.right, TreeNode) and node.right.val == node.val:
                right_new = right + 1
            else:
                right_new = 0

            res[0] = max(res[0], left_new + right_new)
            return max(left_new, right_new)

        __dfs(root)

        return res[0]


def main():
    # Example 1: Output: 2
    # root = [5, 4, 5, 1, 1, None, 5]

    # Example 2: Output: 2
    root = [1, 4, 5, 4, 4, None, 5]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestUnivaluePath(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
