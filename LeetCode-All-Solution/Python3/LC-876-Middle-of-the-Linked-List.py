#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-876-Middle-of-the-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-05
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 876 - (Easy) - Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Description & Requirement:
    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.
Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100
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


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if (not isinstance(head, ListNode)) and (head is not None):
            return None  # Error head type
        # main method: (two pointer: tht fast pointer moves 2 steps at a time, while the slow one moves 1 step.)
        return self._middleNode(head)

    def _middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = fast_ptr = head  # both start from the head node
        while fast_ptr and fast_ptr.next:  # loop condition: the next of fast is not None; end condition: fast is None
            slow_ptr = slow_ptr.next  # moves one step
            fast_ptr = fast_ptr.next.next  # moves two steps
        return slow_ptr


def main():
    # Example 1: Output: [3,4,5]
    head = [1, 2, 3, 4, 5]

    # Example 2: Output: [4,5,6]
    # head = [1, 2, 3, 4, 5, 6]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.middleNode(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans.val)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
