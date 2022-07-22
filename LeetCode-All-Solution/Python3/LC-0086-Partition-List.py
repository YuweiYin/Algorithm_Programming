#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0086-Partition-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-22
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0086 - (Medium) - Partition List
https://leetcode.com/problems/partition-list/

Description & Requirement:
    Given the head of a linked list and a value x, partition it such that 
    all nodes less than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None
        assert isinstance(x, int)
        # main method: (record values in a list/array and then deal with it)
        return self._partition(head, x)

    def _partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Runtime: 32 ms, faster than 97.86% of Python3 online submissions for Partition List.
        Memory Usage: 14 MB, less than 31.57% of Python3 online submissions for Partition List.
        """
        assert isinstance(head, ListNode) and isinstance(x, int)

        all_val = []
        ptr = head
        while isinstance(ptr, ListNode):
            all_val.append(ptr.val)
            ptr = ptr.next

        left_val = []
        right_val = []
        for val in all_val:
            if val < x:
                left_val.append(val)
            else:
                right_val.append(val)

        all_val = left_val + right_val
        ptr = head
        idx = 0
        while isinstance(ptr, ListNode):
            ptr.val = all_val[idx]
            ptr = ptr.next
            idx += 1

        return head


def main():
    # Example 1: Output: [1,2,2,4,3,5]
    head = [1, 4, 3, 2, 5, 2]
    x = 3

    # Example 2: Output: [1,2]
    # head = [2, 1]
    # x = 2

    head = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.partition(head, x)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(head)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
