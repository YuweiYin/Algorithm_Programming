#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0919-Complete-Binary-Tree-Inserter.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-25
=================================================================="""

import sys
import time
from typing import List, Optional
import collections
# import functools

"""
LeetCode - 0919 - (Medium) - Complete Binary Tree Inserter
https://leetcode.com/problems/complete-binary-tree-inserter/

Description & Requirement:
    A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, 
    and all nodes are as far left as possible.

    Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

    Implement the CBTInserter class:
        CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
        int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that 
            the tree remains complete, and returns the value of the parent of the inserted TreeNode.
        TreeNode get_root() Returns the root node of the tree.

Example 1:
    Input
        ["CBTInserter", "insert", "insert", "get_root"]
        [[[1, 2]], [3], [4], []]
    Output
        [null, 1, 2, [1, 2, 3, 4]]
    Explanation
        CBTInserter cBTInserter = new CBTInserter([1, 2]);
        cBTInserter.insert(3);  // return 1
        cBTInserter.insert(4);  // return 2
        cBTInserter.get_root(); // return [1, 2, 3, 4]

Constraints:
    The number of nodes in the tree will be in the range [1, 1000].
    0 <= Node.val <= 5000
    root is a complete binary tree.
    0 <= val <= 5000
    At most 10^4 calls will be made to insert and get_root.
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


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.not_full = collections.deque()

        queue = collections.deque([root])
        while len(queue) > 0:  # bfs, layer-wise traverse
            node = queue.popleft()
            if isinstance(node.left, TreeNode):
                queue.append(node.left)
            if isinstance(node.right, TreeNode):
                queue.append(node.right)
            if not isinstance(node.left, TreeNode) or not isinstance(node.right, TreeNode):  # no left or right child
                self.not_full.append(node)

    def insert(self, val: int) -> int:
        new_child = TreeNode(val)

        node = self.not_full[0]  # the first not_full node

        if not isinstance(node.left, TreeNode):
            node.left = new_child
        else:
            node.right = new_child
            self.not_full.popleft()  # pop this node, because it has two children now

        self.not_full.append(new_child)
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


def main():
    # Example 1: Output: [null, 1, 2, [1, 2, 3, 4]]
    command_list = ["CBTInserter", "insert", "insert", "get_root"]
    param_list = [[[1, 2]], [3], [4], []]

    # init instance
    # solution = Solution()
    root = TreeNode.build_binary_tree_layer(param_list[0][0])
    obj = CBTInserter(root)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "insert":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.insert(param[0]))
            else:
                ans.append("null")
        elif command == "get_root":
            ans.append(obj.get_root().val)
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
