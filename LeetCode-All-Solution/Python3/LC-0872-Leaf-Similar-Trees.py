#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0872-Leaf-Similar-Trees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-08
=================================================================="""

import sys
import time
from typing import List, Optional
import collections
# import functools

"""
LeetCode - 0872 - (Easy) - Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/

Description & Requirement:
    Consider all the leaves of a binary tree, from left to right order, 
    the values of those leaves form a leaf value sequence.

    Two binary trees are considered leaf-similar if their leaf value sequence is the same.

    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true
Example 2:
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false

Constraints:
    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # exception case
        # if not isinstance(root1, TreeNode):
        #     return not isinstance(root2, TreeNode)
        # if not isinstance(root2, TreeNode):
        #     return not isinstance(root1, TreeNode)
        # main method: (DFS pre-order traverse)
        return self._leafSimilar(root1, root2)

    def _leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # assert isinstance(root1, TreeNode) and isinstance(root2, TreeNode)

        def __dfs(node: Optional[TreeNode]):
            if not isinstance(node.left, TreeNode) and not isinstance(node.right, TreeNode):
                yield node.val
            else:
                if isinstance(node.left, TreeNode):
                    yield from __dfs(node.left)
                if isinstance(node.right, TreeNode):
                    yield from __dfs(node.right)

        seq1 = list(__dfs(root1)) if isinstance(root1, TreeNode) else []
        seq2 = list(__dfs(root2)) if isinstance(root2, TreeNode) else []

        return seq1 == seq2


def main():
    # Example 1: Output: true
    root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

    # Example 2: Output: false
    # root1 = [1, 2, 3]
    # root2 = [1, 3, 2]

    root_node_1 = TreeNode.build_binary_tree_layer(root1)
    root_node_2 = TreeNode.build_binary_tree_layer(root2)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.leafSimilar(root_node_1, root_node_2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
