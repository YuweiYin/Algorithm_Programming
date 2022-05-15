#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1302-Deepest-Leaves-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-15
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 1302 - (Medium) - Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/

Description & Requirement:
    Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15
Example 2:
    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 19

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    1 <= Node.val <= 100
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0
        # main method: (DFS)
        return self._deepestLeavesSum(root)

    def _deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)
        depth_val = []

        def _dfs(node: Optional[TreeNode], depth: int) -> None:
            if not isinstance(node, TreeNode):
                return
            if not isinstance(node.left, TreeNode) and not isinstance(node.right, TreeNode):  # node is a leaf
                depth_val.append((depth, node.val))
            else:
                if isinstance(node.left, TreeNode):
                    _dfs(node.left, depth + 1)
                if isinstance(node.right, TreeNode):
                    _dfs(node.right, depth + 1)

        _dfs(root, 1)
        if len(depth_val) == 0:
            return 0
        max_depth = 0
        for d, v in depth_val:  # find the max depth
            if d > max_depth:
                max_depth = d
        res = 0
        for d, v in depth_val:  # sum up the vals with max depth
            if d == max_depth:
                res += v
        return res


def main():
    # Example 1: Output: 15
    root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]

    # Example 2: Output: 19
    # root = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.deepestLeavesSum(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
