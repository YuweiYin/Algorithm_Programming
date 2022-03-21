#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0160-Intersection-of-Two-Linked-Lists.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-21
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0160 - (Easy) - Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Description & Requirement:
    Given the heads of two singly linked-lists headA and headB, 
    return the node at which the two lists intersect. 
    If the two linked lists have no intersection at all, return null.

    For example, the following two linked lists begin to intersect at node c1:
    The test cases are generated such that there are no cycles anywhere in the entire linked structure.

    Note that the linked lists must retain their original structure after the function returns.

    Custom Judge:
        The inputs to the judge are given as follows (your program is not given these inputs):
            intersectVal - The value of the node where the intersection occurs. 
                This is 0 if there is no intersected node.
            listA - The first linked list.
            listB - The second linked list.
            skipA - The number of nodes to skip ahead in listA (starting from the head) 
                to get to the intersected node.
            skipB - The number of nodes to skip ahead in listB (starting from the head) 
                to get to the intersected node.
        The judge will then create the linked structure based on these inputs 
        and pass the two heads, headA and headB to your program. 
        If you correctly return the intersected node, then your solution will be accepted.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'
    Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
        From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'
    Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
        From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection
    Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    Explanation: The two lists do not intersect, so return null.

Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 10^4
    1 <= Node.val <= 10^5
    0 <= skipA < m
    0 <= skipB < n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up:
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # exception case
        if not isinstance(headA, ListNode) or not isinstance(headB, ListNode):
            return None  # Error head type
        # main method: (each step, ptrA and ptrB move to its next, if the next node is None, go to the other list)
        #     if two pointers meet, then that's the joint, else return None
        return self._getIntersectionNode(headA, headB)

    def _getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        assert isinstance(headA, ListNode) and isinstance(headB, ListNode)

        ptrA = headA
        ptrB = headB

        meet_end_a = False  # has traversed the end node of list A
        meet_end_b = False  # has traversed the end node of list B
        while isinstance(ptrA, ListNode) and isinstance(ptrB, ListNode):
            if ptrA == ptrB:
                return ptrA
            # pointer A
            if isinstance(ptrA.next, ListNode):
                ptrA = ptrA.next
            else:
                if meet_end_a:  # can't change list twice
                    return None
                else:  # change list
                    meet_end_a = True
                    ptrA = headB
            # pointer B
            if isinstance(ptrB.next, ListNode):
                ptrB = ptrB.next
            else:
                if meet_end_b:  # can't change list twice
                    return None
                else:  # change list
                    meet_end_b = True
                    ptrB = headA

        return None


def main():
    # Example 1: Output: Intersected at '8'
    # intersectVal = 8
    # listA = [4, 1, 8, 4, 5]
    # listB = [5, 6, 1, 8, 4, 5]
    # skipA = 2
    # skipB = 3

    # Example 2: Output: Intersected at '2'
    # intersectVal = 2
    # listA = [1, 9, 1, 2, 4]
    # listB = [3, 2, 4]
    # skipA = 3
    # skipB = 1

    # Example 3: Output: No intersection
    intersectVal = 0
    listA = [2, 6, 4]
    listB = [1, 5]
    skipA = 3
    skipB = 2

    head_node_a = ListNode.build_singly_linked_list(listA)
    head_node_b = ListNode.build_singly_linked_list(listB)
    ptr_a = head_node_a  # go to the parent node of the intersectVal in listA
    for _ in range(skipA - 1):
        if not isinstance(ptr_a, ListNode):
            break
        ptr_a = ptr_a.next
    ptr_b = head_node_b  # go to the parent node of the intersectVal in listB
    for _ in range(skipB - 1):
        if not isinstance(ptr_b, ListNode):
            break
        ptr_b = ptr_b.next
    if isinstance(ptr_a.next, ListNode) and isinstance(ptr_b.next, ListNode):  # link
        assert ptr_a.next.val == ptr_b.next.val == intersectVal
        ptr_a.next = ptr_b.next

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getIntersectionNode(head_node_a, head_node_b)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    if isinstance(ans, ListNode):
        print(ans.val)
        # ListNode.show_val_singly_linked_list(ans)
    else:
        print("null")

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
