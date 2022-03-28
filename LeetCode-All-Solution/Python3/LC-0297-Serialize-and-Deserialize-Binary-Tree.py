#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0297-Serialize-and-Deserialize-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-28
=================================================================="""

import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0297 - (Hard) - Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Description:
    Serialization is the process of converting a data structure or object into a sequence of bits 
    so that it can be stored in a file or memory buffer, or transmitted across a network connection link 
    to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. 
    There is no restriction on how your serialization/deserialization algorithm should work. 
    https://support.leetcode.com/hc/en-us/sections/360002895993-Technical-Questions
    You just need to ensure that a binary tree can be serialized to a string 
    and this string can be deserialized to the original tree structure.

    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
    You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]
Example 2:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -1000 <= Node.val <= 1000
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


class CodecUnique:
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

        pre_order_str, mid_order_str = data.split(";")
        pre_order = [int(item) for item in pre_order_str.split(",")]
        mid_order = [int(item) for item in mid_order_str.split(",")]
        return _reconstruct(pre_order, mid_order)


class CodecSlow:
    # layer traverse and reconstruct

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not isinstance(root, TreeNode):
            return ""

        res = []
        cur_layer = [root]
        while len(cur_layer) > 0:
            has_child = False
            new_layer = []
            # val_list = []
            for node in cur_layer:
                if isinstance(node, TreeNode):
                    # val_list.append(str(node.val))
                    res.append(str(node.val))
                    if isinstance(node.left, TreeNode) or isinstance(node.right, TreeNode):
                        has_child = True
                    new_layer.append(node.left)
                    new_layer.append(node.right)
                else:
                    # val_list.append("null")
                    res.append("null")
                    new_layer.append(None)
                    new_layer.append(None)
            # res.append(val_list)
            cur_layer = new_layer
            if not has_child:
                break

        data = ",".join(res)
        return data

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def _reconstruct_binary_tree_layer(val_list: List[int]):
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

        if len(data) <= 0:
            return None

        data_val_list = []
        for item in data.split(","):
            if item == "null":
                data_val_list.append(None)
            else:
                data_val_list.append(int(item))
        return _reconstruct_binary_tree_layer(data_val_list)


class Codec:
    # pre-order traverse and reconstruct
    # Runtime: 144 ms, faster than 86.57% of Python3 online submissions for Serialize and Deserialize Binary Tree.
    # Memory Usage: 20.3 MB, less than 64.00% of Python3 online submissions for Serialize and Deserialize Binary Tree.

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = [""]

        def __dfs(cur_node: Optional[TreeNode]):
            if isinstance(cur_node, TreeNode):
                res[0] += str(cur_node.val) + ","
                __dfs(cur_node.left)
                __dfs(cur_node.right)
            else:
                res[0] += "null,"

        __dfs(root)
        if res[0][-1] == ",":  # get rid of the trailing ","
            res[0] = res[0][:-1]
        return res[0]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_deque = collections.deque(data.split(","))

        def __dfs() -> Optional[TreeNode]:
            if len(data_deque) <= 0:
                return None
            cur_node_str = data_deque.popleft()
            if cur_node_str == "null":
                return None

            cur_node = TreeNode(val=int(cur_node_str))
            cur_node.left = __dfs()
            cur_node.right = __dfs()
            return cur_node

        return __dfs()


def main():
    # Example 1: Output: [1,2,3,null,null,4,5]
    root = [1, 2, 3, None, None, 4, 5]

    # Example 2: Output: []
    # root = []

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    # solution = Solution()

    # run & time
    start = time.process_time()
    ser = Codec()
    de_ser = Codec()
    ans = de_ser.deserialize(ser.serialize(root_node))
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
