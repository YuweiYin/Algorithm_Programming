#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1379-Find-a-Corresponding-Node-of-a-Binary-Tree-in-a-Clone-of-That-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-17
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 1379 - (Medium) - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

Description & Requirement:
    Given two binary trees original and cloned and given a reference to a node target in the original tree.

    The cloned tree is a copy of the original tree.

    Return a reference to the same node in the cloned tree.

    Note that you are not allowed to change any of the two trees or 
    the target node and the answer must be a reference to a node in the cloned tree.

Example 1:
    Input: tree = [7,4,3,null,null,6,19], target = 3
    Output: 3
    Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:
    Input: tree = [7], target =  7
    Output: 7
Example 3:
    Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
    Output: 4

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    The values of the nodes of the tree are unique.
    target node is a node from the original tree and is not null.

Follow up:
    Could you solve the problem if repeated values on the tree are allowed?
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
        for idx, cur_root in enumerate(node_list):
            if cur_root is not None:
                cur_root_right_index = (idx + 1) << 1
                cur_root_left_index = cur_root_right_index - 1
                if cur_root_left_index < len_node_list:
                    cur_root.left = node_list[cur_root_left_index]
                if cur_root_right_index < len_node_list:
                    cur_root.right = node_list[cur_root_right_index]
        return node_list[0]  # return root_node

    @staticmethod
    def show_binary_tree_pre_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                val_list.append(cur_root.val)
                __dfs(cur_root.left)
                __dfs(cur_root.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_mid_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                __dfs(cur_root.left)
                val_list.append(cur_root.val)
                __dfs(cur_root.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_post_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_root):
            if isinstance(cur_root, TreeNode):
                __dfs(cur_root.left)
                __dfs(cur_root.right)
                val_list.append(cur_root.val)

        __dfs(root_node)
        return val_list


class Solution:
    def getTargetCopy(self, original: Optional[TreeNode], cloned: Optional[TreeNode],
                      target: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(original, TreeNode) or not isinstance(cloned, TreeNode):
            return None
        if not isinstance(target, TreeNode):
            return None
        # main method: (the same node will appear in the same position in the pre-order traverse path)
        return self._getTargetCopy(original, cloned, target)

    def _getTargetCopy(self, original: Optional[TreeNode], cloned: Optional[TreeNode],
                      target: Optional[TreeNode]) -> Optional[TreeNode]:
        assert isinstance(original, TreeNode) and isinstance(cloned, TreeNode) and isinstance(target, TreeNode)

        node_list_original = []
        stop_dfs = [False]

        def __pre_order_original(cur_node: Optional[TreeNode]):
            if stop_dfs[0]:
                return
            if isinstance(cur_node, TreeNode):
                node_list_original.append(cur_node)
                if cur_node == target:
                    stop_dfs[0] = True
                    return
                __pre_order_original(cur_node.left)
                __pre_order_original(cur_node.right)

        __pre_order_original(original)

        target_index = len(node_list_original)
        node_counter = [0]
        stop_dfs = [False]
        res = []

        def __pre_order_cloned(cur_node: Optional[TreeNode]):
            if stop_dfs[0]:
                return
            if isinstance(cur_node, TreeNode):
                node_counter[0] += 1
                if node_counter[0] == target_index:
                    stop_dfs[0] = True
                    res.append(cur_node)
                    return
                __pre_order_cloned(cur_node.left)
                __pre_order_cloned(cur_node.right)

        __pre_order_cloned(cloned)
        return res[0] if len(res) > 0 else None


def main():
    # Example 1: Output: 3
    # tree = [7, 4, 3, None, None, 6, 19]
    # target = 3
    node_6 = TreeNode(val=6)
    node_19 = TreeNode(val=19)
    node_3 = TreeNode(val=3, left=node_6, right=node_19)
    node_4 = TreeNode(val=4)
    node_7 = TreeNode(val=7, left=node_4, right=node_3)
    tree = node_7

    node_6_cloned = TreeNode(val=6)
    node_19_cloned = TreeNode(val=19)
    node_3_cloned = TreeNode(val=3, left=node_6_cloned, right=node_19_cloned)
    node_4_cloned = TreeNode(val=4)
    node_7_cloned = TreeNode(val=7, left=node_4_cloned, right=node_3_cloned)
    cloned = node_7_cloned

    target = node_3

    # Example 2: Output: 7
    # tree = [7]
    # target = 7

    # Example 3: Output: 4
    # tree = [8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]
    # target = 4

    # root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getTargetCopy(tree, cloned, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans.val)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
