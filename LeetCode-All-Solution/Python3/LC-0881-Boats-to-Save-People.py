#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0881-Boats-to-Save-People.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-24
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0881 - (Medium) - Boats to Save People
https://leetcode.com/problems/boats-to-save-people/

Description & Requirement:
    You are given an array people where people[i] is the weight of the ith person, 
    and an infinite number of boats where each boat can carry a maximum weight of limit. 
    Each boat carries at most two people at the same time, 
    provided the sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.

Example 1:
    Input: people = [1,2], limit = 3
    Output: 1
    Explanation: 1 boat (1, 2)
Example 2:
    Input: people = [3,2,2,1], limit = 3
    Output: 3
    Explanation: 3 boats (1, 2), (2) and (3)
Example 3:
    Input: people = [3,5,3,4], limit = 5
    Output: 4
    Explanation: 4 boats (3), (3), (4), (5)

Constraints:
    1 <= people.length <= 5 * 10^4
    1 <= people[i] <= limit <= 3 * 10^4
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # exception case
        assert isinstance(people, list) and len(people) > 0
        assert isinstance(limit, int) and limit > 0
        for person in people:
            assert isinstance(person, int) and 0 < person <= limit
        # main method: (sort and greedily pair two people such that the sum weight of the two is nearly limit)
        return self._numRescueBoats(people, limit)

    def _numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0

        # first, every person whose weight is equal to limit will exclusively use a boat
        other_people = []  # lighter than limit
        for person in people:
            if person == limit:
                res += 1
            else:
                other_people.append(person)
        other_people.sort()

        # let the lightest person paired with the heaviest person
        light_idx = 0
        heavy_idx = len(other_people) - 1
        while light_idx <= heavy_idx:
            if other_people[light_idx] + other_people[heavy_idx] <= limit:
                light_idx += 1
                heavy_idx -= 1
            else:  # the heavy person can only exclusively use a boat
                heavy_idx -= 1
            res += 1

        return res


def main():
    # Example 1: Output: 1
    # people = [1, 2]
    # limit = 3

    # Example 2: Output: 3
    people = [3, 2, 2, 1]
    limit = 3

    # Example 3: Output: 4
    # people = [3, 5, 3, 4]
    # limit = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numRescueBoats(people, limit)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
