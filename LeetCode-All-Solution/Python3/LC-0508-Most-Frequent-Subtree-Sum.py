#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0508-Most-Frequent-Subtree-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-19
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0508 - (Medium) - Most Frequent Subtree Sum
https://leetcode.com/problems/most-frequent-subtree-sum/

Description & Requirement:
    Given the root of a binary tree, return the most frequent subtree sum. 
    If there is a tie, return all the values with the highest frequency in any order.

    The subtree sum of a node is defined as the sum of all the node values 
    formed by the subtree rooted at that node (including the node itself).

Example 1:
    Input: root = [5,2,-3]
    Output: [2,-3,4]
Example 2:
    Input: root = [5,2,-5]
    Output: [2]

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -10^5 <= Node.val <= 10^5
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
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # exception case
        if not isinstance(root, TreeNode):
            return []
        # main method: (DFS calculate all subtree sum)
        return self._findFrequentTreeSum(root)

    def _findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        Runtime: 44 ms, faster than 98.62% of Python3 online submissions for Most Frequent Subtree Sum.
        Memory Usage: 17.4 MB, less than 37.60% of Python3 online submissions for Most Frequent Subtree Sum.
        """
        assert isinstance(root, TreeNode)
        counter = dict({})

        def __dfs(node: Optional[TreeNode]) -> int:
            if isinstance(node, TreeNode):
                cur_sum = node.val + __dfs(node.left) + __dfs(node.right)
                if cur_sum not in counter:
                    counter[cur_sum] = 1
                else:
                    counter[cur_sum] += 1
                return cur_sum
            else:
                return 0

        __dfs(root)

        counter_val = list(counter.values())
        if len(counter_val) == 0:
            return []
        counter_val.sort(reverse=True)

        res = []
        most_freq = counter_val[0]
        for k, v in counter.items():
            if v == most_freq:
                res.append(k)

        return res


def main():
    # Example 1: Output: [2,-3,4]
    root = [5, 2, -3]

    # Example 2: Output: [2]
    # root = [5, 2, -5]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findFrequentTreeSum(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
