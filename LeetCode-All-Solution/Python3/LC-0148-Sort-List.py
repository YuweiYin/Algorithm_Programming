#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0148-Sort-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-24
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0148 - (Medium) - Sort List
https://leetcode.com/problems/sort-list/

Description & Requirement:
    Given the head of a linked list, 
    return the list after sorting it in ascending order.

Example 1:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]
Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 5 * 10^4].
    -10^5 <= Node.val <= 10^5

Follow up:
    Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        if not isinstance(head.next, ListNode):
            return head
        # main method: (Divide & Conquer, inplace, fast/slow two pointers to find the middle node)
        return self._sortList(head)

    def _sortList(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode)
        # null_head = ListNode(val=0, next=head_node)

        def __combine_sorted_singly_linked_list(
                sll_1: Optional[ListNode], sll_2: Optional[ListNode]) -> Optional[ListNode]:
            if not isinstance(sll_1, ListNode):
                return sll_2
            if not isinstance(sll_2, ListNode):
                return sll_1
            # set sll_1 as the lower head value one, merge sll_2 into sll_1, no extra space consumption
            if sll_1.val > sll_2.val:
                sll_1, sll_2 = sll_2, sll_1
            ptr_sll_1, ptr_sll_1_next = sll_1, sll_1.next
            ptr_sll_2 = sll_2
            while isinstance(ptr_sll_1_next, ListNode) and isinstance(ptr_sll_2, ListNode):
                if ptr_sll_1_next.val > ptr_sll_2.val:
                    # link ptr_sll_1 -> ptr_sll_2 -> ptr_sll_1_next
                    ptr_sll_2_next = ptr_sll_2.next  # record
                    ptr_sll_1.next = ptr_sll_2
                    ptr_sll_1.next.next = ptr_sll_1_next
                    # pointer moves on
                    ptr_sll_1 = ptr_sll_1.next
                    ptr_sll_2 = ptr_sll_2_next
                else:
                    # don't change link, just move on
                    ptr_sll_1 = ptr_sll_1_next
                    ptr_sll_1_next = ptr_sll_1_next.next
            # if ptr_sll_2 has rest elements, just link them to the end of ptr_sll_1
            if isinstance(ptr_sll_2, ListNode):
                ptr_sll_1.next = ptr_sll_2
            return sll_1

        def __divide_and_conquer(cur_head: Optional[ListNode]) -> Optional[ListNode]:
            if not isinstance(cur_head, ListNode):  # no nodes
                return None
            if not isinstance(cur_head.next, ListNode):  # only one node
                cur_head.next = None  # cut the link with other nodes
                return cur_head
            if not isinstance(cur_head.next.next, ListNode):  # only two nodes
                if cur_head.val <= cur_head.next.val:
                    cur_head.next.next = None  # cut the link with other nodes
                    return cur_head
                else:
                    c_h_n = cur_head.next
                    c_h_n.next = cur_head
                    cur_head.next = None  # cut the link with other nodes
                    return c_h_n
            ptr_fast, ptr_slow = cur_head, cur_head
            while isinstance(ptr_fast, ListNode) and isinstance(ptr_fast.next, ListNode):
                ptr_fast = ptr_fast.next.next
                ptr_slow = ptr_slow.next
            # now ptr_slow is the middle node
            # divide (set ptr_slow.next = None)
            ptr_slow_next = ptr_slow.next
            ptr_slow.next = None

            # conquer separately
            left_res = __divide_and_conquer(cur_head)
            right_res = __divide_and_conquer(ptr_slow_next)

            # combine results
            return __combine_sorted_singly_linked_list(left_res, right_res)

        return __divide_and_conquer(head_node)


def main():
    # Example 1: Output: [-1,0,3,4,5]
    head = [-1, 5, 3, 4, 0]

    # Example 3: Output: []
    # head = []

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sortList(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
