#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-19-Remove-Nth-Node-From-End-of-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-05
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 19 - (Medium) - Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Description & Requirement:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
Example 2:
    Input: head = [1], n = 1
    Output: []
Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # exception case
        if (not isinstance(head, ListNode)) and (head is not None):
            return None  # Error head type
        if not isinstance(n, int) or n <= 0:
            return None  # Error n type or needn't delete
        # main method: (reverse the singly linked list twice, remove the n-th node before/in the second reversal)
        # other good ideas:
        #     1. fast/slow pointer, both move 1 step at a time, but fast_ptr has moved n steps at the beginning.
        #     2. first scan count the length of the list (say, L), second scan delete the (L - n)-th node.
        #     3. first scan store all nodes in a stack (list append/pop), second scan delete the n-th node from stack.
        return self._removeNthFromEnd(head, n)

    def _removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = self._reverse_singly_linked_list(head)  # reverse
        head_after_delete = self._delete_nth_node_in_singly_linked_list(new_head, n)  # delete
        recovered_head = self._reverse_singly_linked_list(head_after_delete)  # reverse again
        return recovered_head

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

    @staticmethod
    def _delete_nth_node_in_singly_linked_list(head_node: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (not isinstance(head_node, ListNode)) and (head_node is not None):
            return head_node  # Error head_node type
        if not isinstance(head_node, ListNode):
            return head_node  # Error head_node type
        if not isinstance(n, int) or n <= 0:
            return head_node  # Error n type or needn't delete
        if n == 1:  # border case
            delete_node = head_node  # identify delete_node
            head_node = head_node.next  # change head_node
            delete_node.next = None  # unlink delete_node
            del delete_node  # del delete_node
            return head_node
        # now n must >= 2
        if not head_node.next:
            return head_node  # n is larger than list length
        if n == 2:  # border case
            delete_node = head_node.next  # identify delete_node
            head_node.next = delete_node.next  # skip delete_node, create new link
            delete_node.next = None  # unlink delete_node
            del delete_node  # del delete_node
            return head_node
        # now n must >= 3 and head_node.next is not None
        ptr_pre = head_node
        ptr = head_node.next
        ptr_nth = 2  # indicate ptr is the n-th node at the moment
        while ptr_nth < n:  # move until ptr_nth == n, or stop earlier because of out of range
            if not ptr.next:
                return head_node  # n is larger than list length
            ptr_pre = ptr  # record the previous node of ptr in order to reconstruct the link (skip delete_node)
            ptr = ptr.next
            ptr_nth += 1

        # now ptr is the one that need to be deleted
        delete_note = ptr  # identify delete_node
        ptr_pre.next = delete_note.next  # skip delete_node, create new link
        delete_note.next = None  # unlink delete_node
        del delete_note  # del delete_node
        return head_node


def main():
    # Example 1: Output: [1,2,3,5]
    head = [1, 2, 3, 4, 5]
    n = 2

    # Example 2: Output: []
    # head = [1]
    # n = 1

    # Example 3: Output: [1]
    # head = [1, 2]
    # n = 1

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeNthFromEnd(head_node, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
