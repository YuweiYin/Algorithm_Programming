#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1993-Operations-on-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-23
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1993 - (Medium) Operations on Tree
https://leetcode.com/problems/operations-on-tree/

Description & Requirement:
    You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where 
    parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent.
    You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

    The data structure should support the following functions:
        - Lock: Locks the given node for the given user and prevents other users from locking the same node. 
            You may only lock a node using this function if the node is unlocked.
        - Unlock: Unlocks the given node for the given user. 
            You may only unlock a node using this function if it is currently locked by the same user.
        - Upgrade: Locks the given node for the given user and unlocks all of its descendants 
            regardless of who locked it. You may only upgrade a node if all 3 conditions are true:
            - The node is unlocked,
            - It has at least one locked descendant (by any user), and
            - It does not have any locked ancestors.

    Implement the LockingTree class:
        - LockingTree(int[] parent) initializes the data structure with the parent array.
        - lock(int num, int user) returns true if it is possible for the user with id user to lock the node num, 
            or false otherwise. If it is possible, the node num will become locked by the user with id user.
        - unlock(int num, int user) returns true if it is possible for the user with id user to unlock the node num, 
            or false otherwise. If it is possible, the node num will become unlocked.
        - upgrade(int num, int user) returns true if it is possible for the user with id user to upgrade the node num, 
            or false otherwise. If it is possible, the node num will be upgraded.

Example 1:
    Input
        ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
        [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
    Output
        [null, true, false, true, true, true, false]
    Explanation
        LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
        lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
                                   // Node 2 will now be locked by user 2.
        lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
        lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
                                   // Node 2 will now be unlocked.
        lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
                                   // Node 4 will now be locked by user 5.
        lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and 
                                   // has at least one locked descendant (node 4).
                                   // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
        lockingTree.lock(0, 1);    // return false because node 0 is already locked.

Constraints:
    n == parent.length
    2 <= n <= 2000
    0 <= parent[i] <= n - 1 for i != 0
    parent[0] == -1
    0 <= num <= n - 1
    1 <= user <= 10^4
    parent represents a valid tree.
    At most 2000 calls in total will be made to lock, unlock, and upgrade.
"""


class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.lockNodeUser = [-1] * n
        self.children = [[] for _ in range(n)]
        for node, p in enumerate(parent):
            if p != -1:
                self.children[p].append(node)

    def lock(self, num: int, user: int) -> bool:
        if self.lockNodeUser[num] == -1:
            self.lockNodeUser[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if self.lockNodeUser[num] == user:
            self.lockNodeUser[num] = -1
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        res = self.lockNodeUser[num] == -1 and not self.has_locked_ancestor(num) \
              and self.check_and_unlock_descendant(num)
        if res:
            self.lockNodeUser[num] = user
        return res

    def has_locked_ancestor(self, num: int) -> bool:
        num = self.parent[num]
        while num != -1:
            if self.lockNodeUser[num] != -1:
                return True
            else:
                num = self.parent[num]
        return False

    def check_and_unlock_descendant(self, num: int) -> bool:
        res = self.lockNodeUser[num] != -1
        self.lockNodeUser[num] = -1
        for child in self.children[num]:
            # DFS
            res |= self.check_and_unlock_descendant(child)
        return res


def main():
    # Example 1: Output: [null, true, false, true, true, true, false]
    command_list = ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
    param_list = [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]

    # init instance
    # solution = Solution()
    parent = param_list[0][0]
    obj = LockingTree(parent)
    ans = ["null"]

    # run & time
    _start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "lock" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.lock(param[0], param[1]))
        elif command == "unlock" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.unlock(param[0], param[1]))
        elif command == "upgrade" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.upgrade(param[0], param[1]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
