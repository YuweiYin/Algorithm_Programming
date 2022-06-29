#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0406-Queue-Reconstruction-by-Height.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-29
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0406 - (Medium) - Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/

Description & Requirement:
    You are given an array of people, people, which are the attributes of some people in a queue 
    (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi 
    with exactly ki other people in front who have a height greater than or equal to hi.

    Reconstruct and return the queue that is represented by the input array people. 
    The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] 
    is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:
    Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    Explanation:
        Person 0 has height 5 with no other people taller or the same height in front.
        Person 1 has height 7 with no other people taller or the same height in front.
        Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
        Person 3 has height 6 with one person taller or the same height in front, which is person 1.
        Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
        Person 5 has height 7 with one person taller or the same height in front, which is person 1.
        Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
Example 2:
    Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:
    1 <= people.length <= 2000
    0 <= hi <= 10^6
    0 <= ki < people.length
    It is guaranteed that the queue can be reconstructed.
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(people, list) and len(people) >= 1
        for person in people:
            assert isinstance(person, list) and len(person) == 2
            assert person[0] >= 0 and person[1] >= 0
        # main method: (sort h_i in a descending order and sort k_i in a ascending order)
        return self._reconstructQueue(people)

    def _reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 97 ms, faster than 96.94% of Python3 online submissions for Queue Reconstruction by Height.
        Memory Usage: 14.5 MB, less than 64.95% of Python3 online submissions for Queue Reconstruction by Height.
        """
        assert isinstance(people, list) and len(people) >= 1

        people.sort(key=lambda x: (-x[0], x[1]))

        res = []
        for person in people:
            res[person[1]: person[1]] = [person]

        return res


def main():
    # Example 1: Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    # people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    # Example 2: Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reconstructQueue(people)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
