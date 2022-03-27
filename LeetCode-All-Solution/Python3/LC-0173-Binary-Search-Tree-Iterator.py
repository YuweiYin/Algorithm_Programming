#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0173-Binary-Search-Tree-Iterator.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-27
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0173 - (Medium) - Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

Description:
    Implement the BSTIterator class that represents an iterator 
    over the in-order traversal of a binary search tree (BST):
        BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
            The root of the BST is given as part of the constructor. 
            The pointer should be initialized to a non-existent number smaller than any element in the BST.
        boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, 
            otherwise returns false.
        int next() Moves the pointer to the right, then returns the number at the pointer.

    Notice that by initializing the pointer to a non-existent smallest number, 
    the first call to next() will return the smallest element in the BST.

    You may assume that next() calls will always be valid. 
    That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:
    Input
        ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
        [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    Output
        [null, 3, 7, true, 9, true, 15, true, 20, false]
    Explanation
        BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
        bSTIterator.next();    // return 3
        bSTIterator.next();    // return 7
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 9
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 15
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 20
        bSTIterator.hasNext(); // return False

Constraints:
    The number of nodes in the tree is in the range [1, 10^5].
    0 <= Node.val <= 10^6
    At most 10^5 calls will be made to hasNext, and next.

Follow up:
    Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, 
    where h is the height of the tree?
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


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.val_list = []  # in this problem, BST is fixed, so just record the in-order traverse list
        self.cursor = -1

        def __dfs(cur_node: Optional[TreeNode]):  # in-order BST traverse
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                self.val_list.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(self.root)

    def next(self) -> int:
        if self.cursor + 1 < len(self.val_list):
            self.cursor += 1
            return self.val_list[self.cursor]
        else:
            return -1  # error

    def hasNext(self) -> bool:
        return self.cursor + 1 < len(self.val_list)


def main():
    # Example 1: Output: [null, 3, 7, true, 9, true, 15, true, 20, false]
    command_list = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    param_list = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]

    # init instance
    # solution = Solution()
    root_node = TreeNode.build_binary_tree_layer(param_list[0][0])

    # run & time
    start = time.process_time()
    obj = BSTIterator(root_node)
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        # param = param_list[idx]
        if command == "next":
            ans.append(obj.next())
        elif command == "hasNext":
            ans.append(obj.hasNext())
        else:
            continue
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
