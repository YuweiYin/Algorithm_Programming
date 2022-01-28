#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1996-The-Number-of-Weak-Characters-in-the-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-28
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1996 - (Medium) - The Number of Weak Characters in the Game
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

Description & Requirement:
    You are playing a game that contains multiple characters, and each of the characters has two main properties: 
    attack and defense. You are given a 2D integer array properties where properties[i] = [attack_i, defense_i] 
    represents the properties of the ith character in the game.

    A character is said to be weak if any other character has both attack and defense levels 
    strictly greater than this character's attack and defense levels. 
    More formally, a character i is said to be weak if there exists another character j where 
    attack_j > attack_i and defense_j > defense_i.

    Return the number of weak characters.

Example 1:
    Input: properties = [[5,5],[6,3],[3,6]]
    Output: 0
    Explanation: No character has strictly greater attack and defense than the other.
Example 2:
    Input: properties = [[2,2],[3,3]]
    Output: 1
    Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:
    Input: properties = [[1,5],[10,4],[4,3]]
    Output: 1
    Explanation: The third character is weak because the second character has a strictly greater attack and defense.

Constraints:
    2 <= properties.length <= 10^5
    properties[i].length == 2
    1 <= attack_i, defense_i <= 10^5
"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # exception case
        if not isinstance(properties, list) or len(properties) <= 0:
            return 0  # Error input type
        if len(properties) == 1:
            return 0
        if len(properties) == 2:
            if properties[0][0] < properties[1][0] and properties[0][1] < properties[1][1]:
                return 1
            elif properties[0][0] > properties[1][0] and properties[0][1] > properties[1][1]:
                return 1
            else:
                return 0
        # main method: ("cross sort", sort list, attack in descending order)
        #     after sorting, scan list. check each point, if it is a weak number or not.
        #     now, att is in descending order, att[i] must be <= all att[j], where 0 <= j < i
        #     so if there exist a prop[j] such that def[j] > att[i], then i is a weak number
        #     therefore, use a variable max_def to record the largest defense value of all 0 <= j < i
        #         if def[i] < max_def, then prop[i] is a weak number.
        #         if def[i] >= max_def, then prop[i] is not a weak number.
        #             now, there's a problem: should max_def be updated?
        #             if update max_def to a larger def[i], while att[i+1] == att[i] but def[i+1] < former max_def
        #                 which means i+1 is a weak number, but as max_def has been updated, i+1 won't be count as weak
        #         consequently, when attack value is the same, sort their defense values in ascending order
        #              in this way, if prop[i] is not a weak number, then def[i+1] > def[i] is definitely not weak, too.
        #              just normally update the max_def, and the whole process will remain correct.
        return self._numberOfWeakCharacters(properties)

    def _numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        len_prop = len(properties)
        assert len_prop >= 3

        # sort attack in descending order; when attack value is the same, sort their defense values in ascending order
        properties.sort(key=lambda x: (-x[0], x[1]))

        res = 0  # weak number counter
        max_def = -1  # max defense value before the current property

        for _att, _def in properties:
            if _def < max_def:  # now, att order is valid (coz of sorting), consider def value
                res += 1
            else:
                max_def = max(max_def, _def)  # update the max_def

        return res


def main():
    # Example 1: Output: 0
    # properties = [[5, 5], [6, 3], [3, 6]]

    # Example 2: Output: 1
    # properties = [[2, 2], [3, 3]]

    # Example 3: Output: 1
    properties = [[1, 5], [10, 4], [4, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfWeakCharacters(properties)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
