#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1125-Smallest-Sufficient-Team.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1125 - (Hard) - Smallest Sufficient Team
https://leetcode.com/problems/smallest-sufficient-team/

Description & Requirement:
    In a project, you have a list of required skills req_skills, and a list of people. 
    The i-th person people[i] contains a list of skills that the person has.

    Consider a sufficient team: a set of people such that for every required skill in req_skills, 
    there is at least one person in the team who has that skill. 
    We can represent these teams by the index of each person.

        For example, team = [0, 1, 3] represents the people with skills 
        people[0], people[1], and people[3].

    Return any sufficient team of the smallest possible size, 
    represented by the index of each person. You may return the answer in any order.

    It is guaranteed an answer exists.

Example 1:
    Input: req_skills = ["java","nodejs","reactjs"], 
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    Output: [0,2]
Example 2:
    Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], 
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],
        ["reactjs","csharp"],["csharp","math"],["aws","java"]]
    Output: [1,2]

Constraints:
    1 <= req_skills.length <= 16
    1 <= req_skills[i].length <= 16
    req_skills[i] consists of lowercase English letters.
    All the strings of req_skills are unique.
    1 <= people.length <= 60
    0 <= people[i].length <= 16
    1 <= people[i][j].length <= 16
    people[i][j] consists of lowercase English letters.
    All the strings of people[i] are unique.
    Every skill in people[i] is a skill in req_skills.
    It is guaranteed a sufficient team exists.
"""


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # exception case
        assert isinstance(req_skills, list) and len(req_skills) >= 1
        assert isinstance(people, list) and len(people) >= 1
        # main method: (dynamic programming)
        return self._smallestSufficientTeam(req_skills, people)

    def _smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        assert isinstance(req_skills, list) and len(req_skills) >= 1
        assert isinstance(people, list) and len(people) >= 1

        n, m = len(req_skills), len(people)
        skill_index = {v: i for i, v in enumerate(req_skills)}
        dp = [m] * (1 << n)
        dp[0] = 0

        prev_skill = [0] * (1 << n)
        prev_people = [0] * (1 << n)
        for i, p in enumerate(people):
            cur_skill = 0
            for s in p:
                cur_skill |= 1 << skill_index[s]
            for prev in range(1 << n):
                comb = prev | cur_skill
                if dp[comb] > dp[prev] + 1:
                    dp[comb] = dp[prev] + 1
                    prev_skill[comb] = prev
                    prev_people[comb] = i

        res = []
        i = (1 << n) - 1
        while i > 0:
            res.append(prev_people[i])
            i = prev_skill[i]

        return res


def main():
    # Example 1: Output: [0,2]
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]

    # Example 2: Output: [1,2]
    # req_skills = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
    # people = [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"],
    #           ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestSufficientTeam(req_skills, people)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
