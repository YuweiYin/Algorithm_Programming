#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0117-Populating-Next-Right-Pointers-in-Each-Node-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-20
=================================================================="""
import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0117 - (Medium) - Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Description & Requirement:
    Given a binary tree
        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }
    Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.

Example 1:
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A), 
        your function should populate each next pointer to point to its next right node, 
        just like in Figure B. The serialized output is in level order as connected by the next pointers, 
        with '#' signifying the end of each level.
Example 2:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 6000].
    -100 <= Node.val <= 100

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
            # return self._connect(root)
            return self._connectSimplify(root)

    def _connectSimplify(self, root: Optional[Node]) -> Optional[Node]:

        def __bfs_layer_traverse(cur_layer_nodes: List[Node]):
            # populate each next pointer to point to its next right node
            for idx in range(len(cur_layer_nodes) - 1):
                cur_layer_nodes[idx].next = cur_layer_nodes[idx + 1]
            # get all next layer nodes
            next_layer_nodes = []
            for node in cur_layer_nodes:
                if isinstance(node.left, Node):
                    next_layer_nodes.append(node.left)
                if isinstance(node.right, Node):
                    next_layer_nodes.append(node.right)
            # deal with the next layer
            if len(next_layer_nodes) > 0:
                __bfs_layer_traverse(next_layer_nodes)

        __bfs_layer_traverse([root])
        return root

    def _connect(self, root: Optional[Node]) -> Optional[Node]:
        cur_level = 0  # the current layer of perfect binary tree

        node_queue = collections.deque()
        node_queue.append(root)

        height_dict = dict({})  # key: node height; value: number of nodes with this height

        def __dfs_count_height(node: Optional[Node]) -> int:
            """
            :return: max height
            """
            if isinstance(node, Node):
                if isinstance(node.left, Node) and isinstance(node.right, Node):
                    height = max(__dfs_count_height(node.left), __dfs_count_height(node.right)) + 1
                elif isinstance(node.left, Node):
                    height = __dfs_count_height(node.left) + 1
                elif isinstance(node.right, Node):
                    height = __dfs_count_height(node.right) + 1
                else:
                    height = 1  # leaf height == 1
                # record height
                if height not in height_dict:
                    height_dict[height] = 1
                else:
                    height_dict[height] += 1
                return height
            else:
                return 0

        # root_height = __dfs_count_height(root)  # leaf height == 1, root_height is the max height
        # for ht in range(1, root_height + 1):
        #     assert ht in height_dict and height_dict[ht] > 0

        depth_dict = dict({})  # key: node depth; value: number of nodes with this depth

        def __bfs_count_depth(cur_layer_nodes: List[Node]) -> int:
            """
            :return: max depth
            """
            next_layer_nodes = []
            for node in cur_layer_nodes:
                if isinstance(node.left, Node):
                    next_layer_nodes.append(node.left)
                if isinstance(node.right, Node):
                    next_layer_nodes.append(node.right)
            if len(next_layer_nodes) > 0:
                depth = 1 + __bfs_count_depth(next_layer_nodes)
            else:
                depth = 1
            if depth not in depth_dict:
                depth_dict[depth] = len(cur_layer_nodes)
            else:
                pass  # error branch
            return depth

        root_depth = __bfs_count_depth([root])  # leaf depth == 1, root_depth is the max depth (reverse idea)
        for dt in range(1, root_depth + 1):
            assert dt in depth_dict and depth_dict[dt] > 0

        while len(node_queue) > 0:
            cur_level_node_list = []  # all nodes of this layer
            # get the number of nodes on this layer, based on height_dict
            node_num = depth_dict[root_depth - cur_level]  # how many nodes in this layer (of this height)
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
    # Example 1: Output: [1,#,2,3,#,4,5,7,#]
    # root = [1, 2, 3, 4, 5, None, 7]

    # Example 2: Output: []
    # root = []

    root = [1, 2, 3, 4, 5]

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
