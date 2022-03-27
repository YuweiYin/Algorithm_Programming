#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0230-Kth-Smallest-Element-in-a-BST.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-26
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0230 - (Medium) - Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Description:
    Given the root of a binary search tree, and an integer k, 
    return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1
Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 10^4
    0 <= Node.val <= 10^4

Follow up:
    If the BST is modified often (i.e., we can do insert and delete operations) 
    and you need to find the kth smallest frequently, how would you optimize?
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # exception case
        assert isinstance(root, TreeNode) and k > 0
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return root.val
        # main method: (1. BST in-order traverse; 2. record & maintain the subtree size of each node)
        return self._kthSmallest(root, k)

    def _kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Runtime: 48 ms, faster than 95.94% of Python3 online submissions for Kth Smallest Element in a BST.
        Memory Usage: 18 MB, less than 49.13% of Python3 online submissions for Kth Smallest Element in a BST.
        """
        assert isinstance(root, TreeNode)

        res = []
        order = [k]

        def __dfs(cur_node: Optional[TreeNode]):
            if order[0] == 0:
                return
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                if order[0] == 0:
                    return
                res.append(cur_node.val)
                order[0] -= 1
                if order[0] == 0:
                    return
                __dfs(cur_node.right)

        __dfs(root)
        return res[-1] if len(res) > 0 else root.val


def main():
    # Example 1: Output: 1
    root = [3, 1, 4, None, 2]
    k = 1

    # Example 2: Output: 3
    # root = [5, 3, 6, 2, 4, None, None, 1]
    # k = 3

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kthSmallest(root_node, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
