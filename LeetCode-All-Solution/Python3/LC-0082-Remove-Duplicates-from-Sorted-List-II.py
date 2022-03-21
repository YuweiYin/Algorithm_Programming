#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0082-Remove-Duplicates-from-Sorted-List-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-16
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0082 - (Medium) - Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Description & Requirement:
    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
    leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]
Example 2:
    Input: head = [1,1,1,2,3]
    Output: [2,3]

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        if not isinstance(head.next, ListNode):
            return head  # only one element
        if not isinstance(head.next.next, ListNode):
            return None if head.val == head.next.val else head  # only two element
        # main method: (three pointers, in-place delete)
        return self._deleteDuplicates(head)

    def _deleteDuplicates(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 44 ms, faster than 86.84% of Python3 online submissions for Remove Duplicates from Sorted List II.
        Memory Usage: 13.9 MB, less than 35.92% of Python3 online submissions for Remove Duplicates from Sorted List II.
        """
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode) and \
               isinstance(head_node.next.next, ListNode)

        pseudo_head = ListNode(val=sys.maxsize, next=head_node)

        ptr = pseudo_head
        while isinstance(ptr.next, ListNode) and isinstance(ptr.next.next, ListNode):
            if ptr.next.val == ptr.next.next.val:
                same_val = ptr.next.val  # record the same val
                while isinstance(ptr.next, ListNode) and ptr.next.val == same_val:
                    next_node = ptr.next.next
                    del ptr.next
                    ptr.next = next_node  # change link
            else:
                ptr = ptr.next  # move on

        return pseudo_head.next


def main():
    # Example 1: Output: [1,2,5]
    # head = [1, 2, 3, 3, 4, 4, 5]

    # Example 2: Output: [2,3]
    head = [1, 1, 1, 2, 3]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.deleteDuplicates(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
