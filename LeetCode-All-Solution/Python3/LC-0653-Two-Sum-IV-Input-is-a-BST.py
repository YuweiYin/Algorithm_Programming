#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0653-Two-Sum-IV-Input-is-a-BST.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-10
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0653 - (Easy) - Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Description & Requirement:
    Given the root of a Binary Search Tree and a target number k, 
    return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
    Input: root = [5,3,6,2,4,null,7], k = 9
    Output: true
Example 2:
    Input: root = [5,3,6,2,4,null,7], k = 28
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -10^4 <= Node.val <= 10^4
    root is guaranteed to be a valid binary search tree.
    -10^5 <= k <= 10^5
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # exception case
        if not isinstance(root, TreeNode):
            return False
        # main method: (BST traverse and LC-0001-Two-Sum)
        return self._findTarget(root, k)

    def _findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Runtime: 84 ms, faster than 86.84% of Python3 online submissions for Two Sum IV - Input is a BST.
        Memory Usage: 20.2 MB, less than 18.47% of Python3 online submissions for Two Sum IV - Input is a BST.
        """

        val_list = []

        def __dfs(cur_node: Optional[TreeNode]):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                val_list.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(root)
        if len(val_list) < 2:
            return False

        return len(self._twoSum(val_list, k)) > 0

    def _twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        LC-0001-Two-Sum
        """
        len_nums = len(nums)
        assert len_nums >= 2

        hash_dict = dict({})  # key: num; value: num_idx
        for num_idx, num in enumerate(nums):  # one scan, once found, stop loop
            diff = target - num
            if diff in hash_dict:
                return [hash_dict[diff], num_idx]
            else:
                hash_dict[num] = num_idx  # store it, to be paired for later numbers

        return []  # can't find two_sum pair


def main():
    # Example 1: Output: true
    root = [5, 3, 6, 2, 4, None, 7]
    k = 9

    # Example 2: Output: false
    # root = [5, 3, 6, 2, 4, None, 7]
    # k = 28

    root_node = TreeNode.build_binary_tree_layer(root)
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findTarget(root_node, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
