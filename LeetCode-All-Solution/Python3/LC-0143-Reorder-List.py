#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0143-Reorder-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-23
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0143 - (Medium) - Reorder List
https://leetcode.com/problems/reorder-list/

Description & Requirement:
    You are given the head of a singly linked-list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln

    Reorder the list to be on the following form:
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]
Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 10^4].
    1 <= Node.val <= 1000
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


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # exception case
        # at least 3 nodes
        if isinstance(head, ListNode) and isinstance(head.next, ListNode) and isinstance(head.next.next, ListNode):
            # main method: (record nodes in a list)
            self._reorderList(head)

    def _reorderList(self, head_node: Optional[ListNode]) -> None:
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode) and \
               isinstance(head_node.next.next, ListNode)

        node_list = []
        ptr = head_node
        while isinstance(ptr, ListNode):
            node_list.append(ptr)
            ptr = ptr.next

        # def __reverse_list(origin_list: list, left_idx: int, right_idx: int) -> list:
        #     while left_idx < right_idx:
        #         origin_list[left_idx], origin_list[right_idx] = origin_list[right_idx], origin_list[left_idx]
        #         left_idx += 1
        #         right_idx -= 1
        #     return origin_list

        new_list = []
        left_idx = 0
        right_idx = len(node_list) - 1
        while left_idx < right_idx:
            new_list.append(node_list[left_idx])
            new_list.append(node_list[right_idx])
            left_idx += 1
            right_idx -= 1
        if left_idx == right_idx:
            new_list.append(node_list[left_idx])

        for idx in range(1, len(new_list)):
            new_list[idx - 1].next = new_list[idx]
        new_list[-1].next = None


def main():
    # Example 1: Output: [1,4,2,3]
    head = [1, 2, 3, 4]

    # Example 2: Output: [1,5,2,4,3]
    # head = [1, 2, 3, 4, 5]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.reorderList(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(head_node)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
