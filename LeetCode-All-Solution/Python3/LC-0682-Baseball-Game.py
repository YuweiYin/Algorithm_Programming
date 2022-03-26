#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0682-Baseball-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-26
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0682 - (Easy) - Baseball Game
https://leetcode.com/problems/baseball-game/

Description & Requirement:
    You are keeping score for a baseball game with strange rules. 
    The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

    At the beginning of the game, you start with an empty record. You are given a list of strings ops, 
    where ops[i] is the ith operation you must apply to the record and is one of the following:
        An integer x - Record a new score of x.
        "+" - Record a new score that is the sum of the previous two scores. 
            It is guaranteed there will always be two previous scores.
        "D" - Record a new score that is double the previous score. 
            It is guaranteed there will always be a previous score.
        "C" - Invalidate the previous score, removing it from the record. 
            It is guaranteed there will always be a previous score.

    Return the sum of all the scores on the record.

Example 1:
    Input: ops = ["5","2","C","D","+"]
    Output: 30
    Explanation:
        "5" - Add 5 to the record, record is now [5].
        "2" - Add 2 to the record, record is now [5, 2].
        "C" - Invalidate and remove the previous score, record is now [5].
        "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
        "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
        The total sum is 5 + 10 + 15 = 30.
Example 2:
    Input: ops = ["5","-2","4","C","D","9","+","+"]
    Output: 27
    Explanation:
        "5" - Add 5 to the record, record is now [5].
        "-2" - Add -2 to the record, record is now [5, -2].
        "4" - Add 4 to the record, record is now [5, -2, 4].
        "C" - Invalidate and remove the previous score, record is now [5, -2].
        "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
        "9" - Add 9 to the record, record is now [5, -2, -4, 9].
        "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
        "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
        The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:
    Input: ops = ["1"]
    Output: 1

Constraints:
    1 <= ops.length <= 1000
    ops[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
    For operation "+", there will always be at least two previous scores on the record.
    For operations "C" and "D", there will always be at least one previous score on the record.
"""


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # exception case
        assert isinstance(ops, list) and len(ops) > 0
        # main method: (stack stimulate)
        return self._calPoints(ops)

    def _calPoints(self, ops: List[str]) -> int:
        """
        Runtime: 40 ms, faster than 92.91% of Python3 online submissions for Baseball Game.
        Memory Usage: 14.3 MB, less than 12.10% of Python3 online submissions for Baseball Game.
        """
        stack = []

        def __is_number(test_str: str) -> bool:
            if test_str.isdigit():
                return True
            if len(test_str) >= 2 and test_str[0] == "-" and test_str[1:].isdigit():
                return True
            return False

        for op in ops:
            if isinstance(op, str):
                if __is_number(op):
                    stack.append(int(op))
                elif op == "+" and len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
                elif op == "D" and len(stack) >= 1:
                    stack.append(stack[-1] << 1)
                elif op == "C" and len(stack) >= 1:
                    stack.pop()
                else:
                    continue
            else:
                continue

        return sum(stack)


def main():
    # Example 1: Output: 30
    # ops = ["5", "2", "C", "D", "+"]

    # Example 2: Output: 27
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]

    # Example 3: Output: 1
    # ops = ["1"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.calPoints(ops)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
