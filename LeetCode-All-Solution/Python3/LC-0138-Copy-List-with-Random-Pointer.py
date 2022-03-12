#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0138-Copy-List-with-Random-Pointer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-12
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0138 - (Medium) - Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

Description & Requirement:
    A linked list of length n is given such that each node contains an additional random pointer, 
    which could point to any node in the list, or null.

    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
    where each new node has its value set to the value of its corresponding original node. 
    Both the next and random pointer of the new nodes should point to new nodes in the copied list 
    such that the pointers in the original list and copied list represent the same list state. 
    None of the pointers in the new list should point to nodes in the original list.

    For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
    then for the corresponding two nodes x and y in the copied list, x.random --> y.

    Return the head of the copied linked list.

    The linked list is represented in the input/output as a list of n nodes. 
    Each node is represented as a pair of [val, random_index] where:
        val: an integer representing Node.val
        random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

    Your code will only be given the head of the original linked list.

Example 1:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:
    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]
Example 3:
    Input: head = [[3,null],[3,0],[3,null]]
    Output: [[3,null],[3,0],[3,null]]

Constraints:
    0 <= n <= 1000
    -10^4 <= Node.val <= 10^4
    Node.random is null or is pointing to some node in the linked list.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    @staticmethod
    def build_node_list(node_list: List[List[Optional[int]]]):
        if len(node_list) == 0:
            return None
        head_node = Node(x=node_list[0][0], next=None, random=node_list[0][1])  # TODO: random should be Node or None
        ptr = head_node
        for node in node_list[1:]:
            new_node = Node(x=node[0], next=None, random=node[1])
            ptr.next = new_node
            ptr = ptr.next
        return head_node


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # exception case
        if not isinstance(head, Node):
            return None
        # main method: (scan, record node-index mapping, and deep copy)
        return self._copyRandomList(head)

    def _copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # get all old nodes and the node-index map
        node_list_old = []
        node_to_index = dict({})
        ptr = head
        index = 0
        while isinstance(ptr, Node):
            node_list_old.append(ptr)
            node_to_index[ptr] = index
            ptr = ptr.next
            index += 1

        # get index-index map: node_idx -> random_node/None -> random_idx/-1
        index_to_index = dict({})
        for idx, node_old in enumerate(node_list_old):
            if isinstance(node_old.random, Node) and node_old.random in node_to_index:
                index_to_index[idx] = node_to_index[node_old.random]
            else:
                index_to_index[idx] = -1

        # copy val first
        node_list_new = []
        for node_old in node_list_old:
            node_new = Node(x=node_old.val, next=None, random=None)
            node_list_new.append(node_new)

        # link all new nodes
        len_nodes = len(node_list_new)
        for idx in range(len_nodes - 1):
            node_list_new[idx].next = node_list_new[idx + 1]

        # set random pointer
        for idx, node_new in enumerate(node_list_new):
            random_idx = index_to_index[idx]
            if 0 <= random_idx < len_nodes:
                node_new.random = node_list_new[random_idx]

        return node_list_new[0]


def main():
    # Example 1: Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

    # Example 2: Output: [[1,1],[2,1]]
    # head = [[1, 1], [2, 1]]

    # Example 3: Output: [[3,null],[3,0],[3,null]]
    # head = [[3, None], [3, 0], [3, None]]

    head_node = Node.build_node_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.copyRandomList(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
