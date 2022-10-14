#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2095-Delete-the-Middle-Node-of-a-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-14
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 2095 - (Medium) - Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Description & Requirement:
    You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

    The middle node of a linked list of size n is the ⌊n / 2⌋-th node from the start using 0-based indexing, 
    where ⌊x⌋ denotes the largest integer less than or equal to x.

    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:
    Input: head = [1,3,4,7,1,2,6]
    Output: [1,3,4,1,2,6]
    Explanation:
        The above figure represents the given linked list. The indices of the nodes are written below.
        Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
        We return the new list after removing this node. 
Example 2:
    Input: head = [1,2,3,4]
    Output: [1,2,4]
    Explanation:
        The above figure represents the given linked list.
        For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:
    Input: head = [2,1]
    Output: [2]
    Explanation:
        The above figure represents the given linked list.
        For n = 2, node 1 with value 1 is the middle node, which is marked in red.
        Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    1 <= Node.val <= 10^5
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode) or not isinstance(head.next, ListNode):
            return None
        # main method: (fast/slow pointer)
        return self._deleteMiddle(head)

    def _deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 3036 ms, faster than 61.99% of Python3 submissions for Delete the Middle Node of a Linked List.
        Memory Usage: 59.8 MB, less than 95.69% of Python3 submissions for Delete the Middle Node of a Linked List.
        """
        assert isinstance(head, ListNode) and isinstance(head.next, ListNode)

        slow, fast, prev = head, head, None
        while isinstance(fast, ListNode) and isinstance(fast.next, ListNode):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = prev.next.next

        return head


def main():
    # Example 1: Output: [1,3,4,1,2,6]
    # head = [1, 3, 4, 7, 1, 2, 6]

    # Example 2: Output: [1,2,4]
    head = [1, 2, 3, 4]

    # Example 3: Output: [2]
    # head = [2, 1]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.deleteMiddle(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
