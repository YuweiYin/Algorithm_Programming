#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0112-Path-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-08
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0112 - (Easy) - Path Sum
https://leetcode.com/problems/path-sum/

Description & Requirement:
    Given the root of a binary tree and an integer targetSum, 
    return true if the tree has a root-to-leaf path such that 
    adding up all the values along the path equals targetSum.

    A leaf is a node with no children.

Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
        Explanation: The root-to-leaf path with the target sum is shown.
Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There two root-to-leaf paths in the tree:
        (1 --> 2): The sum is 3.
        (1 --> 3): The sum is 4.
        There is no root-to-leaf path with sum = 5.
Example 3:
    Input: root = [], targetSum = 0
    Output: false
    Explanation: Since the tree is empty, there are no root-to-leaf paths.

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # exception case
        if not isinstance(root, TreeNode):  # no nodes
            return False
        # main method: (dfs traverse)
        return self._hasPathSum(root, targetSum)

    def _hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        assert isinstance(root, TreeNode)

        def __dfs(cur_node: Optional[TreeNode], cur_sum: int) -> bool:
            if isinstance(cur_node, TreeNode):
                cur_sum += cur_node.val
                # cur_node is a left node
                if not isinstance(cur_node.left, TreeNode) and not isinstance(cur_node.right, TreeNode):
                    return cur_sum == targetSum
                return __dfs(cur_node.left, cur_sum) or __dfs(cur_node.right, cur_sum)
            else:  # can't get the target sum till the end leaf
                return False

        return __dfs(root, 0)


def main():
    # Example 1: Output: true
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22

    # Example 2: Output: false
    # root = [1, 2, 3]
    # targetSum = 5

    # Example 3: Output: false
    # root = []
    # targetSum = 0

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.hasPathSum(root_node, targetSum)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
