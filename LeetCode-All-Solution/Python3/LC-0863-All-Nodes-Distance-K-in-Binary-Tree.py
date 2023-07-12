#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0863-All-Nodes-Distance-K-in-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-12
=================================================================="""

import sys
import time
from typing import List, Optional
import collections
# import functools

"""
LeetCode - 0863 - (Medium) - All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Description & Requirement:
    Given the root of a binary tree, the value of a target node target, and an integer k, 
    return an array of the values of all nodes that have a distance k from the target node.

    You can return the answer in any order.

Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
    Output: [7,4,1]
    Explanation: The nodes that are a distance 2 from 
        the target node (with value 5) have values 7, 4, and 1.
Example 2:
    Input: root = [1], target = 1, k = 3
    Output: []

Constraints:
    The number of nodes in the tree is in the range [1, 500].
    0 <= Node.val <= 500
    All the values Node.val are unique.
    target is the value of one of the nodes in the tree.
    0 <= k <= 1000
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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # exception case
        if not isinstance(root, TreeNode):
            return []
        # main method: (DFS)
        return self._distanceK(root, target, k)

    def _distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def __dfs(node: Optional[TreeNode]):
            if isinstance(node, TreeNode):
                if isinstance(node.left, TreeNode):
                    dct[node.left.val].append(node.val)
                    dct[node.val].append(node.left.val)

                if isinstance(node.right, TreeNode):
                    dct[node.right.val].append(node.val)
                    dct[node.val].append(node.right.val)

                __dfs(node.left)
                __dfs(node.right)

        dct = collections.defaultdict(list)
        __dfs(root)

        queue = [target.val]
        visited = {target.val}

        while queue and k:
            queue_new = []
            for i in queue:
                for j in dct[i]:
                    if j not in visited:
                        queue_new.append(j)
                        visited.add(j)
            queue = queue_new
            k -= 1

        return queue


def main():
    # Example 1: Output: [7,4,1]
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    target = 5
    k = 2

    # Example 2: Output: []
    # root = [1]
    # target = 1
    # k = 3

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.distanceK(root_node, target, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
