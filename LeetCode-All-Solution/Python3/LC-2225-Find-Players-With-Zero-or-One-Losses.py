#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2225-Find-Players-With-Zero-or-One-Losses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-28
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2225 - (Medium) - Find Players With Zero or One Losses
https://leetcode.com/problems/find-players-with-zero-or-one-losses/

Description & Requirement:
    You are given an integer array matches where matches[i] = [winner_i, loser_i] indicates that 
    the player winner_i defeated player loser_i in a match.

    Return a list answer of size 2 where:

        answer[0] is a list of all players that have not lost any matches.
        answer[1] is a list of all players that have lost exactly one match.
        The values in the two lists should be returned in increasing order.

    Note:
        You should only consider the players that have played at least one match.
        The testcases will be generated such that no two matches will have the same outcome.

Example 1:
    Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    Output: [[1,2,10],[4,5,7,8]]
    Explanation:
        Players 1, 2, and 10 have not lost any matches.
        Players 4, 5, 7, and 8 each have lost one match.
        Players 3, 6, and 9 each have lost two matches.
        Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:
    Input: matches = [[2,3],[1,3],[5,4],[6,4]]
    Output: [[1,2,5,6],[]]
    Explanation:
        Players 1, 2, 5, and 6 have not lost any matches.
        Players 3 and 4 each have lost two matches.
        Thus, answer[0] = [1,2,5,6] and answer[1] = [].

Constraints:
    1 <= matches.length <= 10^5
    matches[i].length == 2
    1 <= winner_i, loser_i <= 10^5
    winner_i != loser_i
    All matches[i] are unique.
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(matches, list) and len(matches) >= 1
        assert all([len(match) == 2 and match[0] != match[1] for match in matches])
        # main method: (hash set)
        return self._findWinners(matches)

    def _findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        assert isinstance(matches, list) and len(matches) >= 1

        freq = collections.Counter()
        for winner, loser in matches:
            if winner not in freq:
                freq[winner] = 0
            freq[loser] += 1

        res = [[], []]
        for key, value in freq.items():
            if value < 2:
                res[value].append(key)

        res[0].sort()
        res[1].sort()
        return res


def main():
    # Example 1: Output: [[1,2,10],[4,5,7,8]]
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]

    # Example 2: Output: [[1,2,5,6],[]]
    # matches = [[2, 3], [1, 3], [5, 4], [6, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findWinners(matches)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
