#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0841-Keys-and-Rooms.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-29
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0841 - (Medium) - Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/

Description & Requirement:
    There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
    Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

    When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, 
    denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
    return true if you can visit all the rooms, or false otherwise.

Example 1:
    Input: rooms = [[1],[2],[3],[]]
    Output: true
    Explanation: 
        We visit room 0 and pick up key 1.
        We then visit room 1 and pick up key 2.
        We then visit room 2 and pick up key 3.
        We then visit room 3.
        Since we were able to visit every room, we return true.
Example 2:
    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

Constraints:
    n == rooms.length
    2 <= n <= 1000
    0 <= rooms[i].length <= 1000
    1 <= sum(rooms[i].length) <= 3000
    0 <= rooms[i][j] < n
    All the values of rooms[i] are unique.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # exception case
        assert isinstance(rooms, list) and len(rooms) >= 2
        # main method: (stimulate, expand the search span)
        return self._canVisitAllRooms(rooms)

    def _canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Runtime: 72 ms, faster than 82.59% of Python3 online submissions for Keys and Rooms.
        Memory Usage: 14.5 MB, less than 35.54% of Python3 online submissions for Keys and Rooms.
        """
        bfs_queue = collections.deque()
        visited = set()

        bfs_queue.append(0)
        while len(bfs_queue) > 0:
            cur_room = bfs_queue.popleft()
            if cur_room in visited:
                continue
            visited.add(cur_room)
            for room_key in rooms[cur_room]:  # get all keys of this room
                if room_key not in visited:
                    bfs_queue.append(room_key)

        return len(visited) == len(rooms)


def main():
    # Example 1: Output: true
    # rooms = [[1], [2], [3], []]

    # Example 2: Output: false
    rooms = [[1, 3], [3, 0, 1], [2], [0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canVisitAllRooms(rooms)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
