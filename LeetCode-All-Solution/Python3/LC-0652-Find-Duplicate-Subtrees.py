#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0652-Find-Duplicate-Subtrees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-05
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0652 - (Medium) - Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/

Description & Requirement:
    Given the root of a binary tree, return all duplicate subtrees.

    For each kind of duplicate subtrees, you only need to return the root node of any one of them.

    Two trees are duplicate if they have the same structure with the same node values.

Example 1:
    Input: root = [1,2,3,4,null,2,4,null,null,4]
    Output: [[2,4],[4]]
Example 2:
    Input: root = [2,1,1]
    Output: [[1]]
Example 3:
    Input: root = [2,2,2,3,null,3,null]
    Output: [[2,3],[3]]

Constraints:
    The number of the nodes in the tree will be in the range [1, 10^4]
    -200 <= Node.val <= 200
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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # exception case
        if not isinstance(root, TreeNode):
            return []
        # main method: (DFS, tag each node and serialize all trees)
        return self._findDuplicateSubtrees(root)

    def _findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        assert isinstance(root, TreeNode)

        idx = [0]
        visited = dict()
        dup_tree = set()

        def __dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            cur_subtree = (node.val, __dfs(node.left), __dfs(node.right))
            if cur_subtree in visited:
                (tree, index) = visited[cur_subtree]
                dup_tree.add(tree)
                return index
            else:
                idx[0] += 1
                visited[cur_subtree] = (node, idx[0])
                return idx[0]

        __dfs(root)
        return list(dup_tree)


def main():
    # Example 1: Output: [[2,4],[4]]
    # root = [1, 2, 3, 4, None, 2, 4, None, None, None, None, 4]

    # Example 2: Output: [[1]]
    root = [2, 1, 1]

    # Example 3: Output: [[2,3],[3]]
    # root = [2, 2, 2, 3, None, 3, None]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findDuplicateSubtrees(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print([node.val for node in ans])

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
