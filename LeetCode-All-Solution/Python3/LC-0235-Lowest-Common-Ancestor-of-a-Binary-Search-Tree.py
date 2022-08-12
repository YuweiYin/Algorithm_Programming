#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0235-Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-10
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0235 - (Easy) - Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Description & Requirement:
    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

    According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): 
    "The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
    that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:
    Input: root = [2,1], p = 2, q = 1
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [2, 10^5].
    -10^9 <= Node.val <= 10^9
    All Node.val are unique.
    p != q
    p and q will exist in the BST.
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


class SparseTableRMQ:
    # Sparse Table construction, Time O(n log n)
    def __init__(self, array):
        self.st_len = len(array)
        self.inf = 0x3f3f3f3f  # 1061109567

        # construct log_table to calculate log_2 (len(array))
        # log_table[0]is null, and log_table[i] is floor(log_2 i)
        self.log_table = (self.st_len + 1) * [0]
        for i in range(2, self.st_len + 1):
            self.log_table[i] = self.log_table[i >> 1] + 1

        # Sparse Table: row = 1 + log_2 (self.st_len)，col = self.st_len
        # st[0] is the original array
        self.st = [[self.inf] * self.st_len for _ in range(1 + self.log_table[self.st_len])]
        self.st[0] = array

        # Dynamic Programming: st[i][j] = min( st[i-1][j], st[i-1][j + 2^(i-1)] )
        for i in range(1, len(self.st)):
            j = 0
            while j + (1 << i) <= self.st_len:
                self.st[i][j] = min(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                j += 1

    # if update any value in the array, the Sparse Table need to be reconstructed, Time O(n log n)
    # but if the length of array changes, it's better to reconstruct SparseTableRMQ object
    # and if the change of array is frequent, consider using Segment Tree instead of Sparse Table
    def update(self, index, value):
        if 0 <= index < len(self.st[0]) and self.st[0][index] != value:
            self.st[0][index] = value
            for i in range(1, len(self.st)):
                j = 0
                while j + (1 << i) <= self.st_len:
                    self.st[i][j] = min(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                    j += 1

    # get the minimum of [left, right] (closed interval), Time: O(1)
    # 0 <= left <= right <= n-1
    def query_minimum(self, left, right):
        if left > right:
            return self.inf

        if left < 0:
            left = 0
        if right >= self.st_len:
            right = self.st_len - 1

        # (right - left + 1) if the length of the interval, get the logarithm of this length
        log_2 = self.log_table[right - left + 1]

        # st[log_2][left] if the minimum in array[left: left + 2 ** log_2]
        return min(self.st[log_2][left], self.st[log_2][right - (1 << log_2) + 1])

    def print_st(self):
        for i in range(len(self.st)):
            print(self.st[i])


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode],
                             p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None
        # main method: (record the paths from root to p and from root to q, then find LCA)
        #     if there are multiple queries for the same BST, use SparseTableRMQ to solve
        return self._lowestCommonAncestor(root, p, q)

    def _lowestCommonAncestor(self, root: Optional[TreeNode],
                              p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 93 ms, faster than 80.80% of Python3 submissions for LCA of a Binary Search Tree.
        Memory Usage: 18.8 MB, less than 68.62% of Python3 submissions for LCA of a Binary Search Tree.
        """

        def __root_to_node_path(cur_node: Optional[TreeNode], target_node: Optional[TreeNode],
                                cur_path: List[TreeNode]) -> List[TreeNode]:
            if not isinstance(cur_node, TreeNode):
                return cur_path

            cur_path.append(cur_node)
            if cur_node == target_node:
                return cur_path
            elif target_node.val < cur_node.val:  # go left
                return __root_to_node_path(cur_node.left, target_node, cur_path)
            else:  # go right
                return __root_to_node_path(cur_node.right, target_node, cur_path)

        root_to_p = __root_to_node_path(root, p, [])
        root_to_q = __root_to_node_path(root, q, [])

        # get LCA
        common_ancestor = None
        for p_ancestor, q_ancestor in zip(root_to_p, root_to_q):
            if p_ancestor == q_ancestor:  # not fork yet, still common ancestor
                common_ancestor = p_ancestor
            else:  # start forking
                break

        return common_ancestor


def main():
    # Example 1: Output: 6
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 8

    # Example 2: Output: 2
    # root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    # p = 2
    # q = 4

    # Example 3: Output: 2
    # root = [2, 1]
    # p = 2
    # q = 1

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
    print(TreeNode.show_binary_tree_mid_order(root_node))  # mid traverse BST to get ordered list

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lowestCommonAncestor(root_node, p_node, q_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans.val)
    # print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
