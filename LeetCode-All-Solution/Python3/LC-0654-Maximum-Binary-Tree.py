#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0654-Maximum-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-20
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0654 - (Easy) - Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/

Description & Requirement:
    You are given an integer array nums with no duplicates. 
    A maximum binary tree can be built recursively from nums using the following algorithm:
        Create a root node whose value is the maximum value in nums.
        Recursively build the left subtree on the subarray prefix to the left of the maximum value.
        Recursively build the right subtree on the subarray suffix to the right of the maximum value.

    Return the maximum binary tree built from nums.

Example 1:
    Input: nums = [3,2,1,6,0,5]
    Output: [6,3,5,null,2,0,null,null,1]
    Explanation: The recursive calls are as follow:
        - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
            - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
                - Empty array, so no child.
                - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
                    - Empty array, so no child.
                    - Only one element, so child is a node with value 1.
            - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
                - Only one element, so child is a node with value 0.
                - Empty array, so no child.
Example 2:
    Input: nums = [3,2,1]
    Output: [3,null,2,null,1]

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000
    All integers in nums are unique.
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (recursively construct the binary tree)
        return self._constructMaximumBinaryTree(nums)

    def _constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        assert isinstance(nums, list) and len(nums) >= 1

        def __recur(cur_list: List[int]) -> Optional[TreeNode]:
            cur_max = max(cur_list)
            max_idx = cur_list.index(cur_max)
            left_list = cur_list[0: max_idx]
            right_list = cur_list[max_idx + 1:]

            cur_root = TreeNode(val=cur_max)
            if len(left_list) > 0:
                cur_root.left = __recur(left_list)
            if len(right_list) > 0:
                cur_root.right = __recur(right_list)
            return cur_root

        return __recur(nums)


def main():
    # Example 1: Output: [6,3,5,null,2,0,null,null,1]
    # nums = [3, 2, 1, 6, 0, 5]

    # Example 2: Output: [3,null,2,null,null,null,1]
    nums = [3, 2, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.constructMaximumBinaryTree(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
