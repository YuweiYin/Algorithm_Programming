#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0707-Design-Linked-List.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-22
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0707 - (Medium) - Design Linked List
https://leetcode.com/problems/design-linked-list/

Description & Requirement:
    Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
    A node in a singly linked list should have two attributes: val and next. 
    val is the value of the current node, and next is a pointer/reference to the next node.

    If you want to use the doubly linked list, you will need one more attribute prev to 
    indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

    Implement the MyLinkedList class:
        MyLinkedList() Initializes the MyLinkedList object.
        int get(int index) Get the value of the index-th node in the linked list. 
            If the index is invalid, return -1.
        void addAtHead(int val) Add a node of value val before the first element of the linked list. 
            After the insertion, the new node will be the first node of the linked list.
        void addAtTail(int val) Append a node of value val as the last element of the linked list.
        void addAtIndex(int index, int val) Add a node of value val before the index-th node in the linked list. 
            If index equals the length of the linked list, the node will be appended to the end of the linked list. 
            If index is greater than the length, the node will not be inserted.
        void deleteAtIndex(int index) Delete the index-th node in the linked list, if the index is valid.

Example 1:
    Input
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
        [[], [1], [3], [1, 2], [1], [1], [1]]
    Output
        [null, null, null, null, 2, null, 3]
    Explanation
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.addAtHead(1);
        myLinkedList.addAtTail(3);
        myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
        myLinkedList.get(1);              // return 2
        myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
        myLinkedList.get(1);              // return 3

Constraints:
    0 <= index, val <= 1000
    Please do not use the built-in LinkedList library.
    At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
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


class MyLinkedList:

    def __init__(self):
        self.null_head = ListNode()
        self.list_len = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.list_len:
            ptr = self.null_head
            for _ in range(index + 1):  # move to the target node (0-indexed)
                ptr = ptr.next
            return ptr.val
        else:  # invalid index
            return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val=val, next=self.null_head.next)
        self.null_head.next = new_node
        self.list_len += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val=val)
        ptr = self.null_head
        for _ in range(self.list_len): # move to the tail node
            ptr = ptr.next
        ptr.next = new_node
        self.list_len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index < self.list_len:
            new_node = ListNode(val=val)
            ptr = self.null_head
            for _ in range(index):  # move to the pre node of the target node (0-indexed)
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node
            self.list_len += 1
        elif index == self.list_len:  # append to the end
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.list_len:
            ptr = self.null_head
            for _ in range(index):  # move to the pre node of the target node (0-indexed)
                ptr = ptr.next
            delete_node = ptr.next
            ptr.next = delete_node.next
            del delete_node
            self.list_len -= 1


def main():
    # Example 1: Output: [null, null, null, null, 2, null, 3]
    # command_list = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    # param_list = [[], [1], [3], [1, 2], [1], [1], [1]]

    command_list = ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex",
                    "addAtHead", "addAtTail", "get", "addAtHead", "addAtIndex", "addAtHead"]
    param_list = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]

    # init instance
    # solution = Solution()
    obj = MyLinkedList()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "addAtHead":
            if isinstance(param, list) and len(param) == 1:
                obj.addAtHead(param[0])
            ans.append("null")
        elif command == "addAtTail":
            if isinstance(param, list) and len(param) == 1:
                obj.addAtTail(param[0])
            ans.append("null")
        elif command == "addAtIndex":
            if isinstance(param, list) and len(param) == 2:
                obj.addAtIndex(param[0], param[1])
            ans.append("null")
        elif command == "deleteAtIndex":
            if isinstance(param, list) and len(param) == 1:
                obj.deleteAtIndex(param[0])
            ans.append("null")
        elif command == "get":
            if isinstance(param, list) and len(param) == 1:
                get_item = obj.get(param[0])
                ans.append(get_item)
            else:
                ans.append("null")
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    print(ans)
    # ListNode.show_val_singly_linked_list(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
