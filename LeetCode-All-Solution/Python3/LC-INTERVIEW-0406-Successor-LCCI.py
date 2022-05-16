#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-0406-Successor-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-16
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - INTERVIEW-0406 - (Medium) - Successor LCCI
https://leetcode.cn/problems/successor-lcci/

Description & Requirement:
    Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.

    Return null if there's no "next" node for the given node.

Example 1:
    Input: root = [2,1,3], p = 1
          2
         / \
        1   3
    Output: 2
Example 2:
    Input: root = [5,3,6,2,4,null,null,1], p = 6
              5
             / \
            3   6
           / \
          2   4
         /   
        1
    Output: null
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
        for idx, cur_root in enumerate(node_list):
            if cur_root is not None:
                cur_root_right_index = (idx + 1) << 1
                cur_root_left_index = cur_root_right_index - 1
                if cur_root_left_index < len_node_list:
                    cur_root.left = node_list[cur_root_left_index]
                if cur_root_right_index < len_node_list:
                    cur_root.right = node_list[cur_root_right_index]
        return node_list[0]  # return root_node

    @staticmethod
    def show_binary_tree_pre_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                val_list.append(cur_root.val)
                __dfs(cur_root.left)
                __dfs(cur_root.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_mid_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                __dfs(cur_root.left)
                val_list.append(cur_root.val)
                __dfs(cur_root.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_post_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                __dfs(cur_root.left)
                __dfs(cur_root.right)
                val_list.append(cur_root.val)

        __dfs(root_node)
        return val_list


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode) or not isinstance(p, TreeNode):
            return None
        # main method: (BST traverse)
        return self._inorderSuccessor(root, p)

    def _inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        node_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                __dfs(cur_root.left)
                node_list.append(cur_root)
                __dfs(cur_root.right)

        __dfs(root)

        len_node = len(node_list)
        for idx, node in enumerate(node_list):
            if node == p:
                return node_list[idx + 1] if idx < len_node - 1 else None
        return None

    def _inorderSuccessorTODO(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        assert isinstance(root, TreeNode) and isinstance(p, TreeNode)

        def __traverse(node: Optional[TreeNode], parent: Optional[TreeNode], is_left: bool) -> Optional[TreeNode]:
            if not isinstance(node, TreeNode):
                return None
            if node == p:
                if isinstance(node.right, TreeNode):
                    successor = node.right
                    while isinstance(successor.left, TreeNode):
                        successor = successor.left
                    return successor
                else:
                    if isinstance(parent, TreeNode) and is_left:  # the current node is the left child of its parent
                        return parent
                    else:
                        return None
            else:
                if node.val == p.val:
                    res = __traverse(node.left, node, True)
                    if not isinstance(res, TreeNode):
                        res = __traverse(node.right, node, False)
                elif node.val < p.val:
                    res = __traverse(node.right, node, False)
                else:
                    res = __traverse(node.left, node, True)
                return res

        return __traverse(root, None, False)


def main():
    # Example 1: Output: 2
    #     Input:
    #           2
    #          / \
    #         1   3
    #
    # root = [2, 1, 3]
    # p = 1
    # node_1 = TreeNode(val=1)
    # node_2 = TreeNode(val=2)
    # node_3 = TreeNode(val=3)
    # node_2.left = node_1
    # node_2.right = node_3
    # root_node = node_2
    # p = node_1

    # Example 2: Output: null
    # root = [5, 3, 6, 2, 4, None, None, 1]
    # p = 6
    node_1 = TreeNode(val=1)
    node_2 = TreeNode(val=2)
    node_3 = TreeNode(val=3)
    node_4 = TreeNode(val=4)
    node_5 = TreeNode(val=5)
    node_6 = TreeNode(val=6)
    node_5.left = node_3
    node_5.right = node_6
    node_3.left = node_2
    node_3.right = node_4
    node_2.left = node_1
    root_node = node_5
    p = node_6

    # root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.inorderSuccessor(root_node, p)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    if isinstance(ans, TreeNode):
        print(ans.val)
    else:
        print("null")

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
