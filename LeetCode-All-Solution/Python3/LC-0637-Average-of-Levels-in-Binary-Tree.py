#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0637-Average-of-Levels-in-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-02
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0637 - (Easy) - Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Description & Requirement:
    Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
    Answers within 10^{-5} of the actual answer will be accepted.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [3.00000,14.50000,11.00000]
    Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
        Hence return [3, 14.5, 11].
Example 2:
    Input: root = [3,9,20,15,7]
    Output: [3.00000,14.50000,11.00000]

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # exception case
        if not isinstance(root, TreeNode):
            return []
        # main method: (BFS layer traverse)
        return self._averageOfLevels(root)

    def _averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Runtime: 66 ms, faster than 73.91% of Python3 online submissions for Average of Levels in Binary Tree.
        Memory Usage: 16.5 MB, less than 87.46% of Python3 online submissions for Average of Levels in Binary Tree.
        """
        assert isinstance(root, TreeNode)

        res = []
        bfs_queue = [root]

        while len(bfs_queue) > 0:
            new_queue = []
            cur_sum = 0
            cur_cnt = 0
            for node in bfs_queue:
                cur_cnt += 1
                cur_sum += node.val
                if isinstance(node.left, TreeNode):
                    new_queue.append(node.left)
                if isinstance(node.right, TreeNode):
                    new_queue.append(node.right)
            cur_avg = float(cur_sum / cur_cnt) if cur_cnt > 0 else float(0.0)
            res.append(cur_avg)
            bfs_queue = new_queue

        return res


def main():
    # Example 1: Output: [3.00000,14.50000,11.00000]
    root = [3, 9, 20, None, None, 15, 7]

    # Example 2: Output: [3.00000,14.50000,11.00000]
    # root = [3, 9, 20, 15, 7]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.averageOfLevels(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
