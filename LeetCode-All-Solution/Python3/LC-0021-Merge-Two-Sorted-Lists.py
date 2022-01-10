#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0021-Merge-Two-Sorted-Lists.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-10
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0021 - (Easy) - Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Description & Requirement:
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. 
    The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
Example 2:
    Input: list1 = [], list2 = []
    Output: []
Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if (not isinstance(list1, ListNode)) and (list1 is not None):
            return None  # Error head type
        if (not isinstance(list2, ListNode)) and (list2 is not None):
            return None  # Error head type
        if not isinstance(list1, ListNode):
            return list2
        if not isinstance(list2, ListNode):
            return list1
        # main method: (scan from head to tail, compare value, link together)
        return self._mergeTwoLists(list1, list2)

    def _mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        assert isinstance(list1, ListNode) and isinstance(list2, ListNode)
        if list1.val > list2.val:  # swap the two heads, make sure that list1.val <= list2.val
            temp = list1
            list1 = list2
            list2 = temp
        pre_ptr1 = list1
        ptr1 = list1.next
        # pre_ptr2 = list2
        # ptr2 = list2.next
        ptr2 = list2

        while isinstance(ptr1, ListNode) and isinstance(ptr2, ListNode):
            if ptr1.val <= ptr2.val:  # in this case, ptr2.val can insert between pre_ptr1 and ptr1, list1 move
                pre_ptr1 = ptr1
                ptr1 = ptr1.next
            else:  # in this case, ptr2.val should be inserted between pre_ptr1 and ptr1
                old_ptr2_next = ptr2.next  # record
                pre_ptr1.next = ptr2  # link
                ptr2.next = ptr1  # link
                pre_ptr1 = ptr2  # pre_ptr1 moves, while ptr1 stays
                ptr2 = old_ptr2_next  # ptr2 moves

        if not isinstance(ptr2, ListNode):  # list2 has been used up
            return list1

        if not isinstance(ptr1, ListNode):  # list1 has been used up but list2 has not
            assert isinstance(pre_ptr1, ListNode)
            pre_ptr1.next = ptr2  # just link the rest list2 (must > all list1) to the end of list1

        return list1


def main():
    # Example 1: Output: [1,1,2,3,4,4]
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    # Example 2: Output: []
    # list1 = []
    # list2 = []

    # Example 3: Output: [0]
    # list1 = []
    # list2 = [0]

    head_node1 = ListNode.build_singly_linked_list(list1)
    head_node2 = ListNode.build_singly_linked_list(list2)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mergeTwoLists(head_node1, head_node2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
