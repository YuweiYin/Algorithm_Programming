#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0328-Odd-Even-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-06
=================================================================="""

import sys
import time
from typing import List, Optional
import collections
# import functools

"""
LeetCode - 0328 - (Medium) - Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/

Description & Requirement:
    Given the head of a singly linked list, group all the nodes with odd indices together 
    followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.

    You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]
Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]

Constraints:
    The number of nodes in the linked list is in the range [0, 10^4].
    -10^6 <= Node.val <= 10^6
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None
        # main method: (scan)
        return self._oddEvenList(head)

    def _oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        assert isinstance(head, ListNode)

        even_head = head.next
        odd, even = head, even_head

        while isinstance(even, ListNode) and isinstance(even.next, ListNode):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


def main():
    # Example 1: Output: [1,3,5,2,4]
    # head = [1, 2, 3, 4, 5]

    # Example 2: Output: [2,3,6,7,1,5,4]
    head = [2, 1, 3, 5, 6, 4, 7]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.oddEvenList(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
