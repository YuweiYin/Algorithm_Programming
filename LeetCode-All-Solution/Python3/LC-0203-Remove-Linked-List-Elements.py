#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0203-Remove-Linked-List-Elements.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-03
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0203 - (Easy) - Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Description & Requirement:
    Given the head of a linked list and an integer val, 
    remove all the nodes of the linked list that has Node.val == val, 
    and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
Example 2:
    Input: head = [], val = 1
    Output: []
Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 10^4].
    1 <= Node.val <= 50
    0 <= val <= 50
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
        while ptr:
            print(ptr.val)
            ptr = ptr.next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        if not isinstance(head.next, ListNode):
            return head if head.val != val else None  # only one element
        # main method: (scan and delete, change links)
        return self._removeElements(head, val)

    def _removeElements(self, head_node: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Runtime: 68 ms, faster than 92.73% of Python3 online submissions for Remove Linked List Elements.
        Memory Usage: 17.8 MB, less than 26.88% of Python3 online submissions for Remove Linked List Elements.
        """
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode)
        null_head = ListNode(val=val, next=head_node)
        ptr_left = null_head
        ptr_right = head_node
        while isinstance(ptr_right, ListNode):
            if ptr_right.val == val:
                # reconstruct link and del target node
                ptr_left.next = ptr_right.next
                del ptr_right
                ptr_right = ptr_left.next
            else:
                # just move on
                ptr_left = ptr_left.next
                ptr_right = ptr_right.next

        return None if not isinstance(null_head.next, ListNode) else null_head.next


def main():
    # Example 1: Output: [1,2,3,4,5]
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6

    # Example 2: Output: []
    # head = []
    # val = 1

    # Example 3: Output: []
    # head = [7, 7, 7, 7]
    # val = 7

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeElements(head_node, val)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
