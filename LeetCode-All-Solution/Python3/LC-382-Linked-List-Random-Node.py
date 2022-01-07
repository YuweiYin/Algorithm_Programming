#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-382-Linked-List-Random-Node.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-07
=================================================================="""

import sys
import time
import random
from typing import List, Optional

"""
LeetCode - 382 - (Medium) - Linked List Random Node
https://leetcode.com/problems/linked-list-random-node/

Description & Requirement:
    Given a singly linked list, return a random node's value from the linked list. 
    Each node must have the same probability of being chosen.
    
    Implement the Solution class:
        1. Solution(ListNode head) Initializes the object with the integer array nums.
        2. int getRandom() Chooses a node randomly from the list and returns its value. 
            All the nodes of the list should be equally likely to be choosen.

Example 1:
    Input
        ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
        [[[1, 2, 3]], [], [], [], [], []]
    Output
        [null, 1, 3, 2, 2, 3]
    Explanation
        Solution solution = new Solution([1, 2, 3]);
        solution.getRandom(); // return 1
        solution.getRandom(); // return 3
        solution.getRandom(); // return 2
        solution.getRandom(); // return 2
        solution.getRandom(); // return 3
        // getRandom() should return either 1, 2, or 3 randomly. 
        // Each element should have equal probability of returning.

Constraints:
    The number of nodes in the linked list will be in the range [1, 10^4].
    -10^4 <= Node.val <= 10^4
    At most 104 calls will be made to getRandom.

Follow up:
    1. What if the linked list is extremely large and its length is unknown to you?
    2. Could you solve this efficiently without using extra space?
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


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # exception case
        if (not isinstance(self.head, ListNode)) and (self.head is not None):
            return -1  # Error head type
        # main method: (Reservoir Sampling)
        return self._getRandom()

    def _getRandom(self) -> int:
        """
        [Reservoir Sampling](https://en.wikipedia.org/wiki/Reservoir_sampling): each time reserve only one item,
        for the n-th item (n = 1, 2, 3, ...), its reservation probability is 1/n (abbreviate: r_prob)
        for example, if a nearly infinite list [A, B, C, D, ...] will come in,
        Step 1: A comes (1-st item), A's r_prob is 1/1,
        Step 2: B comes (2-nd item), A is still here, B's r_prob is 1/2,
            which means that A's r_prob is 1/1 * (1 - 1/2) = 1/2 in the whole 2 steps, the same prob to B.
        Step 3: C comes (3-rd item), assume B is reserved on step 2, C's r_prob is 1/3,
            which means that B's r_prob is 1/2 * (1 - 1/3) = 1/3 in the whole 3 steps, the same prob to C.
        so on and so forth. No matter how long the list is (say, N), the r_prob of reserved item will always be 1/N
        """
        n_th = 1
        rs_item = -1  # reserved item at the moment (default: -1 if self.head is None)
        ptr = self.head  # pointer of the simply linked list
        while ptr:  # look over all items one by one
            if n_th == random.randint(1, n_th):  # random.randint will evenly sample (closed interval)
                rs_item = ptr.val  # the r_prob of new item is 1/n_th
            ptr = ptr.next
            n_th += 1
        return rs_item


def main():
    # Example 1:
    #     Input
    #         ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
    #         [[[1, 2, 3]], [], [], [], [], []]
    #     Output
    #         [null, 1, 3, 2, 2, 3]

    head_node = ListNode.build_singly_linked_list([1, 2, 3])

    # init instance
    solution = Solution(head_node)

    print(solution.getRandom())
    print(solution.getRandom())
    print(solution.getRandom())
    print(solution.getRandom())
    print(solution.getRandom())

    # run & time
    # start = time.process_time()
    # ans = solution.getRandom()
    # end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    # print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
