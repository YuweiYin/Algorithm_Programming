#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0669-Trim-a-Binary-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-15
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0669 - (Medium) - Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/

Description & Requirement:
    Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
    trim the tree so that all its elements lies in [low, high]. 
    Trimming the tree should not change the relative structure of the elements that will remain in the tree 
    (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

    Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Example 1:
    Input: root = [1,0,2], low = 1, high = 2
    Output: [1,null,2]
Example 2:
    Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
    Output: [3,2,null,1]

Constraints:
    The number of nodes in the tree in the range [1, 10^4].
    0 <= Node.val <= 10^4
    The value of each node in the tree is unique.
    root is guaranteed to be a valid binary search tree.
    0 <= low <= high <= 10^4
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        # main method: (xxx)
        return self._trimBST(root, low, high)

    def _trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        Runtime: 49 ms, faster than 89.65% of Python3 online submissions for Trim a Binary Search Tree.
        Memory Usage: 18.1 MB, less than 11.70% of Python3 online submissions for Trim a Binary Search Tree.
        """
        assert isinstance(root, TreeNode)
        pseudo_root = TreeNode(right=root)

        def __dfs(cur_node: Optional[TreeNode], parent_node: Optional[TreeNode], is_left: bool) -> None:
            if low <= cur_node.val <= high:
                # do link
                if parent_node == pseudo_root:
                    pseudo_root.right = cur_node
                else:
                    if is_left:
                        parent_node.left = cur_node
                    else:
                        parent_node.right = cur_node
                # explore more
                if isinstance(cur_node.left, TreeNode):
                    __dfs(cur_node.left, cur_node, True)
                if isinstance(cur_node.right, TreeNode):
                    __dfs(cur_node.right, cur_node, False)
            elif cur_node.val < low:  # cur_node.val < low, so the left subtree of cur_node is less than low
                parent_node.left = None
                if isinstance(cur_node.right, TreeNode):
                    __dfs(cur_node.right, parent_node, is_left)  # link parent_node to cur_node.right
            else:  # cur_node.val > high, so the right subtree of cur_node is greater than high
                parent_node.right = None
                if isinstance(cur_node.left, TreeNode):
                    __dfs(cur_node.left, parent_node, is_left)  # link parent_node to cur_node.left

        __dfs(root, pseudo_root, False)
        return pseudo_root.right


def main():
    # Example 1: Output: [1,null,2]
    root = [1, 0, 2]
    low = 1
    high = 2

    # Example 2: Output: [3,2,null,1]
    # root = [3, 0, 4, None, 2, None, None, None, None, 1]
    # low = 1
    # high = 3

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.trimBST(root_node, low, high)
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
