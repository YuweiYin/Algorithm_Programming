#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0099-Recover-Binary-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-19
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0099 - (Medium) - Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

Description & Requirement:
    You are given the root of a binary search tree (BST), 
    where the values of exactly two nodes of the tree were swapped by mistake. 
    Recover the tree without changing its structure.

Example 1:
    Input: root = [1,3,null,null,2]
    Output: [3,1,null,null,2]
    Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:
    Input: root = [3,1,4,null,null,2]
    Output: [2,1,4,null,null,3]
    Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:
    The number of nodes in the tree is in the range [2, 1000].
    -2^31 <= Node.val <= 2^31 - 1

Follow up:
    A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # exception case
        if not isinstance(root, TreeNode):
            return
        # main method: (Morris traverse: Time O(n), Space O(1))
        self._recoverTree(root)

    def _recoverTree(self, root: Optional[TreeNode]) -> None:
        # x: error node 1; y: error not 2; pre is a node whose val should be less than cur_root.val
        x, y, pre, predecessor = None, None, None, None
        cur_root = root

        while isinstance(cur_root, TreeNode):
            if isinstance(cur_root.left, TreeNode):  # has left child
                # find the predecessor node
                predecessor = cur_root.left
                while isinstance(predecessor.right, TreeNode) and predecessor.right != cur_root:
                    predecessor = predecessor.right

                # if predecessor doesn't have the right child, set its right child as cur_root
                if not isinstance(predecessor.right, TreeNode):
                    predecessor.right = cur_root
                    cur_root = cur_root.left  # next loop, start from cur_root.left
                else:
                    # if predecessor has the right child, it must be the extra link,
                    # cut this link and check the right subtree
                    if isinstance(pre, TreeNode) and cur_root.val < pre.val:  # val error, record x and y
                        y = cur_root
                        if not isinstance(x, TreeNode):
                            x = pre
                    pre = cur_root

                    predecessor.right = None
                    cur_root = cur_root.right
            else:  # check the right child
                if isinstance(pre, TreeNode) and cur_root.val < pre.val:  # val error, record x and y
                    y = cur_root
                    if not isinstance(x, TreeNode):
                        x = pre
                pre = cur_root
                cur_root = cur_root.right

        if isinstance(x, TreeNode) and isinstance(y, TreeNode):
            x.val, y.val = y.val, x.val


def main():
    # Example 1: Output: [3,1,null,null,2]
    # root = [1, 3, None, None, 2]

    # Example 2: Output: [2,1,4,null,null,3]
    root = [3, 1, 4, None, None, 2]

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.recoverTree(root_node)
    ans = root_node
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    if isinstance(ans, TreeNode):
        print(TreeNode.show_binary_tree_mid_order(ans))
    else:
        print("null")

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
