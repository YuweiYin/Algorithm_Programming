#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0129-Sum-Root-to-Leaf-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-14
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 2383 - (Medium) - Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/

Description & Requirement:
    You are given the root of a binary tree containing digits from 0 to 9 only.

    Each root-to-leaf path in the tree represents a number.

        For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

    Return the total sum of all root-to-leaf numbers. 
    Test cases are generated so that the answer will fit in a 32-bit integer.

    A leaf node is a node with no children.

Example 1:
    Input: root = [1,2,3]
    Output: 25
    Explanation:
        The root-to-leaf path 1->2 represents the number 12.
        The root-to-leaf path 1->3 represents the number 13.
        Therefore, sum = 12 + 13 = 25.
Example 2:
    Input: root = [4,9,0,5,1]
    Output: 1026
    Explanation:
        The root-to-leaf path 4->9->5 represents the number 495.
        The root-to-leaf path 4->9->1 represents the number 491.
        The root-to-leaf path 4->0 represents the number 40.
        Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (DFS)
        return self._sumNumbers(root)

    def _sumNumbers(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        def __dfs(root: TreeNode, prev_sum: int) -> int:
            if not root:
                return 0
            cur_sum = prev_sum * 10 + root.val
            if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
                return cur_sum
            else:
                return __dfs(root.left, cur_sum) + __dfs(root.right, cur_sum)

        return __dfs(root, 0)


def main():
    # Example 1: Output: 25
    # root = [1, 2, 3]

    # Example 2: Output: 1026
    root = [4, 9, 0, 5, 1]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.sumNumbers(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
