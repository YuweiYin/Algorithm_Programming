#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0617-Merge-Two-Binary-Trees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-08
=================================================================="""
# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0617 - (Easy) - Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/

Description:
    You are given two binary trees `root1` and `root2`.

    Imagine that when you put one of them to cover the other, 
    some nodes of the two trees are overlapped while the others are not. 
    You need to merge the two trees into a new binary tree. 
    The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
    Otherwise, the NOT null node will be used as the node of the new tree.

Requirement:
    Return the merged tree.
    Note: The merging process must start from the root nodes of both trees.

Example 1:
    Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
    Output: [3,4,5,5,4,null,7]
Example 2:
    Input: root1 = [1], root2 = [1,2]
    Output: [2,2]

Constraints:
    The number of nodes in both trees is in the range [0, 2000].
    -10^4 <= Node.val <= 10^4
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root1, TreeNode) and not isinstance(root2, TreeNode):
            return None  # no tree
        elif not isinstance(root1, TreeNode):
            return root2  # only root2 is a tree
        elif not isinstance(root2, TreeNode):
            return root1  # only root1 is a tree
        else:
            # main method: (traverse both trees at the same time)
            return self._mergeTrees(root1, root2)

    def _mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def __dfs(node1, node2):  # pre-order traverse
            assert isinstance(node1, TreeNode) and isinstance(node2, TreeNode)
            node1.val += node2.val

            # left child
            if isinstance(node1.left, TreeNode) and isinstance(node2.left, TreeNode):
                __dfs(node1.left, node2.left)
            elif isinstance(node1.left, TreeNode):
                pass  # from this branch, root2 can't provide any nodes for root1
            elif isinstance(node2.left, TreeNode):
                node1.left = node2.left  # replant node2.left as node1.left
            else:
                pass

            # right child
            if isinstance(node1.right, TreeNode) and isinstance(node2.right, TreeNode):
                __dfs(node1.right, node2.right)
            elif isinstance(node1.right, TreeNode):
                pass  # from this branch, root2 can't provide any nodes for root1
            elif isinstance(node2.right, TreeNode):
                node1.right = node2.right  # replant node2.right as node1.right
            else:
                pass

        __dfs(root1, root2)
        return root1


def main():
    # Example 1: Output: [3, 4, 5, 5, 4, null, 7]
    root1 = [1, 3, 2, 5]
    root2 = [2, 1, 3, None, 4, None, 7]

    # Example 2: Output: [2, 2]
    # root1 = [1]
    # root2 = [1, 2]

    root_node1 = TreeNode.build_binary_tree_layer(root1)
    root_node2 = TreeNode.build_binary_tree_layer(root2)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mergeTrees(root_node1, root_node2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    print(TreeNode.show_binary_tree_pre_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
