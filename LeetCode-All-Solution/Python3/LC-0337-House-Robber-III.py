#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0337-House-Robber-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-18
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
import functools
# import itertools

"""
LeetCode - 0337 - (Medium) House Robber III
https://leetcode.com/problems/house-robber-iii/

Description & Requirement:
    The thief has found himself a new place for his thievery again. 
    There is only one entrance to this area, called root.

    Besides the root, each house has one and only one parent house. 
    After a tour, the smart thief realized that all houses in this place form a binary tree. 
    It will automatically contact the police if two directly-linked houses were broken into on the same night.

    Given the root of the binary tree, 
    return the maximum amount of money the thief can rob without alerting the police.

Example 1:
    Input: root = [3,2,3,null,3,null,1]
    Output: 7
    Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
    Input: root = [3,4,5,1,3,null,1]
    Output: 9
    Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    0 <= Node.val <= 10^4
"""


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
    def rob(self, root: Optional[TreeNode]) -> int:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (Dynamic Programming)
        return self._rob(root)

    def _rob(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        @functools.lru_cache(maxsize=None)
        def __dfs(node: Optional[TreeNode]) -> (int, int):
            if not isinstance(node, TreeNode):
                return 0, 0

            l_rob, l_not_rob = __dfs(node.left)
            r_rob, r_not_rob = __dfs(node.right)

            rob = l_not_rob + r_not_rob + node.val
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)

            return rob, not_rob

        return max(__dfs(root))


def main():
    # Example 1: Output: 7
    # root = [3, 2, 3, None, 3, None, 1]

    # Example 2: Output: 9
    root = [3, 4, 5, 1, 3, None, 1]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.rob(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
