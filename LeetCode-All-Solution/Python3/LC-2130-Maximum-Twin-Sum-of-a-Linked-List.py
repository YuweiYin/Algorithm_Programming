#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2130-Maximum-Twin-Sum-of-a-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-17
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 2130 - (Medium) - Maximum Twin Sum of a Linked List
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

Description & Requirement:
    In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list 
    is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. 
    These are the only nodes with twins for n = 4.

    The twin sum is defined as the sum of a node and its twin.

    Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example 1:
    Input: head = [5,4,2,1]
    Output: 6
    Explanation:
        Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
        There are no other nodes with twins in the linked list.
        Thus, the maximum twin sum of the linked list is 6. 
Example 2:
    Input: head = [4,2,2,3]
    Output: 7
    Explanation:
        The nodes with twins present in this linked list are:
        - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
        - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
        Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:
    Input: head = [1,100000]
    Output: 100001
    Explanation:
        There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

Constraints:
    The number of nodes in the list is an even integer in the range [2, 10^5].
    1 <= Node.val <= 10^5
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        # exception case
        assert isinstance(head, ListNode) and head.val >= 1
        # main method: (fast/slow pointers)
        return self._pairSum(head)

    def _pairSum(self, head: Optional[ListNode]) -> int:
        assert isinstance(head, ListNode) and head.val >= 1

        slow, fast = head, head.next
        while isinstance(fast.next, ListNode):
            slow = slow.next
            fast = fast.next.next

        # reverse the linked-list
        last = slow.next
        while isinstance(last.next, ListNode):
            ptr = last.next
            last.next = ptr.next
            ptr.next = slow.next
            slow.next = ptr

        res = 0
        x, y = head, slow.next
        while isinstance(y, ListNode):
            res = max(res, x.val + y.val)
            x, y = x.next, y.next

        return res


def main():
    # Example 1: Output: 6
    head = [5, 4, 2, 1]

    # Example 2: Output: 7
    # head = [4, 2, 2, 3]

    # Example 3: Output: 100001
    # head = [1, 100000]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pairSum(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
