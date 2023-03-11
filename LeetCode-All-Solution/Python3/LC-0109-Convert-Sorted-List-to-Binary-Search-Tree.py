#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0109-Convert-Sorted-List-to-Binary-Search-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-11
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0109 - (Medium) - Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Description & Requirement:
    Given the head of a singly linked list where elements are sorted in ascending order, 
    convert it to a height-balanced binary search tree.

    A height-balanced binary tree is a binary tree in which 
    the depth of the two subtrees of every node never differs by more than one.

Example 1:
    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], 
        which represents the shown height balanced BST.
Example 2:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in head is in the range [0, 2 * 10^4].
    -10^5 <= Node.val <= 10^5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # this means (by default): end_node.next == None

    @staticmethod
    def build_singly_linked_list(val_list: List[int]):
        if not isinstance(val_list, list) or len(val_list) <= 0:
            return None
        head_node = ListNode(val=val_list[0])
        ptr = head_node
        len_val = len(val_list)
        val_index = 1
        while val_index < len_val:
            new_node = ListNode(val=val_list[val_index])  # create new node
            ptr.next = new_node  # singly link
            ptr = new_node  # move
            val_index += 1
        return head_node

    @staticmethod
    def show_val_singly_linked_list(head_node) -> None:
        # exception case
        if (not isinstance(head_node, ListNode)) and (head_node is not None):
            return None  # Error head_node type
        if not isinstance(head_node, ListNode):
            return None  # Error n type or needn't delete
        ptr = head_node
        while ptr:
            print(ptr.val)
            ptr = ptr.next


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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None
        # main method: (divide and conquer)
        return self._sortedListToBST(head)

    def _sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        assert isinstance(head, ListNode)

        def __get_length(cur_node: ListNode) -> int:
            cur_res = 0
            while cur_node:
                cur_res += 1
                cur_node = cur_node.next
            return cur_res

        def __build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right + 1) >> 1
            root = TreeNode()
            root.left = __build_tree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = __build_tree(mid + 1, right)
            return root

        return __build_tree(0, __get_length(head) - 1)


def main():
    # Example 1: Output: [0,-3,9,-10,null,5]
    head = [-10, -3, 0, 5, 9]

    # Example 2: Output: []
    # head = []

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.sortedListToBST(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
