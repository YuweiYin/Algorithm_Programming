#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2140-Solving-Questions-With-Brainpower.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2140 - (Medium) - Solving Questions With Brainpower
https://leetcode.com/problems/solving-questions-with-brainpower/

Description & Requirement:
    You are given a 0-indexed 2D integer array questions where questions[i] = [points_i, brainpower_i].

    The array describes the questions of an exam, where you have to process the questions in order 
    (i.e., starting from question 0) and make a decision whether to solve or skip each question. 
    Solving question i will earn you points_i points but you will be unable to solve each of 
    the next brainpower_i questions. If you skip question i, you get to make the decision on the next question.

    For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
        If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
        If instead, question 0 is skipped and question 1 is solved, 
            you will earn 4 points but you will be unable to solve questions 2 and 3.

    Return the maximum points you can earn for the exam.

Example 1:
    Input: questions = [[3,2],[4,3],[4,4],[2,5]]
    Output: 5
    Explanation: The maximum points can be earned by solving questions 0 and 3.
        - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
        - Unable to solve questions 1 and 2
        - Solve question 3: Earn 2 points
        Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:
    Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    Output: 7
    Explanation: The maximum points can be earned by solving questions 1 and 4.
        - Skip question 0
        - Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
        - Unable to solve questions 2 and 3
        - Solve question 4: Earn 5 points
        Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.

Constraints:
    1 <= questions.length <= 10^5
    questions[i].length == 2
    1 <= points_i, brainpower_i <= 10^5
"""


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # exception case
        assert isinstance(questions, list) and len(questions) >= 1
        # main method: (dynamic programming)
        return self._mostPoints(questions)

    def _mostPoints(self, questions: List[List[int]]) -> int:
        assert isinstance(questions, list) and len(questions) >= 1

        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], questions[i][0] + dp[min(n, i + questions[i][1] + 1)])

        return dp[0]


def main():
    # Example 1: Output: 5
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]

    # Example 2: Output: 7
    # questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mostPoints(questions)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
