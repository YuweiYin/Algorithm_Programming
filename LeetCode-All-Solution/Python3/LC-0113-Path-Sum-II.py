#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0113-Path-Sum-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-26
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0113 - (Medium) - Path Sum II
https://leetcode.com/problems/path-sum-ii/

Description & Requirement:
    Given the root of a binary tree and an integer targetSum, 
    return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
    Each path should be returned as a list of the node values, not node references.

    A root-to-leaf path is a path starting from the root and ending at any leaf node. 
    A leaf is a node with no children.

Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
    Explanation: There are two paths whose sum equals targetSum:
        5 + 4 + 11 + 2 = 22
        5 + 8 + 4 + 5 = 22
Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: []
Example 3:
    Input: root = [1,2], targetSum = 0
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
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

    @staticmethod
    def show_binary_tree_level_order(root_node) -> List[List[int]]:
        if not isinstance(root_node, TreeNode):
            return []

        res = []
        bfs_queue = [root_node]  # deal with all nodes in the same layer at a time

        while len(bfs_queue) > 0:
            new_bfs_queue = []  # nodes of the next layer
            new_layer_nodes = []  # node vals of this layer
            for node in bfs_queue:
                new_layer_nodes.append(node.val)
                if isinstance(node.left, TreeNode):
                    new_bfs_queue.append(node.left)
                if isinstance(node.right, TreeNode):
                    new_bfs_queue.append(node.right)
            res.append(new_layer_nodes)  # update res
            bfs_queue = new_bfs_queue  # update bfs_queue

        return res


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # exception case
        if not isinstance(root, TreeNode):  # no nodes
            return []
        # main method: (dfs traverse & backtrace)
        return self._pathSum(root, targetSum)

    def _pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        assert isinstance(root, TreeNode)
        res = []

        def __dfs(cur_node: Optional[TreeNode], cur_sum: int, cur_path: List[int]):
            if isinstance(cur_node, TreeNode):
                cur_sum += cur_node.val
                # cur_node is a left node
                if not isinstance(cur_node.left, TreeNode) and not isinstance(cur_node.right, TreeNode):
                    if cur_sum == targetSum:
                        valid_path = cur_path[:]
                        valid_path.append(cur_node.val)
                        res.append(valid_path)
                    return
                # go deeper
                cur_path.append(cur_node.val)
                if isinstance(cur_node.left, TreeNode):
                    __dfs(cur_node.left, cur_sum, cur_path)
                if isinstance(cur_node.right, TreeNode):
                    __dfs(cur_node.right, cur_sum, cur_path)
                # backtrace
                cur_path.pop()
            else:  # can't get the target sum till the end leaf
                return False

        __dfs(root, 0, [])
        return res


def main():
    # Example 1: Output: [[5,4,11,2],[5,8,4,5]]
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    targetSum = 22

    # Example 2: Output: []
    # root = [1, 2, 3]
    # targetSum = 5

    # Example 3: Output: []
    # root = [1, 2]
    # targetSum = 0

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pathSum(root_node, targetSum)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
