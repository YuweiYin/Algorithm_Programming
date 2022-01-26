#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1305-All-Elements-in-Two-Binary-Search-Trees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-26
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 1305 - (Medium) - All Elements in Two Binary Search Trees
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

Description & Requirement:
    Given two binary search trees root1 and root2, 
    return a list containing all the integers from both trees sorted in ascending order.

Example 1:
    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]
Example 2:
    Input: root1 = [1,null,8], root2 = [8,1]
    Output: [1,1,8,8]

Constraints:
    The number of nodes in each tree is in the range [0, 5000].
    -10^5 <= Node.val <= 10^5
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # exception case
        # main method: (BST traverse both trees to get two sorted lists, then combine these two lists)
        return self._getAllElements(root1, root2)

    def _getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def __binary_tree_mid_order(root_node) -> List[int]:  # mid-order traverse
            val_list = []

            def __dfs(cur_node):
                if isinstance(cur_node, TreeNode):
                    __dfs(cur_node.left)
                    val_list.append(cur_node.val)
                    __dfs(cur_node.right)

            __dfs(root_node)
            return val_list

        val_list_1 = __binary_tree_mid_order(root1)
        val_list_2 = __binary_tree_mid_order(root2)

        res_list = []
        cursor_1 = 0
        cursor_2 = 0
        while cursor_1 < len(val_list_1) and cursor_2 < len(val_list_2):
            if val_list_1[cursor_1] <= val_list_2[cursor_2]:  # put in the small one
                res_list.append(val_list_1[cursor_1])
                cursor_1 += 1
            else:
                res_list.append(val_list_2[cursor_2])
                cursor_2 += 1

        # assert cursor_1 == len(val_list_1) or cursor_2 == len(val_list_2)
        # deal with the rest items
        while cursor_1 < len(val_list_1):
            res_list.append(val_list_1[cursor_1])
            cursor_1 += 1
        while cursor_2 < len(val_list_2):
            res_list.append(val_list_2[cursor_2])
            cursor_2 += 1

        return res_list


def main():
    # Example 1: Output: [0,1,1,2,3,4]
    root1 = [2, 1, 4]
    root2 = [1, 0, 3]

    # Example 2: Output: [1,1,8,8]
    # root1 = [1, None, 8]
    # root2 = [8, 1]

    root_node1 = TreeNode.build_binary_tree_layer(root1)
    print(TreeNode.show_binary_tree_mid_order(root_node1))  # mid traverse BST to get ordered list

    root_node2 = TreeNode.build_binary_tree_layer(root2)
    print(TreeNode.show_binary_tree_mid_order(root_node2))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getAllElements(root_node1, root_node2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)
    # print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
