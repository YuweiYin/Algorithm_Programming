#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0061-Rotate-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-11
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0061 - (Medium) - Rotate List
https://leetcode.com/problems/rotate-list/

Description & Requirement:
    Given the head of a linked list, 
    rotate the list to the right by k places.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        if not isinstance(head.next, ListNode):
            return head  # only one element
        assert isinstance(k, int) and k >= 0
        if k == 0:
            return head
        # main method: (scan, record the head, tail, and K-th node, where K = k % len(singly-linked list))
        return self._rotateRight(head, k)

    def _rotateRight(self, head_node: Optional[ListNode], k: int) -> Optional[ListNode]:
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode)

        pseudo_head = ListNode(val=sys.maxsize, next=head_node)  # Constraint: -100 <= Node.val <= 100

        tail = pseudo_head
        sll_len = 0
        while isinstance(tail.next, ListNode):  # get len(singly-linked list)
            sll_len += 1
            tail = tail.next
        # now ptr is the tail node
        k %= sll_len
        if k == 0:
            return head_node

        # find the two breaking nodes
        breaking_left = pseudo_head
        step_counter = sll_len - k
        for _ in range(step_counter):
            breaking_left = breaking_left.next
        breaking_right = breaking_left.next

        # head...breaking_left  breaking_right...tail  ->  breaking_right...tail  head...breaking_left
        pseudo_head.next = breaking_right
        breaking_left.next = None
        tail.next = head_node

        return pseudo_head.next


def main():
    # Example 1: Output: [4,5,1,2,3]
    # head = [1, 2, 3, 4, 5]
    # k = 2

    # Example 2: Output: [2,0,1]
    head = [0, 1, 2]
    k = 4

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rotateRight(head_node, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
