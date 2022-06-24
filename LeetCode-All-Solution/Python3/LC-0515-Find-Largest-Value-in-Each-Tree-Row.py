#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0515-Find-Largest-Value-in-Each-Tree-Row.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-24
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0515 - (Medium) - Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Description & Requirement:
    Given the root of a binary tree, 
    return an array of the largest value in each row of the tree (0-indexed).

Example 1:
    Input: root = [1,3,2,5,3,null,9]
    Output: [1,3,9]
Example 2:
    Input: root = [1,2,3]
    Output: [1,3]

Constraints:
    The number of nodes in the tree will be in the range [0, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # exception case
        if not isinstance(root, TreeNode):
            return []
        # main method: (BFS layer traverse)
        return self._largestValues(root)

    def _largestValues(self, root: Optional[TreeNode]) -> List[int]:
        assert isinstance(root, TreeNode)

        res = []
        bfs_queue = [root]
        while len(bfs_queue) > 0:
            res.append(max([node.val for node in bfs_queue]))
            new_bfs_queue = []
            for node in bfs_queue:
                if isinstance(node.left, TreeNode):
                    new_bfs_queue.append(node.left)
                if isinstance(node.right, TreeNode):
                    new_bfs_queue.append(node.right)
            bfs_queue = new_bfs_queue

        return res


def main():
    # Example 1: Output: [1,3,9]
    root = [1, 3, 2, 5, 3, None, 9]

    # Example 2: Output: [1,3]
    # root = [1, 2, 3]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestValues(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
