#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1145-Binary-Tree-Coloring-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-03
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 1145 - (Medium) - Binary Tree Coloring Game
https://leetcode.com/problems/binary-tree-coloring-game/

Description & Requirement:
    Two players play a turn based game on a binary tree. We are given the root of this binary tree, 
    and the number of nodes n in the tree. n is odd, and each node has a distinct value from 1 to n.

    Initially, the first player names a value x with 1 <= x <= n, 
    and the second player names a value y with 1 <= y <= n and y != x. 
    The first player colors the node with value x red, and the second player colors the node with value y blue.

    Then, the players take turns starting with the first player. 
    In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and 
    colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

    If (and only if) a player cannot choose such a node in this way, they must pass their turn. 
    If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

    You are the second player. If it is possible to choose such a y to ensure you win the game, return true. 
    If it is not possible, return false.

Example 1:
    Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
    Output: true
    Explanation: The second player can choose the node with value 2.
Example 2:
    Input: root = [1,2,3], n = 3, x = 1
    Output: false

Constraints:
    The number of nodes in the tree is n.
    1 <= x <= n <= 100
    n is odd.
    1 <= Node.val <= n
    All the values of the tree are unique.
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
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # exception case
        assert isinstance(root, TreeNode)
        assert isinstance(n, int) and isinstance(x, int) and 1 <= x <= n
        # main method: (DFS)
        return self._btreeGameWinningMove(root, n, x)

    def _btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        assert isinstance(root, TreeNode)
        assert isinstance(n, int) and isinstance(x, int) and 1 <= x <= n

        x_node = [None]

        def __get_subtree_size(node):
            if not node:
                return 0
            if node.val == x:
                x_node[0] = node
            return 1 + __get_subtree_size(node.left) + __get_subtree_size(node.right)

        __get_subtree_size(root)

        leftSize = __get_subtree_size(x_node[0].left) if isinstance(x_node[0], TreeNode) else 0
        if leftSize >= ((n + 1) >> 1):
            return True

        rightSize = __get_subtree_size(x_node[0].right) if isinstance(x_node[0], TreeNode) else 0
        if rightSize >= ((n + 1) >> 1):
            return True

        return (n - leftSize - rightSize - 1) >= ((n + 1) >> 1)


def main():
    # Example 1: Output: true
    root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    n = 11
    x = 3

    # Example 2: Output: false
    # root = [1, 2, 3]
    # n = 3
    # x = 1

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.btreeGameWinningMove(root_node, n, x)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
