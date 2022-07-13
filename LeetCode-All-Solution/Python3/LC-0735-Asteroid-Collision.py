#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0735-Asteroid-Collision.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-13
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0735 - (Medium) - Asteroid Collision
https://leetcode.com/problems/asteroid-collision/

Description & Requirement:
    We are given an array asteroids of integers representing asteroids in a row.

    For each asteroid, the absolute value represents its size, 
    and the sign represents its direction (positive meaning right, negative meaning left). 
    Each asteroid moves at the same speed.

    Find out the state of the asteroids after all collisions. 
    If two asteroids meet, the smaller one will explode. 
    If both are the same size, both will explode. 
    Two asteroids moving in the same direction will never meet.

Example 1:
    Input: asteroids = [5,10,-5]
    Output: [5,10]
    Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:
    Input: asteroids = [8,-8]
    Output: []
    Explanation: The 8 and -8 collide exploding each other.
Example 3:
    Input: asteroids = [10,2,-5]
    Output: [10]
    Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:
    2 <= asteroids.length <= 10^4
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # exception case
        assert isinstance(asteroids, list) and len(asteroids) >= 2
        # main method: (stack simulation)
        return self._asteroidCollision(asteroids)

    def _asteroidCollision(self, asteroids: List[int]) -> List[int]:
        assert isinstance(asteroids, list) and len(asteroids) >= 2

        stack = []
        for aster in asteroids:
            assert isinstance(aster, int) and aster != 0
            if aster > 0:  # moving rightward
                stack.append(aster)
            else:  # moving leftward
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(aster)
                    continue
                cur_size = abs(aster)
                while len(stack) > 0 and cur_size > stack[-1] > 0:  # collide with asteroids
                    stack.pop()
                if len(stack) > 0:  # now, cur_size <= stack[-1]
                    if stack[-1] < 0:
                        stack.append(aster)
                    else:  # stack[-1] > 0
                        if cur_size == stack[-1]:  # explode each other.
                            stack.pop()
                        else:
                            pass  # cur asteroid was exploded
                else:
                    stack.append(aster)

        return stack


def main():
    # Example 1: Output: [5,10]
    # asteroids = [5, 10, -5]

    # Example 2: Output: []
    # asteroids = [8, -8]

    # Example 3: Output: [10]
    asteroids = [10, 2, -5]

    # Example 4: Output: [-2,-2,-2]
    # asteroids = [-2, -2, 1, -2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.asteroidCollision(asteroids)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
