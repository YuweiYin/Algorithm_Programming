#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0092-Reverse-Linked-List-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-21
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0092 - (Medium) - Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Description & Requirement:
    Given the head of a singly linked list and two integers left and right where left <= right, 
    reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

Follow up:
    Could you do it in one pass?
"""


# Definition for singly-linked list.
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
        while ptr:
            print(ptr.val)
            ptr = ptr.next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None
        assert isinstance(left, int) and isinstance(right, int) and 1 <= left <= right
        # main method: (scan and change links)
        return self._reverseBetween(head, left, right)

    def _reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Runtime: 30 ms, faster than 96.39% of Python3 online submissions for Reverse Linked List II.
        Memory Usage: 14 MB, less than 87.01% of Python3 online submissions for Reverse Linked List II.
        """
        assert isinstance(head, ListNode)
        assert isinstance(left, int) and isinstance(right, int) and 1 <= left <= right

        pseudo_head = ListNode(next=head)
        ptr = pseudo_head
        for _ in range(left - 1):
            ptr = ptr.next

        ptr_next = ptr.next
        for _ in range(right - left):
            ptr_next_next = ptr_next.next
            ptr_next.next = ptr_next_next.next
            ptr_next_next.next = ptr.next
            ptr.next = ptr_next_next

        return pseudo_head.next


def main():
    # Example 1: Output: [1,4,3,2,5]
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4

    # Example 2: Output: [5]
    # head = [5]
    # left = 1
    # right = 1

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverseBetween(head_node, left, right)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
