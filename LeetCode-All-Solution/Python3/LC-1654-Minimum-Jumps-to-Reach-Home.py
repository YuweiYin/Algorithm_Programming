#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1654-Minimum-Jumps-to-Reach-Home.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-30
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1654 - (Medium) Minimum Jumps to Reach Home
https://leetcode.com/problems/minimum-jumps-to-reach-home/

Description & Requirement:
    A certain bug's home is on the x-axis at position x. 
    Help them get there from position 0.

    The bug jumps according to the following rules:
        It can jump exactly a positions forward (to the right).
        It can jump exactly b positions backward (to the left).
        It cannot jump backward twice in a row.
        It cannot jump to any forbidden positions.

    The bug may jump forward beyond its home, 
    but it cannot jump to positions numbered with negative integers.

    Given an array of integers forbidden, where forbidden[i] means that 
    the bug cannot jump to the position forbidden[i], and integers a, b, and x, 
    return the minimum number of jumps needed for the bug to reach its home. 
    If there is no possible sequence of jumps that lands the bug on position x, return -1.

Example 1:
    Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
    Output: 3
    Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
Example 2:
    Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
    Output: -1
Example 3:
    Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
    Output: 2
    Explanation: One jump forward (0 -> 16) then one jump 
        backward (16 -> 7) will get the bug home.

Constraints:
    1 <= forbidden.length <= 1000
    1 <= a, b, forbidden[i] <= 2000
    0 <= x <= 2000
    All the elements in forbidden are distinct.
    Position x is not forbidden.
"""


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # exception case
        assert isinstance(forbidden, list) and len(forbidden) >= 1
        assert isinstance(a, int) and isinstance(b, int) and 1 <= a and 1 <= b
        assert isinstance(x, int)
        # main method: (BFS)
        return self._minimumJumps(forbidden, a, b, x)

    def _minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        assert isinstance(forbidden, list) and len(forbidden) >= 1
        assert isinstance(a, int) and isinstance(b, int) and 1 <= a and 1 <= b
        assert isinstance(x, int)

        queue, visited = collections.deque([[0, 1, 0]]), {0}
        lower, upper = 0, max(max(forbidden) + a, x) + b
        forbidden_set = set(forbidden)

        while len(queue) > 0:
            position, direction, step = queue.popleft()
            if position == x:
                return step

            nextPosition = position + a
            nextDirection = 1
            if (lower <= nextPosition <= upper) and (nextPosition * nextDirection not in visited) and \
                    (nextPosition not in forbidden_set):
                visited.add(nextPosition * nextDirection)
                queue.append([nextPosition, nextDirection, step + 1])

            if direction == 1:
                nextPosition = position - b
                nextDirection = -1
                if (lower <= nextPosition <= upper) and (nextPosition * nextDirection not in visited) and \
                        (nextPosition not in forbidden_set):
                    visited.add(nextPosition * nextDirection)
                    queue.append([nextPosition, nextDirection, step + 1])

        return -1


def main():
    # Example 1: Output: 3
    # forbidden = [14, 4, 18, 1, 15]
    # a = 3
    # b = 15
    # x = 9

    # Example 2: Output: -1
    # forbidden = [8, 3, 16, 6, 12, 20]
    # a = 15
    # b = 13
    # x = 11

    # Example 3: Output: 2
    forbidden = [1, 6, 2, 14, 5, 17, 4]
    a = 16
    b = 9
    x = 7

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimumJumps(forbidden, a, b, x)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
