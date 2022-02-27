#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0662-Maximum-Width-of-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-27
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections

"""
LeetCode - 0662 - (Medium) - Maximum Width of Binary Tree
https://leetcode.com/problems/maximum-width-of-binary-tree/

Description & Requirement:
    Given the root of a binary tree, return the maximum width of the given tree.

    The maximum width of a tree is the maximum width among all levels.

    The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
    where the null nodes between the end-nodes are also counted into the length calculation.

    It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:
    Input: root = [1,3,2,5,3,null,9]
    Output: 4
    Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
    Input: root = [1,3,null,5,3]
    Output: 2
    Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
    Input: root = [1,3,2,5]
    Output: 2
    Explanation: The maximum width existing in the second level with the length 2 (3,2).

Constraints:
    The number of nodes in the tree is in the range [1, 3000].
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # exception case
        if not isinstance(root, TreeNode):
            return 0  # no tree, just null
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return 1  # only root node
        # main method: (BFS layer traverse, give node_number to every node as the node_number in perfect binary tree)
        # layer 1: root = 1
        # layer 2: root.left = 2 (= 2 * 1), root.right = 3 (= 2 * 1 + 1)
        # layer 3: root.left.left = 4 (= 2 * 2), root.left.right = 5 (= 2 * 2 + 1)
        #          root.right.left = 4 (= 3 * 2), root.right.right = 5 (= 3 * 2 + 1)
        # the width of each layer is (max_node_number - min_node_number + 1) in this layer
        # other method:
        #     apply bfs, for each layer, the first node that bfs visits is the leftmost node in this layer;
        #         similarly, the last node that bfs visits is the rightmost node in this layer.
        #     or apply dfs, but need to store both node and its layer information
        return self._widthOfBinaryTree(root)

    def _widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        assert isinstance(root, TreeNode)

        layer_number = [[1]]  # layer_number[i] is all the order_number in the layer i
        bfs_queue = []  # element: (cur_node, the node_number of its parent, True if it's left child else False)
        if isinstance(root.left, TreeNode):
            bfs_queue.append((root.left, 1, True))
        if isinstance(root.right, TreeNode):
            bfs_queue.append((root.right, 1, False))

        while len(bfs_queue) > 0:
            new_bfs_queue = []
            cur_layer_number = []
            for cur_node, parent_number, left_flag in bfs_queue:  # deal all nodes in a layer at a time
                if not isinstance(cur_node, TreeNode):
                    continue

                # calculate the node_number of the current node and store in the cur_layer_number list
                if left_flag:
                    cur_node_number = parent_number << 1
                else:
                    cur_node_number = (parent_number << 1) + 1
                cur_layer_number.append(cur_node_number)

                # put its child in the queue
                if isinstance(cur_node.left, TreeNode):
                    new_bfs_queue.append((cur_node.left, cur_node_number, True))
                if isinstance(cur_node.right, TreeNode):
                    new_bfs_queue.append((cur_node.right, cur_node_number, False))
            # done dealing with this layer
            layer_number.append(cur_layer_number)
            bfs_queue = new_bfs_queue

        # scan, the width of each layer is (max_node_number - min_node_number + 1) in this layer
        res = 1
        for layer in layer_number:
            res = max(res, max(layer) - min(layer) + 1)
        return res


def main():
    # Example 1: Output: 4
    # root = [1, 3, 2, 5, 3, None, 9]

    # Example 2: Output: 2
    # root = [1, 3, None, 5, 3]

    # Example 3: Output: 2
    root = [1, 3, 2, 5]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.widthOfBinaryTree(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)
    # print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
