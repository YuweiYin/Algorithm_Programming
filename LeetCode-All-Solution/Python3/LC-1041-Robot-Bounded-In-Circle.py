#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1041-Robot-Bounded-In-Circle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-09
=================================================================="""

import sys
import time
# from typing import List
# import queue
# import collections

"""
LeetCode - 1041 - (Medium) - Robot Bounded In Circle
https://leetcode.com/problems/robot-bounded-in-circle/

Description:
    On an infinite plane, a robot initially stands at (0, 0) and faces north. 
    The robot can receive one of three instructions:
        "G": go straight 1 unit;
        "L": turn 90 degrees to the left;
        "R": turn 90 degrees to the right.
    The robot performs the instructions given in order, and repeats them forever.

Requirement:
    Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
    Input: instructions = "GGLLGG"
    Output: true
    Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
        When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:
    Input: instructions = "GG"
    Output: false
    Explanation: The robot moves north indefinitely.
Example 3:
    Input: instructions = "GL"
    Output: true
    Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Constraints:
    1 <= instructions.length <= 100
    instructions[i] is 'G', 'L' or, 'R'.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # exception case
        if not isinstance(instructions, str) or len(instructions) <= 0:
            return False
        if len(instructions) == 1:
            if str == "G":
                return False
            else:
                return True  # always turn directions
        if "G" not in instructions:
            return True  # always turn directions
        # main method:
        return self._isRobotBounded(instructions)

    def _isRobotBounded(self, instructions: str) -> bool:
        # len_ins = len(instructions)
        # max_step = len_ins << 2  # if the route forms a circle, perform (4 * len_ins) steps is enough
        # case 1: After one set of instructions, the robot return to (0, 0) -> return Ture
        # case 2.1: After one set of instructions, the robot is not at (0, 0), and it still faces north -> return False
        # case 2.2: After one set of instructions, the robot is not at (0, 0), and it faces south,
        #    then after next set of instructions, it must return to (0, 0) and face north -> return True
        # case 2.3: After one set of instructions, the robot is not at (0, 0), and it faces east,
        #    then after next set of instructions, it must face south; keep moving, it must face west,
        #    keep moving again, it must return to (0, 0) and face north -> return True
        #    (the routh is like a "square" whose edges are not straight lines but irregular curves)
        # case 2.4: similar to case 2.3 -> return True

        cur_x, cur_y = 0, 0
        cur_direction = 0  # in clockwise order. 0: north, 1: east, 2: south, 3: west
        mod_direction = 4
        for ins in instructions:
            if ins == "G":  # go straight
                if cur_direction == 0:  # north
                    cur_x += 1
                elif cur_direction == 1:  # east
                    cur_y += 1
                elif cur_direction == 2:  # south
                    cur_x -= 1
                elif cur_direction == 3:  # west
                    cur_y -= 1
                else:
                    pass  # error direction
            elif ins == "L":  # turn left
                cur_direction = (cur_direction - 1) % mod_direction
            elif ins == "R":  # turn right
                cur_direction = (cur_direction + 1) % mod_direction
            else:
                pass  # error instruction

        if cur_x == 0 and cur_y == 0:
            return True  # case 1
        else:
            if cur_direction == 0:
                return False  # case 2.1
            else:
                return True  # case 2.2, 2.3, 2.4


def main():
    # Example 1: Output: true
    instructions = "GGLLGG"

    # Example 2: Output: false
    # instructions = "GG"

    # Example 3: Output: true
    # instructions = "GL"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isRobotBounded(instructions)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
