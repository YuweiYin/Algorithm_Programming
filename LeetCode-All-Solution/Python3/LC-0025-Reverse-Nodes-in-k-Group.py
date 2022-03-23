#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0025-Reverse-Nodes-in-k-Group.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-23
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0025 - (Hard) - Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Description & Requirement:
    Given the head of a linked list, reverse the nodes of the list k at a time, 
    and return the modified list.

    k is a positive integer and is less than or equal to the length of the linked list. 
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

Follow-up:
    Can you solve the problem in O(1) extra memory space?
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        if not isinstance(head.next, ListNode):
            return head  # only one element
        if k <= 1:
            return head
        # main method: (in-place reverse group)
        return self._reverseKGroup(head, k)

    def _reverseKGroup(self, head_node: Optional[ListNode], k: int) -> Optional[ListNode]:
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode) and k >= 2

        pseudo_head = ListNode(val=sys.maxsize, next=head_node)

        start = pseudo_head
        end = pseudo_head.next
        left, right, temp = head_node, head_node, head_node
        # start->left->right->...->end

        while isinstance(end, ListNode):
            # move end
            move_count = 0
            while move_count < k:
                if isinstance(end, ListNode):
                    end = end.next
                    move_count += 1
                else:
                    break
            if move_count < k:
                break

            # move right
            if isinstance(right.next, ListNode):
                right = right.next
            else:
                break

            # reverse each two adjacent nodes: left and right
            while right != end:
                # change left->right to right->left
                temp = right.next
                right.next = left
                # move on
                left = right
                right = temp

            # change the link of start and end
            # now: start->node_1<->node_2<-...<-node_k  end->  (node_k is `left`, `end` is `right`)
            start.next.next = end
            temp = start.next
            start.next = left

            # move on, for next loop
            start = temp
            left = end

        return pseudo_head.next


def main():
    # Example 1: Output: [2,1,4,3,5]
    # head = [1, 2, 3, 4, 5]
    # k = 2

    # Example 2: Output: [3,2,1,4,5]
    head = [1, 2, 3, 4, 5]
    k = 3

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverseKGroup(head_node, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans.val)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
