#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0141-Linked-List-Cycle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-03
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0141 - (Easy) - Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Description & Requirement:
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that 
    can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
    Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.

Follow up:
    Can you solve it using O(1) (i.e. constant) memory?
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # exception case
        if not isinstance(head, ListNode):
            return False  # Error head type
        if not isinstance(head.next, ListNode):
            return head.next == head  # only one element
        # main method: (same to LC-0142-Linked-List-Cycle-II)
        #     tow pointer, fast & slow, start from the same time, fast ptr moves 2 steps at a time
        return self._hasCycle(head)

    def _hasCycle(self, head_node: Optional[ListNode]) -> bool:
        """
        Runtime: 52 ms, faster than 94.92% of Python3 online submissions for Linked List Cycle.
        Memory Usage: 17.8 MB, less than 23.48% of Python3 online submissions for Linked List Cycle.
        """
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode)
        slow_ptr = head_node  # slow, moves 1 step at a time, from head
        fast_ptr = head_node  # slow, moves 2 step at a time, from head
        while isinstance(fast_ptr, ListNode):
            slow_ptr = slow_ptr.next  # slow moves 1 step
            if isinstance(fast_ptr.next, ListNode):  # check if fast can move 2 steps
                fast_ptr = fast_ptr.next.next
            else:
                return False  # fast reach end, no cycle
            if slow_ptr == fast_ptr:  # if there's a loop, fast and slow must meet each other
                # new_ptr = head_node  # create a new pointer from head
                # while new_ptr != slow_ptr:  # move new and slow till they meet
                #     new_ptr = new_ptr.next
                #     slow_ptr = slow_ptr.next
                return True  # when they meet, that is exactly the loop entrance
        return True  # actually, won't reach here


def main():
    # Example 1: Output: true
    head = [3, 2, 0, -4]
    pos = 1

    # Example 2: Output: true
    # head = [1, 2]
    # pos = 0

    # Example 3: Output: false
    # head = [1]
    # pos = -1

    head_node = ListNode.build_singly_linked_list_with_loop(head, pos)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.hasCycle(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)
    # ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
