#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0142-Linked-List-Cycle-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-19
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0142 - (Medium) - Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

Description & Requirement:
    Given the head of a linked list, return the node where the cycle begins. 
    If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list 
    that can be reached again by continuously following the next pointer. 
    Internally, `pos` is used to denote the index of the node that 
    tail's next pointer is connected to (0-indexed). 
    It is -1 if there is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exception case
        if not isinstance(head, ListNode):
            return None  # Error head type
        if not isinstance(head.next, ListNode):
            return head if head.next == head else None  # only one element
        # main method: (tow pointer, fast & slow, start from the same time, fast ptr moves 2 steps at a time)
        #              (when slow ptr can move to the late half of the linked list, it means there must be a cycle)
        #              (when there's a cycle, fast ptr and slow ptr will meet before slow ptr finish the first cycle)
        #              (X: distance from head_node to loop_enter_node.  Y: distance from loop_enter_node to f_s_meet.)
        #              (Z: loop length - B.  k: before meet the slow ptr, how many loops has the fast ptr traveled.)
        #              (when meet, slow ptr has traveled (X+Y), while fast ptr has traveled (X + Y + k*(Y+Z))  )
        #              (so there's an equation: 2 * (X + Y) = (X + Y + k*(Y+Z)), so  X = Z + (k-1)*(Y+Z) )
        #              (now, if a new ptr starts from head and moves 1 step at a time, slow keep moving too)
        #              (when new ptr reach loop entrance, it has moved X steps, and slow has moved Z+(k-1)*(Y+Z) steps.)
        #              (therefore, the total travel distance of slow is X+Y + Z+(k-1)*(Y+Z) == X + k*(Y+Z) )
        #              ((Y+Z) is loop length, so new ptr and slow ptr must meet exactly at the loop entrance node.)
        # other idea (space O(n)): just scan the linked list, store nodes(vals) in dict, check if any node will repeat
        return self._detectCycle(head)

    def _detectCycle(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        assert isinstance(head_node, ListNode) and isinstance(head_node.next, ListNode)
        slow_ptr = head_node  # slow, moves 1 step at a time, from head
        fast_ptr = head_node  # slow, moves 2 step at a time, from head
        while isinstance(fast_ptr, ListNode):
            slow_ptr = slow_ptr.next  # slow moves 1 step
            if isinstance(fast_ptr.next, ListNode):  # check if fast can move 2 steps
                fast_ptr = fast_ptr.next.next
            else:
                return None  # fast reach end, no cycle
            if slow_ptr == fast_ptr:  # if there's a loop, fast and slow must meet each other
                new_ptr = head_node  # create a new pointer from head
                while new_ptr != slow_ptr:  # move new and slow till they meet
                    new_ptr = new_ptr.next
                    slow_ptr = slow_ptr.next
                return new_ptr  # when they meet, that is exactly the loop entrance
        return None  # actually, won't reach here


def main():
    # Example 1: Output: tail connects to node index 1
    # head = [3, 2, 0, -4]
    # pos = 1

    # Example 2: Output: tail connects to node index 0
    # head = [1, 2]
    # pos = 0

    # Example 3: Output: no cycle
    head = [1]
    pos = -1

    head_node = ListNode.build_singly_linked_list_with_loop(head, pos)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.detectCycle(head_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    if isinstance(ans, ListNode):
        print(ans.val)
    else:
        print("No cycle.")
    # ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
