#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0874-Walking-Robot-Simulation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-19
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 0874 - (Medium) - Walking Robot Simulation
https://leetcode.com/problems/walking-robot-simulation/

Description & Requirement:
    A robot on an infinite XY-plane starts at point (0, 0) facing north. 
    The robot can receive a sequence of these three possible types of commands:
        -2: Turn left 90 degrees.
        -1: Turn right 90 degrees.
        1 <= k <= 9: Move forward k units, one unit at a time.

    Some of the grid squares are obstacles. The i-th obstacle is at grid point obstacles[i] = (xi, yi). 
    If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

    Return the maximum Euclidean distance that the robot ever gets from the origin squared 
    (i.e. if the distance is 5, return 25).

    Note:
        North means +Y direction.
        East means +X direction.
        South means -Y direction.
        West means -X direction.

Example 1:
    Input: commands = [4,-1,3], obstacles = []
    Output: 25
    Explanation: The robot starts at (0, 0):
        1. Move north 4 units to (0, 4).
        2. Turn right.
        3. Move east 3 units to (3, 4).
        The furthest point the robot ever gets from the origin is (3, 4), 
            which squared is 32 + 42 = 25 units away.
Example 2:
    Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
    Output: 65
    Explanation: The robot starts at (0, 0):
        1. Move north 4 units to (0, 4).
        2. Turn right.
        3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
        4. Turn left.
        5. Move north 4 units to (1, 8).
        The furthest point the robot ever gets from the origin is (1, 8), 
            which squared is 12 + 82 = 65 units away.
Example 3:
    Input: commands = [6,-1,-1,6], obstacles = []
    Output: 36
    Explanation: The robot starts at (0, 0):
        1. Move north 6 units to (0, 6).
        2. Turn right.
        3. Turn right.
        4. Move south 6 units to (0, 0).
        The furthest point the robot ever gets from the origin is (0, 6), 
            which squared is 62 = 36 units away.

Constraints:
    1 <= commands.length <= 10^4
    commands[i] is either -2, -1, or an integer in the range [1, 9].
    0 <= obstacles.length <= 10^4
    -3 * 10^4 <= xi, yi <= 3 * 10^4
    The answer is guaranteed to be less than 2^31.
"""


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # exception case
        assert isinstance(commands, list) and len(commands) >= 1
        assert isinstance(obstacles, list)
        # main method: (hash set)
        return self._robotSim(commands, obstacles)

    def _robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        assert isinstance(commands, list) and len(commands) >= 1
        assert isinstance(obstacles, list)

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        px, py, d = 0, 0, 1
        hash_set = set([tuple(i) for i in obstacles])
        res = 0

        for command in commands:
            if command < 0:
                d += 1 if command == -1 else -1
                d %= 4
            else:
                for _ in range(command):
                    if tuple([px + dirs[d][0], py + dirs[d][1]]) in hash_set:
                        break
                    px, py = px + dirs[d][0], py + dirs[d][1]
                    res = max(res, px * px + py * py)

        return res


def main():
    # Example 1: Output: 25
    # commands = [4, -1, 3]
    # obstacles = []

    # Example 2: Output: 65
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]

    # Example 3: Output: 36
    # commands = [6, -1, -1, 6]
    # obstacles = []

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.robotSim(commands, obstacles)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
