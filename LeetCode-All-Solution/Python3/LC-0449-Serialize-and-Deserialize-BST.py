#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0449-Serialize-and-Deserialize-BST.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-11
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0449 - (Medium) - Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/

Description & Requirement:
    Serialization is converting a data structure or object into a sequence of bits so that 
    it can be stored in a file or memory buffer, or transmitted across a network connection link 
    to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary search tree. 
    There is no restriction on how your serialization/deserialization algorithm should work. 
    You need to ensure that a binary search tree can be serialized to a string, 
    and this string can be deserialized to the original tree structure.

    The encoded string should be as compact as possible.

Example 1:
    Input: root = [2,1,3]
    Output: [2,1,3]
Example 2:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    0 <= Node.val <= 10^4
    The input tree is guaranteed to be a binary search tree.
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


class Codec:
    # if every value is unique

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def _get_binary_tree_pre_order(root_node) -> List[int]:
            val_list = []

            def __dfs(cur_node):
                if isinstance(cur_node, TreeNode):
                    val_list.append(cur_node.val)
                    __dfs(cur_node.left)
                    __dfs(cur_node.right)

            __dfs(root_node)
            return val_list

        def _get_binary_tree_mid_order(root_node) -> List[int]:
            val_list = []

            def __dfs(cur_node):
                if isinstance(cur_node, TreeNode):
                    __dfs(cur_node.left)
                    val_list.append(cur_node.val)
                    __dfs(cur_node.right)

            __dfs(root_node)
            return val_list

        if not isinstance(root, TreeNode):
            return ""
        pre_order = _get_binary_tree_pre_order(root)
        mid_order = _get_binary_tree_mid_order(root)
        assert len(pre_order) == len(mid_order)
        pre_order_str = ",".join([str(item) for item in pre_order])
        mid_order_str = ",".join([str(item) for item in mid_order])
        data = pre_order_str + ";" + mid_order_str
        return data

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def _reconstruct(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            assert isinstance(preorder, list) and isinstance(inorder, list) and len(preorder) == len(inorder)
            if len(preorder) == 0:
                return None  # no tree
            if len(preorder) == 1:
                return TreeNode(val=preorder[0])
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

                # assert cur_root_val in hash_dict
                inorder_root_idx = hash_dict[cur_root_val]

                cur_root.left = __dfs(inorder_left_idx, inorder_root_idx - 1)
                cur_root.right = __dfs(inorder_root_idx + 1, inorder_right_idx)
                return cur_root

            return __dfs(0, len(inorder) - 1)

        if len(data) <= 0:
            return None
        pre_order_str, mid_order_str = data.split(";")
        pre_order = [int(item) for item in pre_order_str.split(",")]
        mid_order = [int(item) for item in mid_order_str.split(",")]
        return _reconstruct(pre_order, mid_order)


def main():
    # Example 1: Output: [2,1,3]
    root = [2, 1, 3]

    # Example 2: Output: []
    # root = []

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    # solution = Solution()
    ser = Codec()
    de_ser = Codec()

    # run & time
    start = time.process_time()
    tree = ser.serialize(root_node)
    ans = de_ser.deserialize(tree)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(tree)
    # print(ans)
    print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
