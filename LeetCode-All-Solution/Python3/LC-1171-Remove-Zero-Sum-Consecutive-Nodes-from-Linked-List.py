#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1171-Remove-Zero-Sum-Consecutive-Nodes-from-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-11
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 1171 - (Medium) - Remove Zero Sum Consecutive Nodes from Linked List
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

Description & Requirement:
    Given the head of a linked list, we repeatedly delete consecutive sequences of nodes 
    that sum to 0 until there are no such sequences.

    After doing so, return the head of the final linked list.  You may return any such answer.

    (Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
    Input: head = [1,2,-3,3,1]
    Output: [3,1]
    Note: The answer [1,2,1] would also be accepted.
Example 2:
    Input: head = [1,2,3,-3,4]
    Output: [1,2,4]
Example 3:
    Input: head = [1,2,3,-3,-2]
    Output: [1]

Constraints:
    The given linked list will contain between 1 and 1000 nodes.
    Each node in the linked list has -1000 <= node.val <= 1000.
"""


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
    def build_singly_linked_list_with_loop(val_list: List[int], loop_pos: int):
        if loop_pos == -1:
            return ListNode.build_singly_linked_list(val_list)
        if not isinstance(val_list, list) or len(val_list) <= 0:
            return None
        head_node = ListNode(val=val_list[0])
        node_list = [head_node]
        ptr = head_node
        len_val = len(val_list)
        val_index = 1
        while val_index < len_val:
            new_node = ListNode(val=val_list[val_index])  # create new node
            ptr.next = new_node  # singly link
            ptr = new_node  # move
            node_list.append(new_node)
            val_index += 1
        if 0 <= loop_pos < len(node_list):
            node_list[len(node_list) - 1].next = node_list[loop_pos]
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


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None
        # main method: (hash)
        return self._removeZeroSumSublists(head)

    def _removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not isinstance(head, ListNode):
            return None

        prefix = 0
        visited = {}
        visited[0] = dummy_head = ListNode(0)
        dummy_head.next = head

        while isinstance(head, ListNode):
            prefix += head.val
            visited[prefix] = head
            head = head.next

        head = dummy_head
        prefix = 0
        while isinstance(head, ListNode):
            prefix += head.val
            head.next = visited[prefix].next
            head = head.next

        return dummy_head.next


def main():
    # Example 1: Output: [3,1]
    head = [1, 2, -3, 3, 1]

    # Example 2: Output: [1,2,4]
    # head = [1, 2, 3, -3, 4]

    # Example 3: Output: [1]
    # head = [1, 2, 3, -3, -2]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeZeroSumSublists(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
