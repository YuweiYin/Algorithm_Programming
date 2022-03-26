#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0199-Binary-Tree-Right-Side-View.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-26
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0199 - (Medium) - Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Description:
    Given the root of a binary tree, imagine yourself standing on the right side of it, 
    return the values of the nodes you can see ordered from top to bottom.

Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
Example 2:
    Input: root = [1,null,3]
    Output: [1,3]
Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # exception case
        if not isinstance(root, TreeNode):
            return []  # no tree
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return [root.val]
        # main method: (bfs layer-wise traverse)
        return self._rightSideView(root)

    def _rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Runtime: 36 ms, faster than 83.08% of Python3 online submissions for Binary Tree Right Side View.
        Memory Usage: 14 MB, less than 30.07% of Python3 online submissions for Binary Tree Right Side View.
        """
        assert isinstance(root, TreeNode)

        res = []
        bfs_queue = [root]  # deal with all nodes in bfs_queue at a time
        while len(bfs_queue) > 0:
            new_bfs_queue = []
            cur_layer = []
            for cur_node in bfs_queue:
                cur_layer.append(cur_node.val)
                if isinstance(cur_node.left, TreeNode):
                    new_bfs_queue.append(cur_node.left)
                if isinstance(cur_node.right, TreeNode):
                    new_bfs_queue.append(cur_node.right)
            if len(cur_layer) > 0:
                res.append(cur_layer[-1])  # only append the last item in this layer
            bfs_queue = new_bfs_queue

        return res


def main():
    # Example 1: Output: [1,3,4]
    root = [1, 2, 3, None, 5, None, 4]

    # Example 2: Output: [1,3]
    # root = [1, None, 3]

    # Example 3: Output: []
    # root = []

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rightSideView(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
