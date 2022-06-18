#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-OFFER-II-0029-Sorted-Circular-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-18
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - OFFER-II-0029 - (Medium) - Sorted Circular Linked List
https://leetcode.cn/problems/4ueAj6/

Description & Requirement:
    给定循环单调非递减列表中的一个点, 写一个函数向这个列表中插入一个新元素 insertVal, 使这个列表仍然是循环升序的.
    给定的可以是这个列表中任意一个顶点的指针, 并不一定是这个列表中最小元素的指针.
    如果有多个满足条件的插入位置, 可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序.

    如果列表为空 (给定的节点是 null), 需要创建一个循环有序列表并返回这个节点.
    否则, 请返回原先给定的节点.

Example 1:
    Input: head = [3,4,1], insertVal = 2
    Output: [3,4,1,2]
    Explanation: 在上图中, 有一个包含三个元素的循环有序列表, 获得值为 3 的节点的指针, 需要向表中插入元素 2.
        新插入的节点应该在 1 和 3 之间, 插入之后, 整个列表如上图所示, 最后返回节点 3.
Example 2:
    Input: head = [], insertVal = 1
    Output: [1]
    Explanation: 列表为空 (给定的节点是 null), 创建一个循环有序列表并返回这个节点.
Example 3:
    Input: head = [1], insertVal = 0
    Output: [1, 0]

Constraints:
    0 <= Number of Nodes <= 5 * 10^4
    -10^6 <= Node.val <= 10^6
    -10^6 <= insertVal <= 10^6
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> Optional[Node]:
        # exception case
        assert isinstance(insertVal, int)
        if not isinstance(head, Node):
            new_node = Node(val=insertVal, next=None)
            new_node.next = new_node
            return new_node
        if not isinstance(head.next, Node) or head.next == head:
            new_node = Node(val=insertVal, next=head)
            head.next = new_node
            return head
        # main method: (scan and check the insertVal)
        return self._insert(head, insertVal)

    def _insert(self, head: Optional[Node], insertVal: int) -> Optional[Node]:
        assert isinstance(insertVal, int)
        assert isinstance(head, Node) and isinstance(head.next, Node)

        new_node = Node(val=insertVal, next=None)

        ptr = head
        ptr_next = head.next
        while ptr_next != head:
            if ptr.val <= insertVal <= ptr_next.val:
                break
            if ptr_next.val < ptr.val:
                if ptr.val < insertVal or insertVal < ptr_next.val:
                    break
            ptr = ptr.next
            ptr_next = ptr_next.next

        ptr.next = new_node
        new_node.next = ptr_next
        return head


def main():
    # Example 1: Output: [3,4,1,2]
    # head = [3, 4, 1]
    insertVal = 2
    node_1 = Node(val=1)
    node_4 = Node(val=4, next=node_1)
    node_3 = Node(val=3, next=node_4)
    node_1.next = node_3
    head_node = node_3

    # Example 2: Output: [1]
    # head = []
    # insertVal = 1

    # Example 3: Output: [1, 0]
    # head = [1]
    # insertVal = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.insert(head_node, insertVal)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    new_head = ans
    print(ans.val)
    ans = ans.next
    while isinstance(ans, Node) and ans != new_head:
        print(ans.val)
        ans = ans.next

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
