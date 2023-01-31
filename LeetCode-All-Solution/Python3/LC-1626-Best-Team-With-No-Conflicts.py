#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1626-Best-Team-With-No-Conflicts.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1626 - (Medium) - Best Team With No Conflicts
https://leetcode.com/problems/best-team-with-no-conflicts/

Description & Requirement:
    You are the manager of a basketball team. For the upcoming tournament, 
    you want to choose the team with the highest overall score. 
    The score of the team is the sum of scores of all the players in the team.

    However, the basketball team is not allowed to have conflicts. 
    A conflict exists if a younger player has a strictly higher score than an older player. 
    A conflict does not occur between players of the same age.

    Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, 
    respectively, return the highest overall score of all possible basketball teams.

Example 1:
    Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
    Output: 34
    Explanation: You can choose all the players.
Example 2:
    Input: scores = [4,5,6,5], ages = [2,1,2,1]
    Output: 16
    Explanation: It is best to choose the last 3 players. 
        Notice that you are allowed to choose multiple people of the same age.
Example 3:
    Input: scores = [1,2,3,5], ages = [8,9,10,1]
    Output: 6
    Explanation: It is best to choose the first 3 players. 

Constraints:
    1 <= scores.length, ages.length <= 1000
    scores.length == ages.length
    1 <= scores[i] <= 10^6
    1 <= ages[i] <= 1000
"""


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # exception case
        assert isinstance(scores, list) and len(scores) >= 1
        assert isinstance(ages, list) and len(ages) >= 1
        # main method: (dynamic programming)
        return self._bestTeamScore(scores, ages)

    def _bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        assert isinstance(scores, list) and len(scores) >= 1
        assert isinstance(ages, list) and len(ages) >= 1

        age_score = list(zip(ages, scores))
        age_score.sort(key=lambda x: (x[0], x[1]))

        dp = [age_score[i][1] for i in range(len(scores))]
        for i in range(len(scores)):
            for j in range(i):
                if age_score[i][1] >= age_score[j][1]:
                    dp[i] = max(dp[i], dp[j] + age_score[i][1])

        return max(dp)


def main():
    # Example 1: Output: 34
    scores = [1, 3, 5, 10, 15]
    ages = [1, 2, 3, 4, 5]

    # Example 2: Output: 16
    # scores = [4, 5, 6, 5]
    # ages = [2, 1, 2, 1]

    # Example 3: Output: 6
    # scores = [1, 2, 3, 5]
    # ages = [8, 9, 10, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.bestTeamScore(scores, ages)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
