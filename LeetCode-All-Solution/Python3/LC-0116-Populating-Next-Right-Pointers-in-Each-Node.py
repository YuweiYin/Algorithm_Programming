#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0116-Populating-Next-Right-Pointers-in-Each-Node.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-08
=================================================================="""
import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0116 - (Medium) - Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Description & Requirement:
    You are given a perfect binary tree where all leaves are on the same level, 
    and every parent has two children. The binary tree has the following definition:

    ```
        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }
    ```
    Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.


Example 2:
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation:
        Given the above perfect binary tree (Figure A), 
        your function should populate each next pointer to point to its next right node, just like in Figure B. 
        The serialized output is in level order as connected by the next pointers, 
        with '#' signifying the end of each level.
Example 2:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2^12 - 1].
    -1000 <= Node.val <= 1000

Follow-up:
    You may only use constant extra space.
    The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right  # the left and right of leaf_node are both None
        self.next = next  # the next node in the same level

    @staticmethod
    def build_binary_tree_layer(val_list: List[int]):
        if not isinstance(val_list, list) or len(val_list) <= 0:
            return None

        node_list = []
        for v in val_list:
            if v is None:
                node_list.append(None)
            else:
                node_list.append(Node(val=v))
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
            if isinstance(cur_node, Node):
                val_list.append(cur_node.val)
                __dfs(cur_node.left)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_mid_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, Node):
                __dfs(cur_node.left)
                val_list.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_post_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, Node):
                __dfs(cur_node.left)
                __dfs(cur_node.right)
                val_list.append(cur_node.val)

        __dfs(root_node)
        return val_list


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # exception case
        if not isinstance(root, Node):
            return None  # no tree
        else:
            # main method: (layer traverse)
            return self._connect(root)

    def _connect(self, root: Optional[Node]) -> Optional[Node]:
        cur_level = 0  # the current layer of perfect binary tree

        node_queue = collections.deque()
        node_queue.append(root)

        while len(node_queue) > 0:
            cur_level_node_list = []  # all nodes of this layer
            node_num = 1 << cur_level  # layer 0 has 1 node, layer 1 has 2 nodes, layer 3 has 4 nodes, ...
            cur_level += 1
            for _ in range(node_num):
                if len(node_queue) > 0:
                    cur_pop_node = node_queue.popleft()  # pop left, FIFO
                    cur_level_node_list.append(cur_pop_node)  # put it into cur_level_node_list to be connected
                    if isinstance(cur_pop_node.left, Node):
                        node_queue.append(cur_pop_node.left)  # put its left child into queue
                    if isinstance(cur_pop_node.right, Node):
                        node_queue.append(cur_pop_node.right)  # put its right child into queue
            idx = 0
            while idx < len(cur_level_node_list) - 1:
                cur_level_node_list[idx].next = cur_level_node_list[idx + 1]
                idx += 1
            # cur_level_node_list[len(cur_level_node_list) - 1] = None  # default None

        return root


def main():
    # Example 2: Output: [1,#,2,3,#,4,5,6,7,#]
    root = [1,2,3,4,5,6,7]

    # Example 2: Output: []
    # root = []

    root_node = Node.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.connect(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    print(Node.show_binary_tree_pre_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
