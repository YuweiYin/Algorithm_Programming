#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0234-Palindrome-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-23
=================================================================="""

import sys
import time
from typing import Optional
# from typing import List
# import collections
# import functools

"""
LeetCode - 0234 - (Easy) - Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Description & Requirement:
    Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
    Input: head = [1,2,2,1]
    Output: true
Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9

Follow up:
    Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # exception case
        if not isinstance(head, ListNode):
            return False
        if not isinstance(head.next, ListNode):
            return True
        # main method: (two pointers: use a fast and a slow pointer to find the mid of the linked list)
        return self._isPalindrome(head)

    def _isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Runtime: 1539 ms, faster than 15.73% of Python3 online submissions for Palindrome Linked List.
        Memory Usage: 39 MB, less than 84.51% of Python3 online submissions for Palindrome Linked List.
        """
        assert isinstance(head, ListNode)

        pseudo_head = ListNode(next=head)
        fast, slow = pseudo_head, pseudo_head
        f_steps, s_steps = 0, 0
        while isinstance(fast.next, ListNode):
            slow = slow.next
            s_steps += 1
            fast = fast.next
            f_steps += 1
            if isinstance(fast, ListNode) and isinstance(fast.next, ListNode):
                fast = fast.next
                f_steps += 1
            else:
                break

        # print(f_steps)
        # print(s_steps)

        def __reverse_list(start_head: ListNode):
            ptr = start_head.next
            assert isinstance(ptr, ListNode)
            ptr_next = ptr.next
            while isinstance(ptr_next, ListNode):
                tmp = ptr_next.next
                ptr_next.next = ptr
                ptr = ptr_next
                ptr_next = tmp

        __reverse_list(slow)

        if f_steps & 0x01 == 1:
            left_ptr = head
            right_ptr = fast
            while left_ptr != slow:
                if left_ptr.val != right_ptr.val:
                    return False
                left_ptr = left_ptr.next
                right_ptr = right_ptr.next
        else:
            left_ptr = head
            right_ptr = fast
            while left_ptr != slow.next:
                if left_ptr.val != right_ptr.val:
                    return False
                left_ptr = left_ptr.next
                right_ptr = right_ptr.next

        return True


def main():
    # Example 1: Output: true
    # head = [1, 2, 2, 1]

    # Example 2: Output: false
    # head = [1, 2]

    node_1 = ListNode(val=1)
    node_2 = ListNode(val=2, next=node_1)
    # node_3 = ListNode(val=2, next=node_2)
    node_4 = ListNode(val=2, next=node_2)
    node_5 = ListNode(val=1, next=node_4)
    head = node_5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPalindrome(head)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
