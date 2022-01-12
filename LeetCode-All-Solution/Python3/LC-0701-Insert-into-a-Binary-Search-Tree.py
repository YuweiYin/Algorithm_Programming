#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0701-Insert-into-a-Binary-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-12
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0701 - (Medium) - Insert into a Binary Search Tree
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Description & Requirement:
    You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
    Return the root node of the BST after the insertion. 
    It is guaranteed that the new value does not exist in the original BST.

    Notice that there may exist multiple valid ways for the insertion, 
    as long as the tree remains a BST after insertion. You can return any of them.

Example 1:
    Input: root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]
Example 2:
    Input: root = [40,20,60,10,30,50,70], val = 25
    Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:
    Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
    Output: [4,2,7,1,3,5]

Constraints:
    The number of nodes in the tree will be in the range [0, 10^4].
    -10^8 <= Node.val <= 10^8
    All the values Node.val are unique.
    -10^8 <= val <= 10^8
    It's guaranteed that val does not exist in the original BST.
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            new_root = TreeNode(val=val)
            return new_root  # new tree new root
        # main method: (traverse both trees at the same time)
        return self._insertIntoBST(root, val)

    def _insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def __dfs(node: Optional[TreeNode]):  # BST traverse
            assert isinstance(node, TreeNode)

            if val <= node.val:  # go left
                # left child
                if isinstance(node.left, TreeNode):
                    __dfs(node.left)
                else:  # left child is None, can be inserted there
                    new_node = TreeNode(val=val)
                    node.left = new_node
                    return
            else:  # go right
                # right child
                if isinstance(node.right, TreeNode):
                    __dfs(node.right)
                else:  # right child is None, can be inserted there
                    new_node = TreeNode(val=val)
                    node.right = new_node
                    return

        __dfs(root)
        return root


def main():
    # Example 1: Output: [4,2,7,1,3,5]
    # root = [4, 2, 7, 1, 3]
    # val = 5

    # Example 2: Output: [40,20,60,10,30,50,70,null,null,25]
    # root = [40, 20, 60, 10, 30, 50, 70]
    # val = 25

    # Example 3: Output: [4,2,7,1,3,5]
    root = [4, 2, 7, 1, 3, None, None, None, None, None, None]
    val = 5

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.insertIntoBST(root_node, val)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
