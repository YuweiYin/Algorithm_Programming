#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0002-Add-Two-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-10
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0002 - (Medium) - Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Description & Requirement:
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]
Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
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
        while isinstance(ptr, ListNode):
            print(ptr.val)
            ptr = ptr.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(l1, ListNode):
            return l2
        if not isinstance(l2, ListNode):
            return l1
        # main method: (1. add number, modify val and next link in the longer list; 2. convert into integer and add.)
        return self._addTwoNumbers(l1, l2)

    def _addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 72 ms, faster than 86.11% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 14 MB, less than 65.79% of Python3 online submissions for Add Two Numbers.
        """
        assert isinstance(l1, ListNode) and isinstance(l2, ListNode)

        # convert linked list into integer and add
        def __convert_into_integer(ll: Optional[ListNode]) -> int:
            ptr = ll
            num = 0
            base = 1
            while isinstance(ptr, ListNode):
                num += ptr.val * base
                base *= 10
                ptr = ptr.next
            return num

        # add two integers
        num_1 = __convert_into_integer(l1)
        num_2 = __convert_into_integer(l2)
        num_sum = num_1 + num_2

        # let l1 be the longer linked list
        if num_1 < num_2:
            l1, l2 = l2, l1

        # modify l1
        head_val = num_sum % 10
        l1.val = head_val
        num_sum //= 10
        ptr_1 = l1
        while num_sum > 0:
            cur_val = num_sum % 10
            num_sum //= 10
            if isinstance(ptr_1.next, ListNode):  # if the next node exists, modify its value
                ptr_1.next.val = cur_val
            else:  # else, create the next node and get them linked together
                new_node = ListNode(val=cur_val)
                ptr_1.next = new_node
            ptr_1 = ptr_1.next

        return l1


def main():
    # Example 1: Output: [7,0,8]
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]

    # Example 2: Output: [0]
    # l1 = [0]
    # l2 = [0]

    # Example 3: Output: [8,9,9,9,0,0,0,1]
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]

    head_node_1 = ListNode.build_singly_linked_list(l1)
    head_node_2 = ListNode.build_singly_linked_list(l2)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.addTwoNumbers(head_node_1, head_node_2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
