#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1457-Pseudo-Palindromic-Paths-in-a-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-14
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 1457 - (Medium) - Pseudo-Palindromic Paths in a Binary Tree
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

Description & Requirement:
    Given a binary tree where node values are digits from 1 to 9. 
    A path in the binary tree is said to be pseudo-palindromic if 
    at least one permutation of the node values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
    Input: root = [2,3,1,3,1,null,1]
    Output: 2 
    Explanation: The figure above represents the given binary tree. 
        There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], 
        and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths 
        since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and 
        the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:
    Input: root = [2,1,1,1,3,null,null,null,null,null,1]
    Output: 1 
    Explanation: The figure above represents the given binary tree. 
        There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], 
        and the path [2,1]. Among these paths only the green path is pseudo-palindromic 
        since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:
    Input: root = [9]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 9
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
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0
        # main method: (DFS)
        return self._pseudoPalindromicPaths(root)

    def _pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 1101 ms, faster than 78.51% of Python3 submissions for Pseudo-Palindromic Paths in a Binary Tree.
        Memory Usage: 86.5 MB, less than 19.31% of Python3 submissions for Pseudo-Palindromic Paths in a Binary Tree.
        """
        assert isinstance(root, TreeNode)

        res = [0]
        path = dict({})

        def __dfs(cur_node: Optional[TreeNode]) -> None:
            if not isinstance(cur_node, TreeNode):
                return
            cur_val = cur_node.val
            if cur_val not in path:
                path[cur_val] = 1
            else:
                path[cur_val] += 1

            # deal with the leaf node
            if not isinstance(cur_node.left, TreeNode) and not isinstance(cur_node.right, TreeNode):
                odd_occur = 0  # the counter of the elements that occur odd times
                for k, v in path.items():
                    if v & 0x01 == 1:
                        odd_occur += 1
                if odd_occur <= 1:
                    res[0] += 1

            # DFS
            if isinstance(cur_node.left, TreeNode):
                __dfs(cur_node.left)
            if isinstance(cur_node.right, TreeNode):
                __dfs(cur_node.right)

            path[cur_val] -= 1  # backtrace

        __dfs(root)
        return res[0]


def main():
    # Example 1: Output: 2
    root = [2, 3, 1, 3, 1, None, 1]

    # Example 2: Output: 1
    # root = [2, 1, 1, 1, 3, None, None, None, None, None, 1]

    # Example 3: Output: 1
    # root = [9]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pseudoPalindromicPaths(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
