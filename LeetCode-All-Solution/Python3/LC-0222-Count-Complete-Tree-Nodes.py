#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0222-Count-Complete-Tree-Nodes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-15
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0222 - (Medium) - Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/

Description & Requirement:
    Given the root of a complete binary tree, return the number of the nodes in the tree.

    According to [Wikipedia](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees),
    every level, except possibly the last, is completely filled in a complete binary tree, 
    and all nodes in the last level are as far left as possible. 
    It can have between 1 and 2h nodes inclusive at the last level h.

    Design an algorithm that runs in less than O(n) time complexity.

Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: 6
Example 2:
    Input: root = []
    Output: 0
Example 3:
    Input: root = [1]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [0, 5 * 104].
    0 <= Node.val <= 5 * 10^4
    The tree is guaranteed to be complete.
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0
        # main method: (binary search & bit manipulation)
        return self._countNodes(root)

    def _countNodes(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        level = 0
        ptr = root
        while isinstance(ptr.left, TreeNode):
            level += 1
            ptr = ptr.left

        def __exists(level: int, k: int) -> bool:
            bits = 1 << (level - 1)
            _ptr = root
            while isinstance(_ptr, TreeNode) and bits > 0:
                if not (bits & k):
                    _ptr = _ptr.left
                else:
                    _ptr = _ptr.right
                bits >>= 1
            return isinstance(_ptr, TreeNode)

        low = 1 << level
        high = (1 << (level + 1)) - 1
        while low < high:
            mid = ((high - low + 1) >> 1) + low
            if __exists(level, mid):
                low = mid
            else:
                high = mid - 1

        return low


def main():
    # Example 1: Output: 6
    root = [1, 2, 3, 4, 5, 6]

    # Example 2: Output: 0
    # root = []

    # Example 3: Output: 1
    # root = [1]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countNodes(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
