#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0445-Add-Two-Numbers-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-03
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools
# import itertools

"""
LeetCode - 0445 - (Easy) - Add Two Numbers II
https://leetcode.com/problems/add-two-numbers-ii/

Description & Requirement:
    You are given two non-empty linked lists representing two non-negative integers. 
    The most significant digit comes first and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [7,2,4,3], l2 = [5,6,4]
    Output: [7,8,0,7]
Example 2:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [8,0,7]
Example 3:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

Follow up:
    Could you solve it without reversing the input lists?
"""


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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        assert isinstance(l1, ListNode)
        assert isinstance(l2, ListNode)
        # main method: (stack)
        return self._addTwoNumbers(l1, l2)

    def _addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        assert isinstance(l1, ListNode)
        assert isinstance(l2, ListNode)

        stack_1, stack_2 = [], []
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_2.append(l2.val)
            l2 = l2.next

        res = None
        carry = 0
        while stack_1 or stack_2 or carry != 0:
            digit_1 = 0 if not stack_1 else stack_1.pop()
            digit_2 = 0 if not stack_2 else stack_2.pop()

            cur_sum = digit_1 + digit_2 + carry
            carry = cur_sum // 10
            cur_sum %= 10

            ptr = ListNode(cur_sum)
            ptr.next = res
            res = ptr

        return res


def main():
    # Example 1: Output: [7,8,0,7]
    l1 = [7, 2, 4, 3]
    l2 = [5, 6, 4]

    # Example 2: Output: [8,0,7]
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]

    # Example 3: Output: [0]
    # l1 = [0]
    # l2 = [0]

    l1_list = ListNode.build_singly_linked_list(l1)
    l2_list = ListNode.build_singly_linked_list(l2)

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.addTwoNumbers(l1_list, l2_list)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
