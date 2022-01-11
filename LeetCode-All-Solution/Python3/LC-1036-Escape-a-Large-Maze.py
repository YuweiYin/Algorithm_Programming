#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1036-Escape-a-Large-Maze.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-11
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 1036 - (Hard) - Escape a Large Maze
https://leetcode.com/problems/escape-a-large-maze/

Description:
    There is a 1 million by 1 million grid on an XY-plane, 
    and the coordinates of each grid square are (x, y).

    We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. 
    There is also an array of blocked squares, 
    where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).

    Each move, we can walk one square north, east, south, or west 
    if the square is not in the array of blocked squares. 
    We are also not allowed to walk outside of the grid.

Requirement:
    Return true if and only if it is possible to reach the target square 
    from the source square through a sequence of valid moves.

Example 1:
    Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
    Output: false
    Explanation: The target square is inaccessible starting from the source square because we cannot move.
        We cannot move north or east because those squares are blocked.
        We cannot move south or west because we cannot go outside of the grid.
Example 2:
    Input: blocked = [], source = [0,0], target = [999999,999999]
    Output: true
    Explanation: Because there are no blocked cells, it is possible to reach the target square.

Constraints:
    0 <= blocked.length <= 200
    blocked[i].length == 2
    0 <= xi, yi < 10^6
    source.length == target.length == 2
    0 <= sx, sy, tx, ty < 10^6
    source != target
    It is guaranteed that source and target are not blocked.
"""


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        Runtime: 711 ms, faster than 84.21% of Python3 online submissions for Escape a Large Maze.
        Memory Usage: 18.8 MB, less than 89.47% of Python3 online submissions for Escape a Large Maze.
        """
        # exception case
        if not isinstance(blocked, list) or not isinstance(source, list) or not isinstance(target, list):
            return False  # error input
        if len(source) != 2 or len(target) != 2:
            return False  # error input
        if len(blocked) <= 1:  # 0 or 1 blocked square cannot surround target square, so there must be a valid path
            return True
        if source == target:  # Why bother moving?
            return True
        for blocked_square in blocked:
            if len(blocked_square) != 2:
                return False  # error input
            if blocked_square[0] == source[0] and blocked_square[1] == source[1]:
                return False  # source is blocked
            if blocked_square[0] == target[0] and blocked_square[1] == target[1]:
                return False  # target is blocked
        # main method: single-source bfs from source to target until:
        #     1. reach the target. -> True
        #     2. bfs area > max blocked area. -> Ture  (Constraints: 0 <= blocked.length <= 200)
        #     3. get fully surrounded, can't move but not reach target. -> False
        return self._isEscapePossible(blocked, source, target)

    def _isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        MAX_INDEX = 999999
        len_b = len(blocked)
        blocked_set = set()  # convert to set, for fast judge
        for blocked_square in blocked:
            blocked_set.add(tuple(blocked_square))
        # special case: the number of blocked squares are not enough to surround the target square
        if len_b == 2:  # return False if source/target is at the corner and blocked squares surround it
            if source == [0, 0] or target == [0, 0]:  # northwest corner
                if (0, 1) in blocked_set and (1, 0) in blocked_set:
                    return False
                else:
                    return True
            if source == [0, MAX_INDEX] or target == [0, MAX_INDEX]:  # northeast corner
                if (0, MAX_INDEX - 1) in blocked_set and (1, MAX_INDEX) in blocked_set:
                    return False
                else:
                    return True
            if source == [MAX_INDEX, 0] or target == [MAX_INDEX, 0]:  # southwest corner
                if (MAX_INDEX - 1, 0) in blocked_set and (MAX_INDEX, 1) in blocked_set:
                    return False
                else:
                    return True
            if source == [MAX_INDEX, MAX_INDEX] or target == [MAX_INDEX, MAX_INDEX]:  # southeast corner
                if (MAX_INDEX - 1, MAX_INDEX) in blocked_set and (MAX_INDEX, MAX_INDEX - 1) in blocked_set:
                    return False
                else:
                    return True
            return True  # source and target are not at the corner, so there must be a valid path

        # single-source bfs from source to target until:
        #     1. reach the target. -> True
        #     2. bfs area > max blocked area. -> Ture  (Constraints: 0 <= blocked.length <= 200)
        #     3. get fully surrounded, can't move but not reach target. -> False
        # max_blocked_area: imagine blocked area is an isoceles right triangle, surrounding one corner
        # max_blocked_area = sum([i for i in range(1, len_b + 1)])
        max_blocked_area = (len_b * (len_b + 1)) >> 1

        def __check_surround(source_row: int, source_col: int, target_row: int, target_col: int):
            bfs_queue = collections.deque()
            bfs_queue.append([source_row, source_col])
            done_bfs_set = set()  # (x, y) in done_bfs_set means square (x, y) has been explored
            done_bfs_set.add(tuple([source_row, source_col]))
            while len(bfs_queue) > 0:
                cur_row, cur_col = bfs_queue.popleft()
                if cur_row == target_row and cur_col == target_col:  # reach the target
                    return True
                if len(done_bfs_set) > max_blocked_area:  # source is not surrounded, then check if target is surrounded
                    return True
                # four directions
                # if 0 <= cur_col - 1 and tuple([cur_row, cur_col - 1]) not in done_bfs_set and \
                #         tuple([cur_row, cur_col - 1]) not in blocked_set:  # left
                #     bfs_queue.append([cur_row, cur_col - 1])
                #     done_bfs_set.add(tuple([cur_row, cur_col - 1]))  # record done bfs
                if 0 <= cur_col - 1 and (cur_row, cur_col - 1) not in done_bfs_set and \
                        (cur_row, cur_col - 1) not in blocked_set:  # left
                    bfs_queue.append([cur_row, cur_col - 1])
                    done_bfs_set.add(tuple([cur_row, cur_col - 1]))  # record done bfs
                if 0 <= cur_row - 1 and (cur_row - 1, cur_col) not in done_bfs_set and \
                        (cur_row - 1, cur_col) not in blocked_set:  # up
                    bfs_queue.append([cur_row - 1, cur_col])
                    done_bfs_set.add(tuple([cur_row - 1, cur_col]))  # record done bfs
                if cur_col + 1 <= MAX_INDEX and (cur_row, cur_col + 1) not in done_bfs_set and \
                        (cur_row, cur_col + 1) not in blocked_set:  # right
                    bfs_queue.append([cur_row, cur_col + 1])
                    done_bfs_set.add(tuple([cur_row, cur_col + 1]))  # record done bfs
                if cur_row + 1 <= MAX_INDEX and (cur_row + 1, cur_col) not in done_bfs_set and \
                        (cur_row + 1, cur_col) not in blocked_set:  # down
                    bfs_queue.append([cur_row + 1, cur_col])
                    done_bfs_set.add(tuple([cur_row + 1, cur_col]))  # record done bfs
            return False

        if_source_free = __check_surround(source[0], source[1], target[0], target[1])
        if_target_free = __check_surround(target[0], target[1], source[0], source[1])
        return if_source_free and if_target_free


