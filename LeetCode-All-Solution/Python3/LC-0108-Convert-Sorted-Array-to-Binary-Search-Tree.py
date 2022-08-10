#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0108-Convert-Sorted-Array-to-Binary-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-25
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0108 - (Easy) - Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Description:
    Given an integer array nums where the elements are sorted in ascending order, 
    convert it to a height-balanced binary search tree.

    A height-balanced binary tree is a binary tree 
    in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted.
Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
    1 <= nums.length <= 10^4
    -104 <= nums[i] <= 10^4
    nums is sorted in a strictly increasing order.
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return None  # no tree
        if len(nums) == 1:
            return TreeNode(val=nums[0])
        # main method: (similar to binary search, pick the middle number as the val of the current subtree root node)
        return self._sortedArrayToBST(nums)

    def _sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Runtime: 53 ms, faster than 99.73% of Python3 submissions for Convert Sorted Array to Binary Search Tree.
        Memory Usage: 15.6 MB, less than 32.22% of Python3 submissions for Convert Sorted Array to Binary Search Tree.
        """
        assert isinstance(nums, list) and len(nums) > 1

        def __dfs(left_idx: int, right_idx: int) -> Optional[TreeNode]:
            if left_idx > right_idx:
                return None
            mid_idx = (left_idx + right_idx) >> 1
            cur_root_node = TreeNode(nums[mid_idx])
            cur_root_node.left = __dfs(left_idx, mid_idx - 1)
            cur_root_node.right = __dfs(mid_idx + 1, right_idx)
            return cur_root_node

        return __dfs(0, len(nums) - 1)


def main():
    # Example 1: Output: [0,-3,9,-10,null,5]
    nums = [-10, -3, 0, 5, 9]

    # Example 2: Output: [3,1]
    # nums = [1, 3]

    # Example 3: Output: [5,3,8]
    # nums = [3, 5, 8]

    # Example 4: Output: [1,0,2,-1]
    # nums = [-1, 0, 1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sortedArrayToBST(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
