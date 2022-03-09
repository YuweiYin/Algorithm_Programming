#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0700-Search-in-a-Binary-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-09
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0700 - (Easy) - Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/

Description & Requirement:
    You are given the root of a binary search tree (BST) and an integer val.

    Find the node in the BST that the node's value equals val and 
    return the subtree rooted with that node. 
    If such a node does not exist, return null.

Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]
Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output: []

Constraints:
    The number of nodes in the tree is in the range [1, 5000].
    1 <= Node.val <= 10^7
    root is a binary search tree.
    1 <= val <= 10^7
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        # main method: (BST traverse)
        return self._searchBST(root, val)

    def _searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def __dfs(node: Optional[TreeNode]):  # BST traverse
            if not isinstance(node, TreeNode):
                return None

            if val == node.val:  # val matched
                return node
            elif val < node.val:  # go left
                return __dfs(node.left)
            else:  # go right
                return __dfs(node.right)

        return __dfs(root)


def main():
    # Example 1: Output: [2,1,3]
    root = [4, 2, 7, 1, 3]
    val = 2

    # Example 2: Output: []
    # root = [4, 2, 7, 1, 3]
    # val = 5

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.searchBST(root_node, val)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
