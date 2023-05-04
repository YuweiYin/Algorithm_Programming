#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0649-Dota2-Senate.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-04
=================================================================="""

import sys
import time
# from typing import List
import collections
# import functools

"""
LeetCode - 0649 - (Medium) - Dota2 Senate
https://leetcode.com/problems/dota2-senate/

Description & Requirement:
    In the world of Dota2, there are two parties: the Radiant and the Dire.

    The Dota2 senate consists of senators coming from two parties. 
    Now the Senate wants to decide on a change in the Dota2 game. 
    The voting for this change is a round-based procedure. 
    In each round, each senator can exercise one of the two rights:

        Ban one senator's right: 
            A senator can make another senator lose all his rights in this and all the following rounds.
        Announce the victory: 
            If this senator found the senators who still have rights to vote are all from the same party, 
            he can announce the victory and decide on the change in the game.

    Given a string senate representing each senator's party belonging. 
    The character 'R' and 'D' represent the Radiant party and the Dire party. 
    Then if there are n senators, the size of the given string will be n.

    The round-based procedure starts from the first senator to the last senator in the given order. 
    This procedure will last until the end of voting. 
    All the senators who have lost their rights will be skipped during the procedure.

    Suppose every senator is smart enough and will play the best strategy for his own party. 
    Predict which party will finally announce the victory and change the Dota2 game. 
    The output should be "Radiant" or "Dire".

Example 1:
    Input: senate = "RD"
    Output: "Radiant"
    Explanation: 
        The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
        And the second senator can't exercise any rights anymore since his right has been banned. 
        And in round 2, the first senator can just announce the victory 
            since he is the only guy in the senate who can vote.
Example 2:
    Input: senate = "RDD"
    Output: "Dire"
    Explanation: 
        The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
        And the second senator can't exercise any rights anymore since his right has been banned. 
        And the third senator comes from Dire and he can ban the first senator's right in round 1. 
        And in round 2, the third senator can just announce the victory 
            since he is the only guy in the senate who can vote.

Constraints:
    n == senate.length
    1 <= n <= 10^4
    senate[i] is either 'R' or 'D'.
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # exception case
        assert isinstance(senate, str) and len(senate) >= 1
        # main method: (rotation queue)
        return self._predictPartyVictory(senate)

    def _predictPartyVictory(self, senate: str) -> str:
        assert isinstance(senate, str) and len(senate) >= 1

        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for idx, ch in enumerate(senate):
            if ch == "R":
                radiant.append(idx)
            else:
                dire.append(idx)

        while len(radiant) > 0 and len(dire) > 0:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"


def main():
    # Example 1: Output: "Radiant"
    senate = "RD"

    # Example 2: Output: "Dire"
    # senate = "RDD"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.predictPartyVictory(senate)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
