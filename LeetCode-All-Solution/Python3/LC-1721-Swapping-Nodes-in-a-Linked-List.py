#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1721-Swapping-Nodes-in-a-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-04
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 1721 - (Medium) - Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Description & Requirement:
    You are given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the values of the k-th node from the beginning 
    and the k-th node from the end (the list is 1-indexed).

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
Example 2:
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 10^5
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
    def show_val_singly_linked_list(head_node) -> None:
        # exception case
        if (not isinstance(head_node, ListNode)) and (head_node is not None):
            return None  # Error head_node type
        if not isinstance(head_node, ListNode):
            return None  # Error n type or needn't delete
        ptr = head_node
        val_list = []
        while ptr:
            val_list.append(ptr.val)
            ptr = ptr.next
        print(val_list)


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None
        if not isinstance(head.next, ListNode):
            return head
        assert isinstance(k, int) and k >= 1
        # main method: (scan, get len(linked_list) and then locate and swap)
        return self._swapNodes(head, k)

    def _swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pseudo_head = ListNode(val=int(1e9+7), next=head)

        # get len(linked_list)
        sll_len = 0
        ptr = pseudo_head.next
        while isinstance(ptr, ListNode):
            sll_len += 1
            ptr = ptr.next

        # locate the parent nodes of the two target nodes
        target_1 = k - 1
        target_2 = sll_len - k
        if target_1 == target_2:
            return head

        idx = 0
        ptr_1 = pseudo_head
        while isinstance(ptr_1, ListNode) and idx < target_1:
            ptr_1 = ptr_1.next
            idx += 1

        idx = 0
        ptr_2 = pseudo_head
        while isinstance(ptr_2, ListNode) and idx < target_2:
            ptr_2 = ptr_2.next
            idx += 1

        # swap
        if ptr_1 == ptr_2:
            return head

        target_node_1 = ptr_1.next
        target_node_2 = ptr_2.next

        ptr_1.next = target_node_2
        ptr_2.next = target_node_1

        target_node_1.next, target_node_2.next = target_node_2.next, target_node_1.next

        return pseudo_head.next


def main():
    # Example 1: Output: [1,4,3,2,5]
    # head = [1, 2, 3, 4, 5]
    # k = 2

    # Example 2: Output: [7,9,6,6,8,7,3,0,9,5]
    head = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
    k = 5

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.swapNodes(head_node, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
