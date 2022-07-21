#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0814-Binary-Tree-Pruning.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-21
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0814 - (Medium) - Binary Tree Pruning
https://leetcode.com/problems/binary-tree-pruning/

Description & Requirement:
    Given the root of a binary tree, return the same tree where every subtree (of the given tree) 
        not containing a 1 has been removed.

    A subtree of a node node is node plus every node that is a descendant of node.

Example 1:
    Input: root = [1,null,0,0,1]
    Output: [1,null,0,null,1]
    Explanation: 
        Only the red nodes satisfy the property "every subtree not containing a 1".
        The diagram on the right represents the answer.
Example 2:
    Input: root = [1,0,1,0,0,0,1]
    Output: [1,null,1,null,1]
Example 3:
    Input: root = [1,1,0,1,1,0,1,0]
    Output: [1,1,0,1,1,null,1]

Constraints:
    The number of nodes in the tree is in the range [1, 200].
    Node.val is either 0 or 1.
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        # main method: (DFS: if the sum of all values in a subtree is 0, it should be removed.)
        return self._pruneTree(root)

    def _pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        assert isinstance(root, TreeNode)

        def __dfs(cur_node: Optional[TreeNode]) -> int:
            # return the sum of all values in the subtree (of the current node)
            if isinstance(cur_node, TreeNode):
                left_res = __dfs(cur_node.left)
                if left_res == 0:
                    cur_node.left = None
                right_res = __dfs(cur_node.right)
                if right_res == 0:
                    cur_node.right = None
                return cur_node.val + left_res + right_res
            else:  # None
                return 0

        root_res = __dfs(root)
        return None if root_res == 0 else root


def main():
    # Example 1: Output: [1,null,0,null,1]
    # root = [1, None, 0, 0, 1]

    # Example 2: Output: [1,null,1,null,1]
    # root = [1, 0, 1, 0, 0, 0, 1]

    # Example 3: Output: [1,1,0,1,1,null,1]
    root = [1, 1, 0, 1, 1, 0, 1, 0]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pruneTree(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    TreeNode.show_binary_tree_pre_order(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
