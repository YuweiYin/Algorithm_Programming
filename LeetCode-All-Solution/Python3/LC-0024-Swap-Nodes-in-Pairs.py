#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0024-Swap-Nodes-in-Pairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-16
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0024 - (Medium) - Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Description & Requirement:
    Given a linked list, swap every two adjacent nodes and return its head. 
    You must solve the problem without modifying the values in the list's nodes 
        (i.e., only nodes themselves may be changed.)

Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
Example 2:
    Input: head = []
    Output: []
Example 3:
    Input: head = [1]
    Output: [1]

Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
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
        while isinstance(ptr, ListNode):
            print(ptr.val)
            ptr = ptr.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        if not isinstance(head.next, ListNode):
            return head  # only one element
        # main method: (tow pointer, inplace swap every twp adjacent nodes in the singly linked list)
        return self._swapPairs(head)

    def _swapPairs(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 32 ms, faster than 83.13% of Python3 online submissions for Swap Nodes in Pairs.
        Memory Usage: 13.9 MB, less than 90.54% of Python3 online submissions for Swap Nodes in Pairs.
        """
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode)
        null_head = ListNode(val=int(1e9+7), next=head_node)
        left_ptr = null_head
        right_ptr = null_head.next
        while isinstance(right_ptr, ListNode) and isinstance(right_ptr.next, ListNode):
            # swap right_ptr and right_ptr.next
            third_ptr = right_ptr.next
            left_ptr.next = third_ptr
            right_ptr.next = third_ptr.next
            third_ptr.next = right_ptr
            # move on
            left_ptr = right_ptr
            right_ptr = right_ptr.next
        return null_head.next


def main():
    # Example 1: Output: [2,1,4,3]
    head = [1, 2, 3, 4]

    # Example 2: Output: []
    # head = []

    # Example 3: Output: [1]
    # head = [1]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.swapPairs(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
