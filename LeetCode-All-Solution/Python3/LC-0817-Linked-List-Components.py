#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0817-Linked-List-Components.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-12
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections
# import functools

"""
LeetCode - 0817 - (Medium) - Linked List Components
https://leetcode.com/problems/linked-list-components/

Description & Requirement:
    You are given the head of a linked list containing unique integer values and an integer array nums 
    that is a subset of the linked list values.

    Return the number of connected components in nums where two values are connected 
    if they appear consecutively in the linked list.

Example 1:
    Input: head = [0,1,2,3], nums = [0,1,3]
    Output: 2
    Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:
    Input: head = [0,1,2,3,4], nums = [0,3,1,4]
    Output: 2
    Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Constraints:
    The number of nodes in the linked list is n.
    1 <= n <= 10^4
    0 <= Node.val < n
    All the values Node.val are unique.
    1 <= nums.length <= n
    0 <= nums[i] < n
    All the values of nums are unique.
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
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # exception case
        if not isinstance(head, ListNode):
            return 0
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 0
        # main method: (hash set, count the number of consecutive nodes)
        return self._numComponents(head, nums)

    def _numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        assert isinstance(head, ListNode)
        assert isinstance(nums, list) and len(nums) >= 1

        nums_set = set(nums)
        is_in_set = False
        res = 0

        ptr = head
        while isinstance(ptr, ListNode):
            if ptr.val not in nums_set:
                is_in_set = False
            elif not is_in_set:
                is_in_set = True
                res += 1
            ptr = ptr.next

        return res


def main():
    # Example 1: Output: 2
    # head = [0, 1, 2, 3]
    # nums = [0, 1, 3]

    # Example 2: Output: 2
    head = [0, 1, 2, 3, 4]
    nums = [0, 3, 1, 4]

    head_node = ListNode.build_singly_linked_list(head)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numComponents(head_node, nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
