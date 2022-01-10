#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0206-Reverse-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-10
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0206 - (Easy) - Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Description & Requirement:
    Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
Example 2:
    Input: head = [1,2]
    Output: [2,1]
Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        # main method: (two pointer, in-place reverse)
        return self._reverseList(head)

    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse_singly_linked_list(head)  # reverse

    @staticmethod
    def _reverse_singly_linked_list(head_node: Optional[ListNode]) -> Optional[ListNode]:
        if (not isinstance(head_node, ListNode)) and (head_node is not None):
            return head_node  # Error head_node type
        if not isinstance(head_node, ListNode) or not head_node.next:
            return head_node  # only 0 or 1 node, needn't reverse
        # now the singly linked list must have >= 2 nodes
        ptr_pre = head_node
        ptr = head_node.next
        head_node.next = None  # the former head_node is the new end_node, so its next is None
        while ptr.next:
            next_one = ptr.next  # record the next position of ptr
            ptr.next = ptr_pre  # link ptr -> ptr_pre (reverse link)
            ptr_pre = ptr  # move ptr_pre to current ptr position
            ptr = next_one  # move ptr to the recorded next position
        # now ptr.next is None, so ptr is the new head_node now
        ptr.next = ptr_pre  # the last reverse link
        head_node = ptr  # set new head_node
        return head_node


def main():
    # Example 1 Output: [5,4,3,2,1]
    head = [1, 2, 3, 4, 5]

    # Example 2: Output: [2,1]
    # head = [1, 2]

    # Example 3: Output: []
    # head = []

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverseList(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