def main():
    # Example 1: Output: false
    # blocked = [[0, 1], [1, 0]]
    # source = [0, 0]
    # target = [0, 2]

    # Example 2: Output: true
    # blocked = []
    # source = [0, 0]
    # target = [999999, 999999]

    # Example 3: Output: true
    # blocked = [
    #     [691938, 300406],
    #     [710196, 624190],
    #     [858790, 609485],
    #     [268029, 225806],
    #     [200010, 188664],
    #     [132599, 612099],
    #     [329444, 633495],
    #     [196657, 757958],
    #     [628509, 883388]
    # ]
    # source = [655988, 180910]
    # target = [267728, 840949]

    # Example 3: Output: false
    blocked = [
        [100059, 100063], [100060, 100064], [100061, 100065], [100062, 100066], [100063, 100067],
        [100064, 100068], [100065, 100069], [100066, 100070], [100067, 100071], [100068, 100072],
        [100069, 100073], [100070, 100074], [100071, 100075], [100072, 100076], [100073, 100077],
        [100074, 100078], [100075, 100079], [100076, 100080], [100077, 100081], [100078, 100082],
        [100079, 100083], [100080, 100082], [100081, 100081], [100082, 100080], [100083, 100079],
        [100084, 100078], [100085, 100077], [100086, 100076], [100087, 100075], [100088, 100074],
        [100089, 100073], [100090, 100072], [100091, 100071], [100092, 100070], [100093, 100069],
        [100094, 100068], [100095, 100067], [100096, 100066], [100097, 100065], [100098, 100064],
        [100099, 100063], [100098, 100062], [100097, 100061], [100096, 100060], [100095, 100059],
        [100094, 100058], [100093, 100057], [100092, 100056], [100091, 100055], [100090, 100054],
        [100089, 100053], [100088, 100052], [100087, 100051], [100086, 100050], [100085, 100049],
        [100084, 100048], [100083, 100047], [100082, 100046], [100081, 100045], [100080, 100044],
        [100079, 100043], [100078, 100044], [100077, 100045], [100076, 100046], [100075, 100047],
        [100074, 100048], [100073, 100049], [100072, 100050], [100071, 100051], [100070, 100052],
        [100069, 100053], [100068, 100054], [100067, 100055], [100066, 100056], [100065, 100057],
        [100064, 100058], [100063, 100059], [100062, 100060], [100061, 100061], [100060, 100062]
    ]
    source = [100079, 100063]
    target = [999948, 999967]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isEscapePossible(blocked, source, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
