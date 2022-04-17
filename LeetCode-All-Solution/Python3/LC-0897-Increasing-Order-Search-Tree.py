#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0897-Increasing-Order-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-17
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0897 - (Easy) - Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/

Description & Requirement:
    Given the root of a binary search tree, rearrange the tree in in-order 
    so that the leftmost node in the tree is now the root of the tree, 
    and every node has no left child and only one right child.

Example 1:
    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:
    Input: root = [5,1,7]
    Output: [1,null,5,null,7]

Constraints:
    The number of nodes in the given tree will be in the range [1, 100].
    0 <= Node.val <= 1000
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
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        # main method: (BST in-order traverse)
        return self._increasingBST(root)

    def _increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 31 ms, faster than 90.53% of Python3 online submissions for Increasing Order Search Tree.
        Memory Usage: 14 MB, less than 13.79% of Python3 online submissions for Increasing Order Search Tree.
        """
        assert isinstance(root, TreeNode)

        node_list = []

        def __dfs(cur_node) -> None:  # in-order traverse
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                node_list.append(cur_node)
                __dfs(cur_node.right)

        __dfs(root)

        if len(node_list) == 0:
            return None

        # modify the left/right links
        for idx in range(1, len(node_list)):
            node_list[idx - 1].left = None
            node_list[idx - 1].right = node_list[idx]
        node_list[-1].left = None
        node_list[-1].right = None

        return node_list[0]


def main():
    # Example 1: Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
    root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, None, None, 7, 9]

    # Example 2: Output: [1,null,5,null,7]
    # root = [5, 1, 7]

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.increasingBST(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    if isinstance(ans, TreeNode):
        print(TreeNode.show_binary_tree_mid_order(ans))
    else:
        print("null")

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
