#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0023-Merge-k-Sorted-Lists.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-05
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0023 - (Hard) - Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Description & Requirement:
    You are given an array of k linked-lists lists, 
    each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6
Example 2:
    Input: lists = []
    Output: []
Example 3:
    Input: lists = [[]]
    Output: []

Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length won't exceed 10^4.
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # exception case
        if not isinstance(lists, list) or len(lists) <= 0:
            return None  # Error input type
        clear_lists = []
        for li in lists:  # clear null linked list
            if isinstance(li, ListNode):
                clear_lists.append(li)
        if len(clear_lists) <= 0:
            return None
        # main method: (1. Brute force: use a new list store all values, sort the list, then construct new linked list)
        #     (2. Divide & Conquer - Merge sort: each time merge two linked lists.  3. Priority Queue)
        return self._mergeKLists(clear_lists)  # Divide & Conquer - Merge sort.  Time: O(n log k),  Space: O(1)

    def _mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        len_lists = len(lists)
        assert len_lists > 0

        def __merge_sort_linked_list(l1: Optional[ListNode], l2: Optional[ListNode]):
            # l1 and l2 are guaranteed to be sorted linked list
            new_head = ListNode(val=int(1e9+7))
            merged_list = new_head
            ptr1 = l1
            ptr2 = l2

            # merge l1 and l2 into merged_list (this operation may reconstruct l1 and l2, but Space cost O(1))
            while isinstance(ptr1, ListNode) and isinstance(ptr2, ListNode):
                # each step, choose the node with smaller val
                if ptr1.val <= ptr2.val:
                    merged_list.next = ptr1
                    ptr1 = ptr1.next
                else:
                    merged_list.next = ptr2
                    ptr2 = ptr2.next
                merged_list = merged_list.next

            # deal with the rest nodes (either l1 or l2 has rest nodes), just link l1/l2 to the end of merged_list
            if isinstance(ptr1, ListNode):
                merged_list.next = ptr1
            else:
                merged_list.next = ptr2

            return new_head.next

        merge_interval = 1  # the interval of merge sort, 1 -> 2 -> 4 -> 8 -> ...

        while merge_interval < len_lists:
            # each outer loop, merge lists[i] and lists[i + merge_interval], and store the result into lists[i]
            # e.g., 8 lists, first outer loop: merge(0, 1) -> 0; merge(2, 3) -> 2; merge(4, 5) -> 4; merge(6, 7) -> 6;
            # second outer loop: merge(0, 2) -> 0; merge(4, 6) -> 4;
            # third outer loop: merge(0, 4) -> 0; done all.
            i = 0
            while i < len_lists - merge_interval:
                lists[i] = __merge_sort_linked_list(lists[i], lists[i + merge_interval])
                i += merge_interval << 1
            # expand merge_interval
            merge_interval <<= 1

        return lists[0]


def main():
    # Example 1: Output: [1,1,2,3,4,4,5,6]
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

    # Example 2: Output: []
    # lists = []

    # Example 3: Output: []
    # lists = [[]]

    head_node_list = [ListNode.build_singly_linked_list(li) for li in lists]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mergeKLists(head_node_list)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
