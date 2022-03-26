#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0450-Delete-Node-in-a-BST.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-26
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0450 - (Medium) - Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/

Description:
    Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
    Return the root node reference (possibly updated) of the BST.

    Basically, the deletion can be divided into two stages:
        1. Search for a node to remove.
        2. If the node is found, delete the node.

Example 1:
    Input: root = [5,3,6,2,4,null,7], key = 3
    Output: [5,4,6,2,null,null,7]
    Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
        One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
        Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
Example 2:
    Input: root = [5,3,6,2,4,null,7], key = 0
    Output: [5,3,6,2,4,null,7]
    Explanation: The tree does not contain a node with value = 0.
Example 3:
    Input: root = [], key = 0
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    Each node has a unique value.
    root is a valid binary search tree.
    -10^5 <= key <= 10^5

Follow up:
    Could you solve it with time complexity O(height of tree)?
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # exception case
        if not isinstance(root, TreeNode):
            return None  # no tree
        if not isinstance(root.left, TreeNode) and not isinstance(root.right, TreeNode):
            return None if root.val == key else root
        # main method: (BST traverse, recursively delete a node and its successor or predecessor in its subtree)
        return self._deleteNode(root, key)

    def _deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        assert isinstance(root, TreeNode)
        # pseudo_root = TreeNode(val=root.val, left=None, right=root)  # because the current root may be deleted

        def __find_successor(cur_node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not isinstance(cur_node, TreeNode):
                return None
            cur_node = cur_node.right  # one step right
            if not isinstance(cur_node, TreeNode):
                return None
            while isinstance(cur_node.left, TreeNode):  # then, go to the leftmost
                cur_node = cur_node.left
            return cur_node if isinstance(cur_node, TreeNode) else None

        def __find_predecessor(cur_node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not isinstance(cur_node, TreeNode):
                return None
            cur_node = cur_node.left  # one step left
            if not isinstance(cur_node, TreeNode):
                return None
            while isinstance(cur_node.right, TreeNode):  # then, go to the rightmost
                cur_node = cur_node.right
            return cur_node if isinstance(cur_node, TreeNode) else None

        def __delete(cur_node: Optional[TreeNode], delete_key: int) -> Optional[TreeNode]:
            if not isinstance(cur_node, TreeNode):
                return None
            if delete_key == cur_node.val:  # delete the current node
                if not isinstance(cur_node.left, TreeNode) and not isinstance(cur_node.right, TreeNode):
                    cur_node = None  # cur_node is a leaf node
                elif not isinstance(cur_node.right, TreeNode):  # the current node has only left child
                    # delete predecessor from left subtree
                    predecessor_node = __find_predecessor(cur_node)
                    # assert isinstance(predecessor_node, TreeNode)
                    cur_node.val = predecessor_node.val
                    cur_node.left = __delete(cur_node.left, predecessor_node.val)
                elif not isinstance(cur_node.left, TreeNode):  # the current node has only right child
                    # delete successor from right subtree
                    successor_node = __find_successor(cur_node)
                    # assert isinstance(successor_node, TreeNode)
                    cur_node.val = successor_node.val
                    cur_node.right = __delete(cur_node.right, successor_node.val)
                else:  # the current node has both left and right children
                    # either predecessor from left subtree or delete successor from right subtree is fine
                    successor_node = __find_successor(cur_node)
                    # assert isinstance(successor_node, TreeNode)
                    cur_node.val = successor_node.val
                    cur_node.right = __delete(cur_node.right, successor_node.val)
            elif delete_key < cur_node.val:  # modify the left subtree
                cur_node.left = __delete(cur_node.left, delete_key)
            else:  # modify the right subtree
                cur_node.right = __delete(cur_node.right, delete_key)
            return cur_node

        return __delete(root, key)


def main():
    # Example 1: Output: [5,4,6,2,null,null,7]
    root = [5, 3, 6, 2, 4, None, 7]
    key = 3

    # Example 2: Output: [5,3,6,2,4,null,7]
    # root = [5, 3, 6, 2, 4, None, 7]
    # key = 0

    # Example 3: Output: []
    # root = []
    # key = 0

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.deleteNode(root_node, key)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans.val)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
