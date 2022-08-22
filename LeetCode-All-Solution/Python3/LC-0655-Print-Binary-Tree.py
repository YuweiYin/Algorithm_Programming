#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0655-Print-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-22
=================================================================="""

import sys
import time
from typing import List, Optional
import collections
# import functools

"""
LeetCode - 0655 - (Medium) - Print Binary Tree
https://leetcode.com/problems/print-binary-tree/

Description & Requirement:
    Given the root of a binary tree, construct a 0-indexed m x n string matrix res that 
    represents a formatted layout of the tree. 
    The formatted layout matrix should be constructed using the following rules:
        - The height of the tree is height and the number of rows m should be equal to height + 1.
        - The number of columns n should be equal to 2^{height + 1} - 1.
        - Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
        - For each node that has been placed in the matrix at position res[r][c], 
            place its left child at res[r+1][c-2^{height-r-1}] and its right child at res[r+1][c+2^{height-r-1}].
        - Continue this process until all the nodes in the tree have been placed.
        - Any empty cells should contain the empty string "".

    Return the constructed matrix res.

Example 1:
    Input: root = [1,2]
    Output: 
        [["","1",""],
         ["2","",""]]
Example 2:
    Input: root = [1,2,3,null,4]
    Output: 
        [["","","","1","","",""],
         ["","2","","","","3",""],
         ["","","4","","","",""]]

Constraints:
    The number of nodes in the tree is in the range [1, 2^10].
    -99 <= Node.val <= 99
    The depth of the tree will be in the range [1, 10].
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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # exception case
        if not isinstance(root, TreeNode):
            return []
        # main method: (bfs, layer traverse)
        return self._printTree(root)

    def _printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        assert isinstance(root, TreeNode)

        def __bfs_depth(_node: Optional[TreeNode]) -> int:
            h = -1
            _queue = [_node]
            while len(_queue) > 0:
                h += 1
                _new_queue = []
                for _n in _queue:
                    if _n.left:
                        _new_queue.append(_n.left)
                    if _n.right:
                        _new_queue.append(_n.right)
                _queue = _new_queue

            return h

        height = __bfs_depth(root)

        max_height = height + 1
        max_width = (1 << max_height) - 1
        res = [['' for _ in range(max_width)] for _ in range(max_height)]
        queue = collections.deque([(root, 0, (max_width - 1) >> 1)])

        while len(queue) > 0:
            node, r, c = queue.popleft()
            res[r][c] = str(node.val)
            if node.left:
                queue.append((node.left, r + 1, c - (1 << (height - r - 1))))
            if node.right:
                queue.append((node.right, r + 1, c + (1 << (height - r - 1))))

        return res


def main():
    # Example 1: Output: [["","1",""], ["2","",""]]
    # root = [1, 2]

    # Example 2: Output: [["","","","1","","",""], ["","2","","","","3",""], ["","","4","","","",""]]
    root = [1, 2, 3, None, 4]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.printTree(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
