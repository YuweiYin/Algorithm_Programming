#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1669-Merge-In-Between-Linked-Lists.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-30
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1669 - (Medium) - Merge In Between Linked Lists
https://leetcode.com/problems/merge-in-between-linked-lists/

Description & Requirement:
    You are given two linked lists: list1 and list2 of sizes n and m respectively.

    Remove list1's nodes from the a-th node to the b-th node, and put list2 in their place.

    The blue edges and nodes in the following figure indicate the result:

    Build the result list and return its head.

Example 1:
    Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
    Output: [0,1,2,1000000,1000001,1000002,5]
    Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. 
        The blue edges and nodes in the above figure indicate the result.
Example 2:
    Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
    Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    Explanation: The blue edges and nodes in the above figure indicate the result.

Constraints:
    3 <= list1.length <= 10^4
    1 <= a <= b < list1.length - 1
    1 <= list2.length <= 10^4
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
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # exception case
        assert isinstance(list1, ListNode) and isinstance(list2, ListNode)
        assert isinstance(a, int) and isinstance(b, int) and 1 <= a <= b
        # main method: (simulate the process)
        return self._mergeInBetween(list1, a, b, list2)

    def _mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        Time: beats 98.31%; Space: beats 95.64%
        """
        assert isinstance(list1, ListNode) and isinstance(list2, ListNode)
        assert isinstance(a, int) and isinstance(b, int) and 1 <= a <= b

        pre_a = list1
        for _ in range(a - 1):
            pre_a = pre_a.next

        pre_b = pre_a
        for _ in range(b - a + 2):
            pre_b = pre_b.next

        pre_a.next = list2
        while list2.next:
            list2 = list2.next

        list2.next = pre_b

        return list1


def main():
    # Example 1: Output: [0,1,2,1000000,1000001,1000002,5]
    list1 = [0, 1, 2, 3, 4, 5]
    a = 3
    b = 4
    list2 = [1000000, 1000001, 1000002]

    # Example 2: Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    # list1 = [0, 1, 2, 3, 4, 5, 6]
    # a = 2
    # b = 5
    # list2 = [1000000, 1000001, 1000002, 1000003, 1000004]

    head_node_1 = ListNode.build_singly_linked_list(list1)
    head_node_2 = ListNode.build_singly_linked_list(list2)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mergeInBetween(head_node_1, a, b, head_node_2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
