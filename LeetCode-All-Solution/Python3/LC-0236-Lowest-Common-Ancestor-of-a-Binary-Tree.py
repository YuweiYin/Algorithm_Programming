#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0236-Lowest-Common-Ancestor-of-a-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-28
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0236 - (Medium) - Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Description:
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on [Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): 
        "The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
        that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [2, 10^5].
    -10^9 <= Node.val <= 10^9
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
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
    def lowestCommonAncestor(self, root: Optional[TreeNode],
                             p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        # main method: (BFS recursively find LCA)
        return self._lowestCommonAncestor(root, p, q)

    def _lowestCommonAncestor(self, root: Optional[TreeNode],
                              p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:

        res = [TreeNode()]

        def __dfs(_root: Optional[TreeNode], _p: Optional[TreeNode], _q: Optional[TreeNode]) -> bool:
            if isinstance(_root, TreeNode):
                left = __dfs(_root.left, _p, _q)  # return True if the left subtree contains either _p or _q
                right = __dfs(_root.right, _p, _q)  # return True if the right subtree contains either _p or _q
                # cur _root is a common ancestor if
                #     case 1: left and right
                #     case 2: _root itself is either _p or _q, and one of its child subtree contains either _q or _p
                if (left and right) or ((_root.val == _p.val or _root.val == _q.val) and (left or right)):
                    res[0] = _root  # update the lower common ancestor
                # return True if the current subtree contains either _p or _q
                return left or right or _root.val == _p.val or _root.val == _q.val
            else:
                return False

        __dfs(root, p, q)
        return res[0]


def main():
    # Example 1: Output: 3
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 1

    # Example 2: Output: 5
    # root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    # p = 5
    # q = 4

    # Example 3: Output: 1
    # root = [1, 2]
    # p = 1
    # q = 2

    def __build_binary_tree_layer(val_list: List[int], p_val, q_val):
        if not isinstance(val_list, list) or len(val_list) <= 0:
            return None

        p_node = None
        q_node = None

        node_list = []
        for v in val_list:
            if v is None:
                node_list.append(None)
            else:
                if v == p_val:
                    p_node = TreeNode(val=v)
                    node_list.append(p_node)
                elif v == q_val:
                    q_node = TreeNode(val=v)
                    node_list.append(q_node)
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
        return node_list[0], p_node, q_node

    root_node, p_node, q_node = __build_binary_tree_layer(root, p, q)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lowestCommonAncestor(root_node, p_node, q_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans.val)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
