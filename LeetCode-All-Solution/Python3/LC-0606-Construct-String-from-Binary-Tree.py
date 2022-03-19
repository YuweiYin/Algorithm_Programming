#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0606-Construct-String-from-Binary-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-19
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0606 - (Easy) - Construct String from Binary Tree
https://leetcode.com/problems/construct-string-from-binary-tree/

Description:
    Given the root of a binary tree, construct a string consisting of parenthesis and integers 
    from a binary tree with the preorder traversal way, and return it.

    Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship 
    between the string and the original binary tree.

Example 1:
    Input: root = [1,2,3,4]
    Output: "1(2(4))(3)"
    Explanation: Originally, it needs to be "1(2(4)())(3()())", 
        but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:
    Input: root = [1,2,3,null,4]
    Output: "1(2()(4))(3)"
    Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair 
        to break the one-to-one mapping relationship between the input and the output.

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -1000 <= Node.val <= 1000
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # exception case
        if not isinstance(root, TreeNode):
            return ""  # no tree
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return str(root.val)
        # main method: (pre-order traverse)
        return self._tree2str(root)

    def _tree2str(self, root: Optional[TreeNode]) -> str:
        assert isinstance(root, TreeNode)

        def __dfs(node: Optional[TreeNode]) -> str:  # pre-order traverse
            if not isinstance(node, TreeNode):
                return ""
            if isinstance(node.left, TreeNode) and isinstance(node.right, TreeNode):  # has both children
                return str(node.val) + "(" + __dfs(node.left) + ")" + "(" + __dfs(node.right) + ")"
            elif isinstance(node.left, TreeNode):  # only has left child
                return str(node.val) + "(" + __dfs(node.left) + ")"
            elif isinstance(node.right, TreeNode):  # only has right child
                return str(node.val) + "()(" + __dfs(node.right) + ")"
            else:  # has no children
                return str(node.val)

        res = __dfs(root)
        return res


def main():
    # Example 1: Output: "1(2(4))(3)"
    # root = [1, 2, 3, 4]

    # Example 2: Output: "1(2()(4))(3)"
    root = [1, 2, 3, None, 4]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.tree2str(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
