#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0998-Maximum-Binary-Tree-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-30
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0998 - (Medium) - Maximum Binary Tree II
https://leetcode.com/problems/maximum-binary-tree-ii/

Description & Requirement:
    A maximum tree is a tree where every node has a value greater than any other value in its subtree.

    You are given the root of a maximum binary tree and an integer val.

    Just as in the [previous problem](https://leetcode.com/problems/maximum-binary-tree/), 
    the given tree was constructed from a list a (root = Construct(a)) recursively 
    with the following Construct(a) routine:
        If a is empty, return null.
        Otherwise, let a[i] be the largest element of a. Create a root node with the value a[i].
        The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]).
        The right child of root will be Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]).
        Return root.

    Note that we were not given a directly, only a root node root = Construct(a).

    Suppose b is a copy of a with the value val appended to it. It is guaranteed that b has unique values.

    Return Construct(b).

Example 1:
    Input: root = [4,1,3,null,null,2], val = 5
    Output: [5,4,null,1,3,null,null,2]
    Explanation: a = [1,4,2,3], b = [1,4,2,3,5]
Example 2:
    Input: root = [5,2,4,null,1], val = 3
    Output: [5,2,4,null,1,null,3]
    Explanation: a = [2,1,5,4], b = [2,1,5,4,3]
Example 3:
    Input: root = [5,2,3,null,1], val = 4
    Output: [5,2,4,null,1,3]
    Explanation: a = [2,1,5,3], b = [2,1,5,3,4]

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    1 <= Node.val <= 100
    All the values of the tree are unique.
    1 <= val <= 100
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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        assert isinstance(val, int) and val >= 1
        # main method: (recursively find a place to insert)
        return self._insertIntoMaxTree(root, val)

    def _insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        assert isinstance(root, TreeNode)
        assert isinstance(val, int) and val >= 1

        parent = None
        cur_node = root

        while isinstance(cur_node, TreeNode):
            if val > cur_node.val:
                if not parent:
                    return TreeNode(val, left=root)
                new_node = TreeNode(val, cur_node, None)
                parent.right = new_node
                return root
            else:
                parent = cur_node
                cur_node = cur_node.right

        parent.right = TreeNode(val)

        return root


def main():
    # Example 1: Output: [5,4,null,1,3,null,null,2]
    root = [4, 1, 3, None, None, 2]
    val = 5

    # Example 2: Output: [5,2,4,null,1,null,3]
    # root = [5, 2, 4, None, 1]
    # val = 3

    # Example 3: Output: [5,2,4,null,1,3]
    # root = [5, 2, 3, None, 1]
    # val = 4

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.insertIntoMaxTree(root_node, val)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
