#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1022-Sum-of-Root-To-Leaf-Binary-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-11
=================================================================="""
# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 1022 - (Easy) - Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

Description & Requirement:
    You are given the root of a binary tree where each node has a value 0 or 1. 
    Each root-to-leaf path represents a binary number starting with the most significant bit.

    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
    For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. 
    Return the sum of these numbers.

    The test cases are generated so that the answer fits in a 32-bits integer.

Example 1:
    Input: root = [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:
    Input: root = [0]
    Output: 0

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    Node.val is 0 or 1.
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0  # no tree
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):  # no children
            return root.val
        # main method: (dfs & backtrack. traverse till every leaf)
        return self._sumRootToLeaf(root)

    def _sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)
        total_val = [0]  # default: sum(total_val) = 0

        def __dfs(cur_node: TreeNode, cur_bin_str: str):
            if not isinstance(cur_node.left, TreeNode) and not isinstance(cur_node.right, TreeNode):  # leaf
                total_val.append(int(cur_bin_str + str(cur_node.val), 2))  # convert to int and then add to total_val
                return
            else:
                if isinstance(cur_node.left, TreeNode):  # left child
                    __dfs(cur_node.left, cur_bin_str + str(cur_node.val))
                if isinstance(cur_node.right, TreeNode):  # right child
                    __dfs(cur_node.right, cur_bin_str + str(cur_node.val))

        start_bin_str = ""
        __dfs(root, start_bin_str)

        return sum(total_val)


def main():
    # Example 1: Output: 22  Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
    root = [1, 0, 1, 0, 1, 0, 1]

    # Example 2: Output: 0
    # root = [0]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sumRootToLeaf(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
