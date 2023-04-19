#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1372-Longest-ZigZag-Path-in-a-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-19
=================================================================="""

import sys
import time
from typing import List, Optional
import collections
# import functools

"""
LeetCode - 1372 - (Medium) - Longest ZigZag Path in a Binary Tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

Description & Requirement:
    You are given the root of a binary tree.

    A ZigZag path for a binary tree is defined as follow:
        Choose any node in the binary tree and a direction (right or left).
        If the current direction is right, move to the right child of the current node; 
            otherwise, move to the left child.
        Change the direction from right to left or from left to right.
        Repeat the second and third steps until you can't move in the tree.

    Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

    Return the longest ZigZag path contained in that tree.

Example 1:
    Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
    Output: 3
    Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:
    Input: root = [1,1,1,null,1,null,null,1,1,null,1]
    Output: 4
    Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:
    Input: root = [1]
    Output: 0

Constraints:
    The number of nodes in the tree is in the range [1, 5 * 10^4].
    1 <= Node.val <= 100
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0
        # main method: (dynamic programming)
        return self._longestZigZag(root)

    def _longestZigZag(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        dp, graph = collections.defaultdict(int), collections.defaultdict(int)
        queue = collections.deque([[root, None]])
        while len(queue) > 0:
            node, parent = queue.popleft()
            if isinstance(parent, TreeNode):
                if parent.left == node:
                    dp[node] = graph[parent] + 1
                else:
                    graph[node] = dp[parent] + 1
            if isinstance(node.left, TreeNode):
                queue.append([node.left, node])
            if isinstance(node.right, TreeNode):
                queue.append([node.right, node])

        res = 0
        for _, val in dp.items():
            res = max(res, val)
        for _, val in graph.items():
            res = max(res, val)

        return res


def main():
    # Example 1: Output: 3
    # root = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1]

    # Example 2: Output: 4
    # root = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]

    # Example 3: Output: 0
    root = [1]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestZigZag(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
