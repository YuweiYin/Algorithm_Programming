#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0105-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-25
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0105 - (Medium) - Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Description:
    Given two integer arrays preorder and inorder where preorder is the preorder traversal 
    of a binary tree and inorder is the inorder traversal of the same tree, 
    construct and return the binary tree.

Example 1:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # exception case
        assert isinstance(preorder, list) and isinstance(inorder, list) and len(preorder) == len(inorder)
        if len(preorder) == 0:
            return None  # no tree
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])
        # main method: (preorder[i] is the current root node, all its left subtree nodes are in the left of inorder)
        return self._buildTree(preorder, inorder)

    def _buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Runtime: 68 ms, faster than 93.57% of Python3 online submissions.
        Memory Usage: 18.9 MB, less than 76.63% of Python3 online submissions.
        """
        assert isinstance(preorder, list) and isinstance(inorder, list) and len(preorder) == len(inorder) > 1
        preorder_idx = [0]
        hash_dict = dict({})
        for idx, val in enumerate(inorder):
            hash_dict[val] = idx

        def __dfs(inorder_left_idx: int, inorder_right_idx: int) -> Optional[TreeNode]:
            if inorder_left_idx > inorder_right_idx:
                return None

            cur_root_val = preorder[preorder_idx[0]]
            preorder_idx[0] += 1
            cur_root = TreeNode(val=cur_root_val)

            # locate cur_root_val in inorder list
            # inorder_root_idx = inorder_left_idx
            # while inorder_root_idx <= inorder_right_idx:
            #     if inorder[inorder_root_idx] == cur_root_val:
            #         break
            #     inorder_root_idx += 1
            # assert inorder_root_idx <= inorder_right_idx

            # optimize: hash dict
            # assert cur_root_val in hash_dict
            inorder_root_idx = hash_dict[cur_root_val]

            cur_root.left = __dfs(inorder_left_idx, inorder_root_idx - 1)
            cur_root.right = __dfs(inorder_root_idx + 1, inorder_right_idx)
            return cur_root

        return __dfs(0, len(inorder) - 1)


def main():
    # Example 1: Output: [3,9,20,null,null,15,7]
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    # Example 2: Output: [-1]
    # preorder = [-1]
    # inorder = [-1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.buildTree(preorder, inorder)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(TreeNode.show_binary_tree_pre_order(ans))
    print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
