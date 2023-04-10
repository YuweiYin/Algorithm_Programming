#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1019-Next-Greater-Node-In-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-10
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 1019 - (Medium) - Next Greater Node In Linked List
https://leetcode.com/problems/next-greater-node-in-linked-list/

Description & Requirement:
    You are given the head of a linked list with n nodes.

    For each node in the list, find the value of the next greater node. 
    That is, for each node, find the value of the first node that 
    is next to it and has a strictly larger value than it.

    Return an integer array answer where answer[i] is the value of the next greater node 
    of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Example 1:
    Input: head = [2,1,5]
    Output: [5,5,0]
Example 2:
    Input: head = [2,7,4,3,5]
    Output: [7,0,5,5,0]

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 10^4
    1 <= Node.val <= 10^9
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
        val_list = []
        while ptr:
            val_list.append(ptr.val)
            ptr = ptr.next
        print(val_list)


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # exception case
        if not isinstance(head, ListNode):
            return []
        # main method: (monotonous stack)
        return self._nextLargerNodes(head)

    def _nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        pseudo_head = ListNode(val=int(1e9+7), next=head)

        res = []
        stack = []
        ptr = head
        idx = -1
        while isinstance(ptr, ListNode):
            idx += 1
            res.append(0)
            while len(stack) > 0 and stack[-1][0] < ptr.val:
                res[stack[-1][1]] = ptr.val
                stack.pop()
            stack.append((ptr.val, idx))
            ptr = ptr.next

        return res


def main():
    # Example 1: Output: [5,5,0]
    # head = [2, 1, 5]

    # Example 2: Output: [7,0,5,5,0]
    head = [2, 7, 4, 3, 5]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nextLargerNodes(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
