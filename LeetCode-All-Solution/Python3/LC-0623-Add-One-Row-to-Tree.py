#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0623-Add-One-Row-to-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-05
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0623 - (Easy) - Generate a String With Characters That Have Odd Counts
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

Description & Requirement:
    Given the root of a binary tree and two integers val and depth, 
    add a row of nodes with value val at the given depth depth.

    Note that the root node is at depth 1.

    The adding rule is:
        Given the integer depth, for each not null tree node cur at the depth depth - 1, 
            create two tree nodes with value val as cur's left subtree root and right subtree root.
        cur's original left subtree should be the left subtree of the new left subtree root.
        cur's original right subtree should be the right subtree of the new right subtree root.
        If depth == 1 that means there is no depth depth - 1 at all, 
            then create a tree node with value val as the new root of the whole original tree, 
            and the original tree is the new root's left subtree.

Example 1:
    Input: root = [4,2,6,3,1,5], val = 1, depth = 2
    Output: [4,1,1,2,null,null,6,3,1,5]
Example 2:
    Input: root = [4,2,null,3,1], val = 1, depth = 3
    Output: [4,2,null,1,1,3,null,null,1]

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    The depth of the tree is in the range [1, 10^4].
    -100 <= Node.val <= 100
    -10^5 <= val <= 10^5
    1 <= depth <= the depth of tree + 1
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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # exception case
        assert isinstance(val, int) and isinstance(depth, int) and depth >= 1
        # main method: (bfs layer traverse)
        return self._addOneRow(root, val, depth)

    def _addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        assert isinstance(val, int) and isinstance(depth, int) and depth >= 1

        if depth == 1:
            new_root = TreeNode(val=val, left=root)
            return new_root

        bfs_queue = [root]
        cur_depth = 0
        while len(bfs_queue) > 0:
            cur_depth += 1
            if cur_depth == depth - 1:  # the parent layer of all the new nodes
                for node in bfs_queue:
                    new_left = TreeNode(val=val, left=node.left)
                    new_right = TreeNode(val=val, right=node.right)
                    node.left = new_left
                    node.right = new_right
                break
            # bfs
            new_queue = []
            for node in bfs_queue:
                if isinstance(node.left, TreeNode):
                    new_queue.append(node.left)
                if isinstance(node.right, TreeNode):
                    new_queue.append(node.right)
            bfs_queue = new_queue

        return root


def main():
    # Example 1: Output: [4,1,1,2,null,null,6,3,1,5]
    # root = [4, 2, 6, 3, 1, 5]
    # val = 1
    # depth = 2

    # Example 2: Output: [4,2,null,1,1,3,null,null,1]
    root = [4, 2, None, 3, 1]
    val = 1
    depth = 3

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.addOneRow(root_node, val, depth)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(TreeNode.show_binary_tree_pre_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
